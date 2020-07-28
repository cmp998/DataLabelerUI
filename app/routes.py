from app import app, db
from app.forms import TweetForm
from flask import render_template, flash, redirect
from app.models import Tweet
import csv
import os
import time

#tweet = Tweet(tID = 1, given_text = "Example tweet", selected_text = "", primary_sent = 0, secondary_sent = 0, completed = 0)

@app.route('/', methods=['GET','POST'])
def index():
    #get randon tID that is not completed
    TODOs = db.session.query(Tweet).filter(Tweet.primary_sent<0)
    #print(TODOs[0])
    #tID = "1"
    return redirect('/label/' + str(TODOs[0].tID))
    

@app.route('/label/<string:tID>', methods=['GET', 'POST'])
def label(tID):
    form = TweetForm()
    #VALID tID
    if Tweet.query.get(tID):
        tweet = Tweet.query.get(tID)

        #Update this and reload, POST then GET
        if form.validate_on_submit():

            #Auto fill in the neurtal sent to be all given_text otherwise use selected text
            if form.primary_sent.data == 0:
                print("found 0")
                tweet.selected_text = tweet.given_text
            else:
                tweet.selected_text = form.selected_text.data

            tweet.primary_sent = form.primary_sent.data
            tweet.secondary_sent = form.secondary_sent.data

            db.session.commit()

            if (Tweet.query.get(tID)):
                successfully_labeled = Tweet.query.get(tID)
                print("Successfully added: " + successfully_labeled.selected_text + " as " + str(successfully_labeled.primary_sent))
                
                #log this labelled tweet
                basedir = os.path.abspath(os.path.dirname(__file__))
                log_file = os.path.join(basedir, 'log/live_results.log')

                print(successfully_labeled.tID,
                        successfully_labeled.given_text,
                        successfully_labeled.selected_text,
                        successfully_labeled.primary_sent,
                        successfully_labeled.secondary_sent,
                        sep = ",", file = open(log_file, "a"))
                #Go back to the beginning to get a new ID
                return redirect('/')
            else:
                print("Failed adding: ", tID)
        #This is a fresh tweet and needs to be labeled
        else:
            return render_template('index.html', form=form, tweet=tweet)
    #Not a valid tID
    else:
        bad_id_tweet = Tweet(tID = -1, given_text = "---Tweet ID not found in database---\nPlease click home to find a new one!", primary_sent = -1, secondary_sent = -1)
        return render_template('index.html', form=form, tweet=bad_id_tweet)    
    
@app.route('/import/<string:filename>', methods=['GET', 'POST'])
def db_import(filename):
    print(filename)

    basedir = os.path.abspath(os.path.dirname(__file__))
    import_file = os.path.join(basedir, 'static/import/' + filename + '.csv')
    log_file = os.path.join(basedir, 'log/err_' + filename + '.log')
    
    tID_column = 1
    given_text_column = 2
    
    #print("Pre: ", Tweet.query.all())

    with open(import_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            #Nonunique tID handler
            if Tweet.query.get(int(row[tID_column])):
                print("<Tweet " + row[tID_column] + "> was found in the database already" + time.time(), file = open(log_file, "a"))
            new_tweet = Tweet(
                tID = int(row[tID_column]),
                given_text = row[given_text_column],
                selected_text = "",
                primary_sent = -1,
                secondary_sent = -1,
            )
            print(new_tweet)
            db.session.add(new_tweet)
            db.session.commit()

    #print("Post: ", Tweet.query.all())
    return redirect('/')

@app.route('/export/<string:filename>', methods=['GET', 'POST'])
def db_export(filename):
    print(filename)

    basedir = os.path.abspath(os.path.dirname(__file__))
    results_file = os.path.join(basedir, 'log/results_' + filename + '.log')

    labelled_tweets = db.session.query(Tweet).filter(Tweet.primary_sent > -1)
    
    for tweet in labelled_tweets:
        print(tweet.tID,
                tweet.given_text,
                tweet.selected_text,
                tweet.primary_sent,
                tweet.secondary_sent,
                sep = ",", file = open(log_file, "a"))
    return redirect('/')
