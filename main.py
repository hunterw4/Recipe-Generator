from flask import Flask, render_template, redirect, url_for, request
from API import GenerateRecipe

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
        test = GenerateRecipe(category, diet, city)
        response = test.recipe_response()
        print(response)
    return render_template("recipe.html", steps=steps, the_recipe=the_recipe)


if __name__ == "__main__":
    app.run(debug=True)