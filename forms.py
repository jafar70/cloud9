from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import InputRequired 

class ContactForm(Form):
  name = TextField("Name", validators=[InputRequired('Please enter your name.')])
  email = TextField("Email",  validators=[InputRequired("Please enter your email address.")])
  subject = TextField("Subject",  validators=[InputRequired("Please enter a subject.")])
  message = TextAreaField("Message",  validators=[InputRequired("Please enter a message.")])
  submit = SubmitField("Send")
