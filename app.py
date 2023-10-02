from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'description': 'This is a job desciption'
        
    },  
    {  
        'id': 2,
        'title': 'Software Engineer',
        'description': 'This is a job desciption'
        
    }, 
    { 
     
        'id': 3,
        'title': 'Software Engineer',
        'description': 'This is a job desciption'
    },
]

@app.route('/')
def index():
    return render_template('index.html',jobs = JOBS)

if __name__ == "_main_":
    app.run(host='0.0.0.0', debug = True)