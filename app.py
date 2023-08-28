# My flask application again
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Aditya@123!@10.0.1.23/lilly'
db = SQLAlchemy(app)
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')
  return render_template('index.html')
if __name__ == '__main__':
  with app.app_context():
      db.create_all()
app.run(host='0.0.0.0',port=8080
      
