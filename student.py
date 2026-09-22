def show_student():
    gender = input("请输入学生性别：")
    print(f"学生性别：{gender}")
    name = input("请输入学生姓名：")
    print(f"学生姓名：{name}")
    age = input("请输入学生年龄：")
    print(f"学生年龄：{age}")
    score = float(input("请输入学生成绩："))
    print(f"学生成绩：{score}")

if __name__ == "__main__":
    show_student()
