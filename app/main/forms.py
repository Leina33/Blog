from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import Subscriber
from wtforms import ValidationError


class PostForm(FlaskForm):
    title = StringField("Post Title",validators=[Required()])
    post = TextAreaField("Write your post here")
    category = SelectField("Post Category",choices=[('Travel','Travel'),('Fashion','Fashion'),('Hobby','Hobby'),('Life','Life')],validators=[Required()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    email = StringField("Email Address",validators=[Required(),Email()])
    submit = SubmitField("Submit")

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email =data_field.data).first():
            raise ValidationError("Account already subscribed with that email")

class CommentForm(FlaskForm):
    comment = TextAreaField("Leave a Comment")
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')