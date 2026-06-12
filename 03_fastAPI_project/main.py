from fastapi import FastAPI
import uvicorn
from routers import user
from sql.models import Base
from sql.database import engine
import ast

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)

@app.get("/")
async def hello():
    return {"message": "访问本网址/docs调试"}

@app.post("/say_hi")
def say_hi(kwargs):
    print(kwargs)
    print(type(kwargs))
    ans = ast.literal_eval(kwargs)
    print(ans)
    print(type(ans))
    name = ans['name']
    print(name,ans['age'])
    a = 'hello'
    return {'message':f"{a}+world",
            'par':f'接收到的参数有{kwargs}'}
    

if __name__ == '__main__':
    # 直接在代码中启动uvicorn服务器
    uvicorn.run(
        app="main:app",       # 指定要运行的FastAPI应用实例
        host="0.0.0.0",  # 允许外部访问（本地可通过127.0.0.1或localhost访问）
        port=8000,     # 端口号
        reload=True    # 开发模式：代码修改后自动重启（生产环境需去掉）
)


