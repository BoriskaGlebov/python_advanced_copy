"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange
from hw2_validators import number_length, NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(
        validators=[
            InputRequired(message="Форма почты пуста"),
            Email(message="некорректный формат почты"),
        ]
    )
    # phone = IntegerField(validators=[InputRequired(message='номер пуст'), NumberRange(min=1000000000,max=9999999999,message='номер некорректен')])
    # phone = IntegerField(
    #     validators=[InputRequired(message='номер пуст'), number_length(11, 11, message='номер некорректен')])
    phone = IntegerField(
        validators=[
            InputRequired(message="номер пуст"),
            NumberLength(11, 11, message="номер некорректен"),
        ]
    )
    name = StringField(validators=[InputRequired(message="Имя не заполнено")])
    address = StringField(validators=[InputRequired(message="адрес пуст")])
    index = IntegerField(validators=[InputRequired(message="индекс пуст")])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"
    # if form.errors:
    # print('sfsdf', form.errors)

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
