from flask import Flask, render_template, request, redirect, session
from recipes_app import app
from recipes_app.controllers import users_controller, recipes_controller



users=[ 
    {
    "name" : "Jr",
    "email" : "correo@gmail.com",
    "password":"pass123"
    },
    {
    "name" : "Lauddra",
    "email" : "corrddeo2@gmail.com",
    "password":"123perro"
    },
]

recipes = {
    "hot dog": [
        {
            "description" : "hot dog",
            "instructions" : "Hot Dog Instructions",
            "timemaking" : "Yes",
            "date":"today"
        }
    ],
    "taco": [
        {
            "description" : "taco",
            "instructions" : "taco Instructions",
            "timemaking" : "Yes",
            "date":"today"
        }
    ]
}

@app.route('/', methods=['GET'])                           
def login():
    loginError = ""
    if 'loginError' in session:
        loginError = session['loginError']
    return render_template('index.html', loginError=loginError)

@app.route('/home', methods=['GET'])                           
def displayHome():
#   if 'userEmail' in session: #change for name
#         userEmail = session ['userEmail']
#        currentUserTodos = 
    return render_template('dashboard.html')

@app.route('/authentication', methods=['POST'])                           
def validateCredentials():
    userEmail = request.form ['email']
    userPassword = request.form ['password']
    for user in users:
        if user ['email'] == userEmail and user ['password'] == userPassword:
            session ['userEmail'] = userEmail
            if 'loginError' in session:
                session.pop('loginError')
            return redirect ('/recipes')
    session['loginError'] = "Wrong credentials provided."
    return redirect ('/')

@app.route ('/logout', methods=['GET'])
def closeSession():
    session.clear()
    responseObj = {
        'message': 'Logout successfully'
    }
    return responseObj


@app.route("/users", methods=['GET'])
def getAllUsers():
    users = User.get_all_users()
    return render_template ("users.html", users=users)




#@app.route('/register', methods=['POST'])
#def create_user():


if __name__=="__main__":   
    app.run(debug=True) 