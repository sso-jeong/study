marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if  mark >= 60:
        print("%d 번 학 생 은 합 격 입 니 다." % number)
    else:
        print("%d 번 학 생 은 불합격 입 니 다." % number)