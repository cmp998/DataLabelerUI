from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class TweetForm(FlaskForm):
    #ID = IntegerField('tID', validators=[DataRequired()])
    #givenID = IntegerField('givenID')
    selected_text = StringField('Selected Text')
    #given_text = StringField('Given Text')
    primary_sent = RadioField('Primary Sentiment', coerce = int, choices=[
            (-1, 'TODO'), (0, 'neutral'), (1, 'optimistic'), (2, 'happy'),
            (3, 'sad'), (4, 'surprise'), (5, 'fear'), (6, 'anger'),
            (7, 'denial'), (8, 'joking'), (9, 'pessimistic'),
            ], default = -1)
    secondary_sent = RadioField('Secondary Sentiment', coerce=int, choices=[
            (-1, 'TODO'), (0, 'neutral'), (1, 'optimistic'), (2, 'happy'),
            (3, 'sad'), (4, 'surprise'), (5, 'fear'), (6, 'anger'),
            (7, 'denial'), (8, 'joking'), (9, 'pessimistic'),
            ], default = -1)
    #completed = IntegerField('Completed')
    submit = SubmitField('Complete')
"""
class SearchForm(FlaskForm):
    patient_id = StringField('Patient ID', validators=[DataRequired()])
    doctor_id = StringField('Doctor ID')
    medication_id = StringField('Medication ID')
    report_id = StringField('Report ID')
    submit = SubmitField('Search')

class NewPatientForm(FlaskForm):
    ssn = StringField('SSN*', validators=[DataRequired()])
    full_name = StringField('FullName*', validators=[DataRequired()])
    dob = StringField('DOB*', validators=[DataRequired()])
    phone = StringField('Phone*', validators=[DataRequired()])
    gender = StringField('Gender*', validators=[DataRequired()])
    submit = SubmitField('Create')


class NewReportForm(FlaskForm):
    report_id = StringField('Report ID*', validators=[DataRequired()])
    ssn = StringField('SSN*', validators=[DataRequired()])
    doc_id = StringField('Doctor ID*', validators=[DataRequired()])
    med_id = StringField('Medication ID')
    purpose = StringField('Purpose of Visit')
    patient_info = StringField('Patient Info')
    doc_name = StringField('Doctor Name')
    doc_address = StringField('Doctor Address')
    department_name = StringField('Doctor Department')
    hospital_name = StringField("Hospital Name")
    submit = SubmitField('Create')

class EditReport(FlaskForm):
    report_id = StringField('Report ID*', validators=[DataRequired()])
    ssn = StringField('SSN*', validators=[DataRequired()])
    doc_id = StringField('Doctor ID*', validators=[DataRequired()])
    med_id = StringField('Medication ID')
    purpose = StringField('Purpose of Visit')
    patient_info = StringField('Patient Info')
    submit = SubmitField('Save')

class EditDoctor(FlaskForm):
    doc_id = StringField('Doctor ID*', validators=[DataRequired()])
    doc_name = StringField('Doctor Name')
    address = StringField('Doctor Address')
    department_name = StringField('Doctor Department')
    hospital_name = StringField("Hospital Name")
    submit = SubmitField('Save')

class EditMed(FlaskForm):
    report_id = StringField('Report ID')
    med_id = StringField('Medication ID', validators=[DataRequired()])
    submit = SubmitField('Save')
"""