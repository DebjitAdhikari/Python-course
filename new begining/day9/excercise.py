student_course={
    "harry":81,
    "ron":78,
    "a":99,
    "b":74,
    "c":62,
}
student_grade={}
for i in student_course:
    grade=""
    if student_course[i]>90:
        grade="outstanding"
    elif student_course[i]>80:
        grade="ex"
    elif student_course[i]>70:
        grade="acc"
    else:
        grade="fail"
    student_grade[i]=grade
print(student_grade)