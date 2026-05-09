# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print("hello world")
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese=chinese
        if math is not None:
            self.math=math
        if english is not None:
            self.english=english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese+self.math+self.english}"

class Management:
    def __init__(self):
        self.student_list = []

    def add_student(self):
        name = input("请输入新增的学生姓名")
        for s in self.student_list:
            if s.name == name:
                return
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            s1 = Student(name,chinese,math,english)
            self.student_list.append(s1)
            print("添加成功")
            return
        else:
            print("成绩不合法")
            return

    def edit_student(self):
        name = input("请输入修改的学生姓名")
        for s in self.student_list:
            if s.name == name:
                chinese = int(input("请输入语文成绩："))
                math = int(input("请输入数学成绩："))
                english = int(input("请输入英语成绩："))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese=chinese,math=math,english=english)
                    print("修改成功")
                    return
                else:
                    print("成绩不合法")
                    return
        print("没有该学生")

    def remove_student(self):
        name = input("请输入删除的学生姓名")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("没有该学生")

    def find_student(self):
        name = input("请输入查询学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(s)
                return
        print("没有该学生")

    def show_student(self):
        for s in self.student_list:
            print(s)

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    mangement1 = Management()
    while True:
        print("欢迎使用系统")
        choice = int(input("请输入操作"))
        match choice:
            case 1:
                mangement1.add_student()
            case 2:
                mangement1.edit_student()
            case 3:
                mangement1.remove_student()
            case 4:
                mangement1.find_student()
            case 5:
                mangement1.show_student()
            case 6:
                print("bye~")
                break
            case _:
                print("非法操作")
