from recipes_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__( self, firstName, secondName, email, password ):
        self.firstName = firstName
        self.secondName = secondName
        self.email = email
        self.password = password
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "recipes_db" ).query_db( query )
        users = []
            for user in results:
                users.append(User(user['firstName'], user['secondName'], user['email'], user['password']))
            return users

    @classmethod
    def add_user(cls, newUser):
        query = f"INSERT INTO users(firstName, secondName, email, password) VALUES (%(newUser.firstName)s, %(newUser.secondName)s, %(newUser.email)s, %(newUser.password)s)"
        data = {
            "firstName" : newUser.firstName,
            "secondName" : newUser.secondName,
            "email" : newUser.email,
            "password" : newUser.password
        }
        result = connectToMySQL( "recipes_db" ).query_db( query, data )
        return result