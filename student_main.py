import student_grades

name=input("name: ")
sid=int(input("student id: "))
Student1=student_grades.Student(name,sid)

while 1:
    choice=int(input("1:add\n2:show info and exit\nyour choice: "))
    if choice==1:
        course_name=input("course name: ")
        score=int(input("score: "))
        Student1.add_score(course_name,score)
    elif choice==2:
        Student1.show_info()
        break