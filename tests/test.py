import asyncio
async def task1():
    await asyncio.sleep(1)
    print("任务1完成")


async def task2():
    await asyncio.sleep(0.5)
    print("任务2完成")


async def main():
    # 创建并运行多个任务
    await asyncio.gather(task1(), task2())


asyncio.run(main())
# 输出:
# 任务2完成
# 任务1完成
