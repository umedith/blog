from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    # vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
    submit = SubmitField('SUBMIT')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title = StringField('Enter title',validators = [Required()])
    subtitle= StringField('Enter subtitle',validators = [Required()])
    content = TextAreaField('make a blog', validators=[Required()])
    submit = SubmitField('Create Pitch')