# Coding by 张云路
# 2022/11/21 22:39
import os.path

filename='student.txt'
def Menu():
    print('信息管理系统'.center(40,'='))
    print('信息功能菜单'.center(40,'-'))
    print('1.录入学生信息'.rjust(9,'\t'))
    print('2.查找学生信息'.rjust(9,'\t'))
    print('3.删除学生信息'.rjust(9,'\t'))
    print('4.修改学生信息'.rjust(9,'\t'))
    print('5.排序'.rjust(5,'\t'))
    print('6.统计学生总人数'.rjust(10,'\t'))
    print('7.显示所有学生信息'.rjust(11,'\t'))
    print('0.退出'.rjust(5,'\t'))
    print(''.center(43,'='))

def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001):')
        if not id:
            break
        name=input('请输入姓名:')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入python成绩:'))
            java=int(input('请输入java成绩:'))
        except:
            print('不是整数类型，输入无效，请重新输入')
            continue
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续y/n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    save(student_list)
    print('信息录入完毕')

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def show_list(lst):
    if not lst:
        print('不存在')
    else:
        print('{:^6}\t{:^8}\t{:^11}\t{:^10}\t{:^8}'.format('id', 'name', 'english', 'python', 'java'))
        for item in lst:
            print('{:^6}\t{:^8}\t{:^11}\t{:^10}\t{:^8}'.format(item['id'],item['name'],item['english'],item['python'],item['java']))

def search():
    id=''
    name=''
    student_query=[]
    if os.path.exists(filename):
        mode = input('按id查找请输入1，按name查找请输入2: ')
        if mode == '1':
            id = input('请输入id: ')
        elif mode == '2':
            name = input('请输入姓名: ')
        else:
            print('输入错误，请重新输入')
            search()
            return
    else:
        print('学生信息不存在')
    with open(filename,'r',encoding='utf-8') as rfile:
        student_list=rfile.readlines()
        for item in student_list:
            d=dict(eval(item))
            if id!='':
                if d['id'] == id:
                    student_query.append(d)
            elif name!='':
                if d['name']==name:
                    student_query.apend(d)
    show_list(student_query)
    student_query.clear()
    answer=input('是否继续查询y/n: ')
    if answer=='y' or answer=='Y':
        search()

def delete():
    while True:
        student_id=input('请输入要删除学生的ID:')
        if student_id:
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(item)
                        else:
                            flag=True
            if flag:
                print(f'ID为{student_id}的信息已经被删除')
            else:
                print(f'没有找到ID为{student_id}的学生信息')
        else:
            print('无学生信息')
            break
            show()
        answer=input('是否继续y/n: ')
        if answer=='Y' or answer=='y':
            continue;
        else:
            break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学生ID')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_list:
            d=dict(eval(item))
            if d['id']==student_id:
                print('找到学生信息，可以修改')
                while True:
                    try:
                        d['name']=input('请输入姓名: ')
                        d['english']=input('请输入英语成绩: ')
                        d['python']=input('请输入Python成绩: ')
                        d['java']=input('请输入java成绩: ')
                    except:
                        print('输入错误')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(item)
        answer=input('是否继续修改y/n: ')
        if answer=='y' or answer=='Y':
            modify()

def sort():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_f=rfile.readlines()
        student_list=[]
        for item in student_f:
            d=dict(eval(item))
            student_list.append(d)
    else:
        return
    asc_or_dsc=int(input('请选择（0.升序 1.降序）: '))
    while asc_or_dsc!=0 and asc_or_dsc!=1:
        print('输入数值有误，请重新输入')
        asc_or_dsc=int(input('请选择（0.升序 1.降序）: '))
    mode=input('请输入排序方式（0.按总成绩排序 1.按英语成绩排序 2.按Python成绩排序 3.按java成绩排序）:')
    match mode:
        case '0':
            student_list.sort(key=lambda x: int(x['english'])+int(x['python'])+int(x['java']),reverse=asc_or_dsc)
        case '1':
            student_list.sort(key=lambda x: int(x['english']),reverse=asc_or_dsc)
        case '2':
            student_list.sort(key=lambda x: int(x['python']), reverse=asc_or_dsc)
        case '3':
            student_list.sort(key=lambda x: int(x['java']), reverse=asc_or_dsc)
        case _:
            print('非法字符，请重新输入')
            sort()
    show_list(student_list)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        if student_list:
            print(f'一共有{len(student_list)}名学生')
        else:
            print('还没有保存学生信息')
    else:
        print('还没有保存学生信息')

def show():
    student_show=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        for item in student_list:
            d=dict(eval(item))
            student_show.append(d)
        show_list(student_show)

def main():
    while True:
        Menu()
        choice=int(input('请选择 '))
        if choice in range(8):
            match choice:
                case 0:
                    pass
                case 1:
                    insert()
                case 2:
                    search()
                case 3:
                    delete()
                case 4:
                    modify()
                case 5:
                    sort()
                case 6:
                    total()
                case 7:
                    show()
                case _:
                    print('非法字符')
        else:
            print('选项不存在')
        answer = input('您确定要退出系统吗y/n ')
        if answer == 'y' or answer == 'Y':
            print('谢谢您的使用')
            break
        else:
            continue

main()