from recipes_app.config.MySQLConnection import connectToMySQL

class Recipes:
    def __init__( self, rcp_id, rcp_name, rcp_description, rcp_instructions, rcp_timemaking, rcp_date ):
        self.rcp_id = rcp_id
        self.rcp_name = rcp_name
        self.rcp_description = rcp_description
        self.rcp_instructions = rcp_instructions
        self.rcp_timemaking = rcp_timemaking
        self.rcp_date = rcp_date
    
    @classmethod
    def get_all_recipes(cls):
        query= "SELECT * FROM recipes;"
        results= connectToMySQL( "recipes_db" ).query_db( query )
        return results