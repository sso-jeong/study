# 1. 평균 점수 구하기
avg = (80+75+55)/3
print(avg)

# 2. 홀 짝 판별
num = 13 % 2
if num == 1:
    print('홀수')
else:
    print('짝수')

# 3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin.split("-")[0]
num = pin.split("-")[1]
print(yyyymmdd)
print(num)

# 4. 인덱싱
pin = "881120-1068234"
print(pin[7])

# 5. 바꾸기
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 6. 리스트 역순 정렬
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7. 리스트 문자열로 만들기
a = ['Life ', 'is ', 'too ', 'short']
result = " ".join(a)
print(result)

# 8. 튜플 더하기
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9. 딕셔너리 키
#딕셔너리 키엔 리스트가 올 수 없다.

# 10. 딕셔너리 값 추출
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) # {'A':90, 'C':70} 출 력
print(result) # 80 출 력

# 11. 중복 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b) # [1, 2, 3, 4, 5] 출 력

# 12. 변수
# b의 값은 [1, 4, 3] 가 된다. 대입 시 리스트의 id 값은 변하지 않으므로 a, b 값이 동일함