from dotenv import load_dotenv
import os

load_dotenv()
# DASHSCOPE_API_KEY = os.getenv('DASHSCOPE_API_KEY')
# print(DASHSCOPE_API_KEY)  

from langchain_core.globals import set_debug
set_debug(True)

from langchain import hub

# 从Langchain Hub中获得React的提示
prompt = hub.pull('hwchase17/react')
# print(prompt)

from langchain_community.chat_models.tongyi import ChatTongyi
llm = ChatTongyi(model="qwen-turbo")

from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import tool
@tool
def google_search(query: str) -> str:
    """
    当大模型没有相关知识时，用于搜索知识
    """
    search = SerpAPIWrapper()
    results = search.run(query)
    return results
tools = [google_search]

# 导入create_react_agent功能
from langchain.agents import create_react_agent
# 构建ReAct Agent
agent = create_react_agent(llm, tools, prompt=prompt)

from langchain.agents import AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input": "美国总统多大年纪？"})
