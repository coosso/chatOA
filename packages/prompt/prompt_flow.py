from langchain_community.chat_models.tongyi import ChatTongyi
from langchain.schema import HumanMessage, SystemMessage
import json
import os

# 初始化大语言模型，这里以 Qwen 为例，你需要替换为实际的 API 密钥
chat = ChatTongyi(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen-plus",
)

# 系统提示词，定义助手的角色和任务
system_prompt = """你是一个办公聊天自动化处理助手。用户会向你提出请假要求，你的任务是从用户的输入中提取请假开始时间、结束时间和请假理由，并以 JSON 格式返回。
JSON 格式示例：
{
    "dateStart": "具体开始时间",
    "dateEnd": "具体结束时间",
    "duration": "请假时长",
    "reason": "具体请假理由"
}
时间为yyyy/MM/dd HH:mm:ss格式
durationj为小时数
返回纯json数据，不要有markdonwn格式
如果用户输入中未明确开始时间或结束时间，相应字段可以为空字符串。如果没有明确的请假理由，理由字段可以填写“未说明”。"""

async def extract_leave_info(user_input):
    try:
        # 构建消息列表
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ]
        # 调用大模型获取响应
        response = chat.invoke(messages)
        print(response.content)
        try:
            # 尝试将响应内容解析为 JSON
            leave_info = json.loads(response.content)
            return leave_info
        except json.JSONDecodeError as e:
            print(f"无法将响应解析为 JSON 格式，错误信息: {e}")
            return None
    except Exception as e:
        print(f"调用大模型时出现错误: {e}")
        return None

if __name__ == "__main__":
    user_input = "明天是2026年7月1日，帮我请个明天的假，理由是因为要去参加一个重要的家庭聚会。"
    result = extract_leave_info(user_input)
    if result:
        print(result)
