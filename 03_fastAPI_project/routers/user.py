from fastapi import APIRouter
from pydantic import BaseModel
from sql.department import insert_department_data
import sql.employee as employee
import datetime

class item(BaseModel):
    ename:str = None
    gender:str = '男'
    birthday:datetime.date = None
    salary:float = None
    commission_pct:float = None
    tel:str = None
    email:str = None
    address:str = None
    work_place:str = None
    hiredate:datetime.date = None
    
router = APIRouter(
    prefix="/users",
    tags=["user"]
)

# 晚自习完成员工表的增删查改自己办法和老师办法

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"获取 ID 为 {user_id} 的用户信息"}

@router.post("/input_message")
async def input_message(it:item):
    print(it)
    print(type(it))
    try:
        result = await employee.insert_employee(**dict(it))
        print(result)
    except Exception as e:
        print(e)
        print('信息输入失败')
        return 'fail'
    print('信息输入成功')
    return '信息输入完毕'

@router.post("/delete_emp")
async def deletr_emp(id:int):
    try:
        await employee.delete_employee_byid(id)
    except Exception as e:
        print(e)
        return '删除失败'
    return '删除成功'

@router.post("/show_user")
async def show_user():
    try:
        ans = await employee.show()
        return ans
    except Exception as e:
        print(e)
        print('查询失败')
        
@router.post("/select_user")
async def select_user(id):
    try:
        ans = await employee.select_employee_byid(id)
        return ans
    except Exception as e:
        print(e)
    return None

@router.post("/update_user")
async def updateuser(emp:item,id):
    try:
        await employee.update_employee(**dict(emp),id=id)
        return "成功"
    except Exception as e:
        print(e)
        return "失败"
