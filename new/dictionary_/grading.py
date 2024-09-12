student_scores={
    "Harry": 81,
    "Ron": 78,
    "Hermione":99,
    "Draco":74,
    "Nevilee":62,
}
empty_students={}
for i in student_scores:
    if student_scores[i]>90 and student_scores[i]<=100:
        empty_students[i]="Outstanding"
    elif student_scores[i]>80 and student_scores[i]<=90:
        empty_students[i]="Excedds Expections"
    elif student_scores[i]>70 and student_scores[i]<=80:
        empty_students[i]="Acceptable"
    else:
        empty_students[i]="Fail"
for i in empty_students:
    print(i)
    print(empty_students[i])