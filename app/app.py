from fastapi import FastAPI

app = FastAPI()

result = 'ss'

@app.get("/")
def get_result():
    return {"result": result}