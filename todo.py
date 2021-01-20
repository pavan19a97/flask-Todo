from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="Pavan@8824",url="localhost:5234",db="todotasks")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/todotasks"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class TodoModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())

    def __init__(self, id,task):
        self.id = id
        self.task = task

    def __repr__(self):
        return f"<Todo {self.task}>"



@app.route('/')
def index():
        tasks = TodoModel.query.all()
        return render_template("index.html", tasks = tasks)

@app.route('/add', methods=['POST'])
def add():
    data = request.form.get("task")
    id = int(time.time())
    new_ele = TodoModel(id= id, task = data)
    db.session.add(new_ele)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    

    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    task = TodoModel.query.get(todo_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index")) 
        


if __name__ == '__main__':
    app.run(debug=1)
