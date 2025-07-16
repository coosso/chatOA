from fastapi import FastAPI, APIRouter
from typing import Optional

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

router = APIRouter()


@router.get("/", status_code=200)
def root() -> dict:
    return {"msg": "hello"}


@router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if not result:
        return {"msg": "Recipe not found", "code": 404}
    return result[0]

@router.get("/search/", status_code=200)
def search_recpies(
    keyword: Optional[str] = None,
    max_results: Optional[int] = 5
):
    if not keyword:
        return {"results": RECIPES[:max_results]}
    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)    
    return {"results": list(results)[:max_results]}

app.include_router(router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run("part03_query_parameters:app", port=8001, reload=True)
