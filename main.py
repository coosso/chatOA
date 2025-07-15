from fastapi import FastAPI
from pydantic import BaseModel
from packages.prompt.prompt_flow import extract_leave_info
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 配置允许的跨域来源列表
origins = [
    "http://localhost",
    "http://localhost:5173",  # 常见的前端开发端口
    # 可按需添加其他允许的域名
]

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

# 定义请求体模型
class LeaveRequest(BaseModel):
    user_input: str

@app.post("/chat/{user_input}")
async def get_leave_info(user_input: str):
    result = await extract_leave_info(user_input)
    if result:
        print(result)
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
