import asyncio
import time

async def coro_B():
    """模拟一个耗时操作"""
    print("  [coro_B] 开始")
    await asyncio.sleep(1)   # 模拟 I/O 等待
    print("  [coro_B] 结束")
    return "B的结果"

async def coro_A():
    """调用 coro_B 并等待其完成"""
    print("[coro_A] 调用 await coro_B()")
    result = await coro_B()          # 此处串行等待
    print(f"[coro_A] 收到结果: {result}")
    print("[coro_A] 继续执行后续代码")
    return "A完成"

async def main():
    print("=== 串行等待示例 ===")
    start = time.perf_counter()
    await coro_A()
    elapsed = time.perf_counter() - start
    print(f"总耗时: {elapsed:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(main())