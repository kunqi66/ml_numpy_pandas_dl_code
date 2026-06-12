from sql.models import Department
from sql.database import SessionLocal

def insert_department_data():
    # 获取数据库会话
    session = SessionLocal()

    try:
        # =========== 第一步：新增部门 =============
        new_dept = Department(dname="安保部", description="负责公司安保工作")
        session.add(new_dept)  # 将部门对象加入会话
        session.commit()  # 提交到数据库（执行 INSERT 语句）
        session.refresh(new_dept)  # 刷新对象，获取自增的 id 等字段
        # ===================== 输出结果 =====================
        print(f"新增部门：ID={new_dept.did}，名称={new_dept.dname}，描述={new_dept.description}")

    except Exception as e:
        session.rollback()  # 出错时回滚
        print(f"新增失败：{e}")
    finally:
        session.close()  # 关闭会话