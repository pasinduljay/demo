from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class UserForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    users = User.query.all()
    return render_template('index.html', form=form, users=users)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
