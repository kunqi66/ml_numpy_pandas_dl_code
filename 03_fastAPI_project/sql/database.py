from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/testbase"

# 创建引擎（echo=True 会打印执行的 SQL，方便调试）
engine = create_engine(
    DATABASE_URL,
    echo=True,  # 是否启用日志输出 开发环境启用，生产环境关闭
    pool_pre_ping=True  # 连接前检查有效性，避免连接失效
)

SessionLocal = sessionmaker(
    autocommit=False,  # 关闭自动提交，需手动 commit()
    bind=engine
)

