import asyncio
import time

async def my_func(name, delay):
    print(f"任务 {name} 开始")
    await asyncio.sleep(delay)
    print(f"任务 {name} 完成")
    return f"任务 {name} 结果"

async def main_sync():
    print("--- 串行执行---")
    asyncio.create_task(my_func("A", 2)) 
    await my_func("B", 2)
    await asyncio.sleep(4)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main_sync())
    end_time = time.time()
    print(f"串行耗时: {end_time - start_time:.2f}秒")