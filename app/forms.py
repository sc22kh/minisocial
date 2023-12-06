from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired,NumberRange

class FilterForm(FlaskForm): 
   tag = StringField("Tag") #Find way to search with multiple tags

class LoginForm(FlaskForm):
   username = StringField("Username", validators=[DataRequired()])
   password = PasswordField("Password", validators=[DataRequired()])

class NewPostForm(FlaskForm):
   title = StringField("Title", validators=[DataRequired()])
   body = StringField("Body", validators=[DataRequired()])
   tags = StringField("Tags")

"""
class NewTransactionForm(FlaskForm):
    transaction_type = SelectField("Transaction Type",choices=["Income","Expenditure"],validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    amount = DecimalField("Amount",places=2,validators=[DataRequired(),NumberRange(min=0)])
    model_type = StringField("Type", validators=[DataRequired()])

class NewGoalForm(FlaskForm):
   name = StringField("Name", validators=[DataRequired()])
   amount = DecimalField("Amount",places=2,validators=[DataRequired(),NumberRange(min=0)])
"""
    
