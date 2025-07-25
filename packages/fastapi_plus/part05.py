from fastapi import FastAPI, APIRouter, Query, HTTPException

from typing import Optional

from packages.schemas import RecipeSearchResults, Recipe, RecipeCreate

from packages.recipe_data import RECIPES


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}


# Updated using to use a response_model
# https://fastapi.tiangolo.com/tutorial/response-model/
@api_router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a s
    """

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]    
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"{recipe_id} not found"
        )        
    return result[0]


# Updated using the FastAPI parameter validation `Query` class
# # https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    *,
    keyword: Optional[str] = Query(
        None,
        min_length=3,
        openapi_examples={
            "chickenExample": {
                "summary": "A chicken search example",
                "value": "chicken",
            }
        },
    ),
    max_results: Optional[int] = 10,
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}


# New addition, using Pydantic model `RecipeCreate` to define
# the POST request body
@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> dict:
    """
    Create a new recipe (in memory only)
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.model_dump())

    return recipe_entry


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run("part05:app", port=8001, log_level="debug", reload=True)
