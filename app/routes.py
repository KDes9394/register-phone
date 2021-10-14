from flask import render_template
from app.forms import UserInfoForm, PostForm
from app.models import User, Post
from app import db, app

@app.route('/')
def index():
    title = 'Coding Temple Flask'
    return render_template('index.html', title=title)


@app.route('/enter_phone', methods=['POST'])
def enter_phone():
    phone_form = UserInfoForm()
    if phone_form.validate_on_submit():
        print('Hello this form has been submitted correctly')
        first_name = phone_form.first_name.data
        last_name = phone_form.last_name.data
        password = phone_form.password.data
        print(first_name, last_name, password)
        new_phone = User(first_name, last_name, password)
        db.session.add(phone_form)
        db.session.commit()

    return render_template('entire_phone.html', form=phone_form)