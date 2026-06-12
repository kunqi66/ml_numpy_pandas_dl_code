from sql.models import Employee
from sql.database import SessionLocal
from sqlalchemy import text
import asyncio

async def insert_employee(**it):
    session = SessionLocal()
    print('进入函数')
    print('输入函数内',it)
    try:
        emp = Employee(**it)
        session.add(emp)
        session.commit()
        session.refresh(emp)
    except Exception as e:
        print('错误信息',e)
        print("插入员工信息失败")
        session.rollback()
    finally:
        session.close()

async def update_employee(id=0,**emp):
    session = SessionLocal()
    print(emp)
    print(id)
    try:
        em = session.query(Employee).filter(Employee.eid == id).first()
        emp['eid'] = id
        for key, value in emp.items():
            setattr(em, key, value)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()

async def delete_employee_byid(id:int):
    session = SessionLocal()
    try:
        emp = session.query(Employee).filter(Employee.eid == id).first()
        if emp:
            session.delete(emp)
            session.commit()
            print(f"删除{id}成功")
        else:
            print('不存在该员工')
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()

async def select_employee_byid(id):
    session = SessionLocal()
    try:
        result = session.query(Employee).filter(Employee.eid == id).first()
        return result
    except Exception as e:
        print(e)
        print('查无此人')
        session.rollback()
    finally:
        session.close()
    

async def show():
    session = SessionLocal()
    try:
        result = session.execute(text("""
                            SELECT * from t_Employee
                        """)
            ).all()
        print('以下全是结果',result) 
        print(type(result))
        ans = [i._asdict() for i in result]
        return ans
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()



        
