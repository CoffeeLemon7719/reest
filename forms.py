from wtforms import Form
from wtforms import StringField, TextAreaField
from wtforms.fields import EmailField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import validators
from models import User

def lenght_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(Form):
    comment = TextAreaField('Comentario')
    honeypot = HiddenField('',[lenght_honeypot])

class LoginForm(Form):
    username = StringField(
        "Usuario",
        [validators.length(min=4, max=25), validators.DataRequired()]
    )
    password = PasswordField('',[validators.DataRequired()])


class CreateForm(Form):
    username = StringField(
        "username",
        [validators.length(min=4, max=50), validators.DataRequired()],
    )
    email = EmailField(
        "Correo electronico",
        [validators.length(min=4, max=50), validators.DataRequired()],
    )
    password = PasswordField('Password', [validators.DataRequired()])

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('El username ya se encuentra registrado')


