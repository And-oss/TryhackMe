from flask import Flask , render_template , request
from routes import *
from database import database
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2008@localhost/ash'

db = SQLAlchemy(app)

@app.route(routes.main , methods = ['GET' , 'POST'])
def mainPage():
    if request.method == 'POST':
        username = request.form.get('Nick')
        password = request.form.get('passwd')
        email = request.form.get("email")

        User = database.user(username , password , email)
        db.session.add(User)
        db.session.commit()

    return render_template("Main.html")


if __name__ == '__main__':
    app.run()