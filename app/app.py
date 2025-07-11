from fastapi import FastAPI

app = FastAPI()

result = 'ss'

@app.get("/result")
def get_result():
    return {"result": result}