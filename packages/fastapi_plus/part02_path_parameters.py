from fastapi import FastAPI, APIRouter

RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Getivorn
    """
    return {"msg": "Hello, World!"}

@api_router.get("/recipes/{recipe_id}", status_code=200)
def get_recipe(*, recipe_id: int) -> dict:
    """
    Get a recipe by ID.
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    print(result, type(result))
    if not result:
        return {"msg": "Recipe not found", "code": 404}
    return result[0]

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8001, log_level="debug")