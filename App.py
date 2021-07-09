from flask import Flask, render_template, request, redirect, url_for # here we're importing Flask into our python file and callign render_template and request

app = Flask(__name__) # create an instance of flask

@app.route('/') #write and specify the route
def index(): # this is the route path - first page of any website (but just a convention)
    return render_template('login.html') # create a login page by rendering it and create a template for the home page

@app.route('/login', methods = ['POST']) # create login endpoint add methods = ['POST'] because login is a route that is expecting methods to be defined
def login(): # define the function for the login route
    user = {
        "username": "tom",
        "password": 1234
    }

    username = request.form['Username'] #to colect data from end point - here we're capturing the username and password
    password = request.form['Password']
    
    if username == 'tom': #checking if username and password are correct
        if password == '1234':
            return redirect(url_for('scores', username = username)) #url_for to pass it to the url for scores. so, if username and password are correct this will direct user to their scores page

    return "Wrong credentials"+ str(username)


@app.route('/scores/<username>') # create scores endpoint and pass username
def scores(username): # create function to return the user's scores and pass username as a parameter
    exams = [ #create a list of dictionaries with the data being the scores for the exams taken by the user
        {
            "subjectName": "Python",
            "marks": "20/25",
            "date": "13-04-2021"

        },
        {
            "subjectName": "C#",
            "marks": "2/25",
            "date": "13-04-2021"

        },
        {
            "subjectName": "JavaScript",
            "marks": "25/25",
            "date": "13-04-2021"

        },
    ]
    return render_template('scores.html', scores = exams, username = username) # rendering the data in the dictionary and calling scores.html



if __name__ == '__main__':
    app.run(debug = True) #this shows its still in debug mode





