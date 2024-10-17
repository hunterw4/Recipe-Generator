from flask import Flask, render_template, redirect, url_for, request
from API import GenerateRecipe
import json

app = Flask(__name__)

steps = []
the_recipe = []

@app.route("/", methods=["GET","POST"])
def home():
    pass
    return render_template("index.html")

@app.route("/recipe", methods=["GET","POST"])
def recipe():
    if request.method == "POST":
        category = request.form.get('food-categories')
        diet = request.form.get('diet-preferences')
        city = request.form.get('city')
        if diet == "":
            diet = "NA"
        if city == "":
            city = "NA"
        generate = GenerateRecipe(category, diet, city)
        recipe_data = generate.recipe_response()
        print(recipe_data)


        name = recipe_data["name"]
        short_desc = recipe_data["short_desc"]
        description = recipe_data["description"]
        ingredients = recipe_data["ingredients"]
        nutritional_info = recipe_data["nutritional_info"]
        preparation_steps = recipe_data["preparation_steps"]
        cooking_time = recipe_data["cooking_time"]
        serving_size = recipe_data["serving_size"]
        serving_suggestion = recipe_data["serving_suggestion"]
        dish_significance = recipe_data["dish_significance"]

        cal = nutritional_info.get('calories', 'N/A'),
        protein = nutritional_info.get('protein', 'N/A'),
        carbs = nutritional_info.get('carbohydrates', 'N/A'),
        fat = nutritional_info.get('fat', 'N/A'),
        fiber = nutritional_info.get('fiber', 'N/A'),
        sodium = nutritional_info.get('sodium', 'N/A')

    return render_template("recipe.html", recipe_title=name, short_desc=short_desc, description=description,
                           ingredients=ingredients, nutritional_info=nutritional_info,preparation_steps=preparation_steps,
                           cooking_time=cooking_time,serving_size=serving_size,serving_suggestion=serving_suggestion,
                           dish_significance=dish_significance, cal=cal,protein=protein,carbs=carbs,fat=fat,fiber=fiber,
                           sodium=sodium)



if __name__ == "__main__":
    app.run(debug=True)