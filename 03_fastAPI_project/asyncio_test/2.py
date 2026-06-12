import asyncio
import time

async def my_func(name, delay):
    print(f"任务 {name} 开始...")
    await asyncio.sleep(delay)
    print(f"任务 {name} 完成.")
    return f"结果 of {name}"

async def main_concurrent():
    print("--- 并发执行---")
    print("注册任务C")
    asyncio.create_task(my_func("C", 1))
    print("注册任务D")
    asyncio.create_task(my_func("D", 2))

    #必须加这个，否则如果EventLoop发现它的顶级Task(main_concurrent)完成了，它立即触发退出机制。
    #此时EventLoop强制取消所有仍在运行的子Task，然后关闭EventLoop，程序退出。
    await asyncio.sleep(2)#后面换成其他写法


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main_concurrent())
    print(f"并发总耗时: {time.time() - start_time:.2f}秒")

