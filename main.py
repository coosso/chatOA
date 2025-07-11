from fastapi import FastAPI
from pydantic import BaseModel
from packages.prompt.prompt_flow import extract_leave_info

app = FastAPI()

# 定义请求体模型
class LeaveRequest(BaseModel):
    user_input: str


@app.get("/chat/{user_input}")
async def get_leave_info(user_input: str):
    result = await extract_leave_info(user_input)
    if result:
        print(result)
    if result:
        return result
    return {"message": "未能成功提取请假信息"}


@app.get("/result")
def get_result():
    return {"result": "ss"}

user_input = (
        "明天是2026年7月1日，帮我请个明天的假，理由是因为要去参加一个重要的家庭聚会。"
    )
result = extract_leave_info(user_input)
if result:
    print(result)
