from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class BlogForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	content = TextAreaField("Post Blog",validators=[Required()])
	submit = SubmitField('POST')

class CommentForm(FlaskForm):
    comment = StringField('comment', validators=[Required()])
    submit = SubmitField('COMMENT')

class UpdatePostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Update Blog')