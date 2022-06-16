from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@34.142.44.27:3306/earl"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRET_KEY" # change to os.getenv("SECRET_KEY") 

db = SQLAlchemy(app)


class Owners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    cars = db.relationship('Car', backref='ownerbr')


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg = db.Column(db.String(10), unique=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)


class OwnerForm(FlaskForm):
    first_name = StringField("First Name: ")
    last_name = StringField("Last Name: ")
    submit = SubmitField("Submit")


@app.route('/')
def homePage():
    list_of_owners = Owners.query.all()
    
    return render_template('index.html', list1=list_of_owners)


@app.route('/home')
def home():
    return render_template('index.html', names=["Dave", "John", "Daisy"])

@app.route('/create/<f_name>/<l_name>')
def createEntry(f_name, l_name):
    new_entry = Owners(first_name=f_name, last_name=l_name)
    db.session.add(new_entry)
    db.session.commit()
    return render_template('index.html')




@app.route('/add-owner', methods=["GET", "POST"])
def add_owner():
    form = OwnerForm()


    if request.method == 'POST':
        if form.validate_on_submit():
            new_entry = Owners(first_name=form.first_name.data, last_name=form.last_name.data)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('homePage'))


    return render_template('add_owner.html', form=form)







@app.route('/update/<int:id>/<name>')
def update(id, name):
    updated_item = Owners.query.get(id)
    updated_item.first_name = name
    db.session.commit()
    return redirect(url_for("homePage"))


@app.route('/delete/<int:id>')
def delete(id):
    deleted_item = Owners.query.get(id)
    db.session.delete(deleted_item)
    db.session.commit()
    return redirect(url_for("homePage"))


@app.route('/about', methods=['GET', 'POST'])
def about():
    return "Info about the whole team"


@app.route('/about/dave')
def aboutDave():
    return "Info about dave"
    
@app.route('/about/steve')
def aboutSteve():
    return "Info about Steve"

@app.route('/goog')
def goog():
    return redirect('https://www.google.com')



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)