# DataLabelerUI
Quick web application to help with labeling data sets faster

There is an installation script that should help with any dependencies needed.

Instructions for starting:
1. Copy the input file into app/static/import (.csv supported) (you'll need to remove the header row at the top)
2. Start up the applcation using 'flask run' in the terminal
3. Open up the page (you'll get a 500 error since it defaults to finding the next tweet but there isn't one yet)
4. Go to http://127.0.0.1:5000/import/[name_of_file.csv] (You should see each tweet being imported in the terminal)
5. It should load directly into the first unlabelled tweet
6. Use the buttons to select emotions
7. Copy paste the selected text into the box (if you select neutral as the primary it will autofill with all of the given text)
8. Each time complete a tweet it'll output into the live_results file in app/log.
    
When I finish with a set I'll rename it to archive it.  I normally throw it into excel add the headers and the two columns that convert
emtoion numbering into english text.
