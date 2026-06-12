fo(*args, **kwargs):
    print(args)
    print(kwargs)

nums = (10, 20, 30)
person = {'name':'张三', 'age':18, 'gender':'男'}

show_info(*nums, **person)