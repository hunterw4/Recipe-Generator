import os
from openai import OpenAI


class GenerateRecipe():
    OPENAI_API_KEY = os.environ.get("OPENAI_KEY")
    def __init__(self, category, diet, city):
        self.category = category
        self.diet = diet
        self.city = city

    def recipe_response(self):
        client = OpenAI(
            api_key=self.OPENAI_API_KEY
        )

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """You will be generating a me a recipe based off the user's input. The user may enter a city that the dish must originate from. If the city does not exist just generate a dish based off of the other requests. in the following JSON format: 
                        Provide the details of the recipe in the following JSON format:
                        {
                          "name": "Dish Name",
                          "short_desc": "Short description as subtitle",
                          "description": "Recipe description",
                          "ingredients": ["list of ingredients"],
                          "nutritional_info": {
                            "calories": "number of calories",
                            "protein": "amount of protein",
                            "fat": "amount of fat",
                            "carbohydrates": "amount of carbohydrates",
                            "fiber": "amount of fiber",
                            "sodium" "amount of sodium
                          },
                          "preparation_steps": ["list of steps to prepare the dish"],
                          "cooking_time": "time required to cook",
                          "serving_size": "number of servings",
                          "serving_suggestion": "suggestions for how recipe should be served",
                          "dish_significance: "significance of the dish in relation to the place of origin and culture"
                        }"""},
                {
                    "role": "user",
                    "content": f"{self.category, self.diet, self.city}"
                }
            ]
        )

        recipe = print(completion.choices[0].message)
        return recipe
