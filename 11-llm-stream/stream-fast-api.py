from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

def format_sse(data: str, event=None) -> str:
    msg = 'data: {}\n\n'.format(data)
    if event is not None:
        msg = 'event: {}\n{}'.format(event, msg)
    return msg

# 模拟大模型生成文本的过程
async def generate(prompt: str):
    """
    模拟基于输入 prompt 生成长文本的过程，分段逐步返回
    :param prompt: 输入文本
    """
    # 假设这个过程是一个非常复杂且耗时的模型推理
    # 我们将生成分为多个步骤
    parts = [
        f"{prompt} Part 1: The beginning of the story...",
        "Part 2: The middle of the story is where things get complicated...",
        "Part 3: The end of the story comes with a surprising twist...",
        "Part 4: The final resolution and conclusion..."
    ]
    
    for part in parts:
        yield format_sse(part, "delta")
        await asyncio.sleep(1)  # 模拟模型推理的延迟，通常这会是网络请求或计算过程

@app.get("/stream_chat/")
@app.post("/stream_chat/")
async def stream_chat(prompt: str):
    """
    提供一个生成式流式接口，逐步返回生成的文本内容
    """
    return StreamingResponse(generate(prompt), media_type="text/event-stream")
