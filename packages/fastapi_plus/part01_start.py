from fastapi import FastAPI, APIRouter

# 1
app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

# 2
api_router = APIRouter()

# 3
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Getivorn
    """
    return {"msg": "Hello, World!"}

# 4
app.include_router(api_router)


# 5
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, port=8001, log_level="debug")