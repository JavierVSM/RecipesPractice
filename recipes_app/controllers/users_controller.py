from flask import render_template, request, redirect
from recipes_app import app
from recipes_app.models.User import User

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "users.html", users=users )


@app.route ("/register", methods = ['POST'] )
def addUser():
    firstName= request.form ['firstName']   
    secondName= request.form ['secondName']
    email= request.form ['email'] 
    password= request.form ['password']  

    newUser = User( firstName, secondName, email, password )
    result = User.add_user(newUser)
    print (result)
    return redirect ( "/users")
