from recipes_app import app
from flask import render_template
from recipes_app.models.Recipes import Recipes


@app.route("/recipes", methods=['GET'])
def getAllRecipes():
    recipes = Recipes.get_all_recipes()
    return render_template ("dashboard.html", recipes=recipes)
