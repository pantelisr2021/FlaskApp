from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField(label="Όνομα χρήστη",
                        validators=[DataRequired(message="Αυτό το πεδίο δεν μπορεί να είναι κενό"),
                                    Length(min=5, max=15, message="Αυτό το πεδίο πρέπει να είναι από 3 εως 15 χαρακτήρες")])
    email = StringField(label="Email",
                        validators=[DataRequired(message="Αυτό το πεδίο δεν μπορεί να είναι κενό"),
                                    Email(message = "Παρακαλώ εισάγετε σωστά το εμαιλ")])
    password=StringField(label="Password",
                        validators=[DataRequired(message="Αυτό το πεδίο δεν μπορεί να είναι κενό"),
                                    Length(min=5, max=15, message="Αυτό το πεδίο πρέπει να είναι από 3 εως 15 χαρακτήρες")])                 
    password2=StringField(label="Επιβεβαίωση password",
                          validators=[DataRequired(message="Αυτό το πεδίο δεν μπορεί να είναι κενό"),
                                     EqualTo("password"),
                                     Length(min=5, max=15, message="Αυτό το πεδίο πρέπει να είναι από 3 εως 15 χαρακτήρες")])
    submit=SubmitField("Εγγραφή") 


class LoginForm(FlaskForm):
    email=StringField(label="Email",
                        validators=[DataRequired(message="Αυτό το πεδίο δεν μπορεί να είναι κενό"),
                                    Email(message = "Παρακαλώ εισάγετε σωστά το εμαιλ")])
    password=StringField(label="Password",
                        validators=[DataRequired(message="Αυτό το πεδίο δεν μπορεί να είναι κενό")])
    submit=SubmitField("Σύνδεση") 