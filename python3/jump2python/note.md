출처: https://wikidocs.net/book/1

- [1. 자료형](#section-1)
	- [1-1. 숫자](#section-1-1)
	- [1-2. 문자열](#section-1-2)
	- [1-3. 리스트](#section-1-3)
	- [1-4. 튜플](#section-1-4)
	- [1-5. 딕셔너리](#section-1-5)
	- [1-6. 집합](#section-1-6)
	- [1-7. 불](#section-1-7)
	- [1-8. 변수](#section-1-8)
- [2. 제어문](#section-2)
	- [2-1. if](#section-2-1)
	- [2-2. while](#section-2-2)
	- [2-3. for](#section-2-3)

---
<a id="section-1"></a>
# 1. 자료형
<a id="section-1-1"></a>
## 1-1. 숫자
```python
# 정수형
>>> a = 123
>>> a = -178
>>> a = 0

# 실수형
>>> a = 1.2
>>> a = -3.45

# 8진수
>>> a = 0o177
>>> print(a)
127

# 16진수
>>> a = 0x8ff
>>> b = 0xABC
>>> pring(b)
2748
```

```python
# 사칙연산
>>> a = 3
>>> b = 4
>>> a + b
7
>>> a - b
-1
>>> a * b
12
>>> a / b
0.75

# a의 b 제곱
>>> a = 3
>>> b = 4
>>> a ** b
81

# 나눗셈 후 나머지 반환
>>> 7 % 3
1
>>> 3 % 7
3

# 나눗셈 후 몫 반환
>>> 7 // 4
1
```

```python
# 복합 연산자
# +=, -= *=, /=, //=, %=, **=
>>> a = 1
>>> a = a + 1
>>> print(a)
2

>>> a = 1
>>> a += 1
>>> print(a)
2

>>> a = 1
>>> a -= 1
>>> print(a)
0
```

<a id="section-1-2"></a>
## 1-2. 문자열
```python
# 문자열 출력하기
"Life is too short, You need Python"
"Python's favorite food is perl"
"123"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''
'"Python is very easy." he says.'

>>> multiline="""
... Life is too short
... You need python
"""
>>> print(multiline)
Life is too short
You need python

# 문자열 연결하기
>>> head = "Python"
>>> tail = " is fun!"
>>> head + tail
'Python is fun!'

# 문자열 곱하기
>>> a = "python"
>>> a * 2
'pythonpython'
```

```python

# 문자열 길이 (공백 문자도 포함)
>>> a = "Life is too short"
>>> len(a)
17

# 문자열 인덱싱 (0부터 숫자를 셈)
>>> a = "Life is too short, You need Python"
>>> a[3]
'e'

# 문자열 슬라이싱
>>> a = "Life is too short, You need Python"
>>> a[0:4] # a[시작_번호:끝_번호]
'Life'

# 문자열 시작 번호부터 그 문자열의 끝까지 뽑아냄
>>> a[19:]
'You need Python'

# 문자열 처음부터 끝 번호까지 뽑아냄
>>> a[:17]
'Life is too short'

# 문자열 처음부터 끝까지 뽑아냄
>>> a[:]
'Life is too short, You need Python'

# 문자열 슬라이싱
>>> a = "20230331Rainy"
>>> year = a[:4] # 처음부터 4까지 뽑아냄
>>> day = a[4:8] # 4부터 7까지 뽑아냄
>>> weather = a[8:] # 8부터 끝까지 뽑아냄
>>> year
'2023'
>>> day
'0331'
>>> weather
'Rainy'

# 문자열 슬라이싱 후 변경
>>> a = "Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
>>> a[:1] + 'y' + a[2:]
'Python'
```

```python

# 숫자 바로 대입
>>> "I eat %d apples." % 3
'I eat 3 apples.'

# 문자열 바로 대입
>>> "I eat %s apples." % "five"
'I eat five apples.'

# 숫자 변수 대입
>>> number = 3
>>> "I eat %d apples." % number
'I eat 3 apples.'

# 2개 이상의 값 넣기 ( 콤마 )
>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'

# 문자열 포맷 코드
# %s 문자열 (String)
# %c 문자 1 개 (character)
# %d 정수 (Integer)
# %f 부동소수 (floating‑point)
# %o 8 진수
# %x 16 진수
# %% Literal % (문자 % 자체)

# %s는 어떤 형태의 값이든 변환해 넣을 수 있다.
>>> "I have %s apples" % 3
'I have 3 apples'
>>> "rate is %s" % 3.234
'rate is 3.234'

# 공백과 함께 치환하기
# 오른쪽 정렬하고 나머지 공백
>>> "%10s" % "hi"
'        hi'
# 왼쪽 정렬하고 나머지 공백
>>> "%-10sjane." % 'hi'
'hi        jane.'

#소수점 표현
# 소수점 네 번째 자리까지만
>>> "%0.4f" % 3.42134234
'3.4213'

# 오른쪽 정렬하고 나머지 공백
>>> "%10.4f" % 3.42134234
'    3.4213'

#format: 바로 대입
>>> "I eat {0} apples".format(3)
'I eat 3 apples'

>>> "I eat {0} apples".format("five")
'I eat five apples'

# 정렬
# 왼쪽 정렬
>>> "{0:<10}".format("hi")
'hi      '
# 오른쪽 정렬
>>> "{0:>10}".format("hi")
'        hi'
# 가운데 정렬
>>> "{0:^10}".format("hi")
'    hi    '

# 문자열 함수
# count: 갯수
>>> a = "hobby"
>>> a.count('b')
2

# find: 위치 알려주기 0 부터 셈
>>> a = "Python is the best choice"
>>> a.find('b')
14
# 찾는 문자열이 없을 경우
>>> a.find('k')
-1

# index: 찾는 문자열이 없을 경우 오류를 뱉음
>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found

# join: 문자열 삽입
>>> ",".join('abcd')
'a,b,c,d'

# 대소문자 전환: upper, lower
>>> a = "hi"
>>> a.upper()
'HI'
>>> a = "HI"
>>> a.lower()
'hi'

# 왼쪽 오른쪽 양쪽 공백 지우기: lstrip, rstrip, strip
# 한 칸 이상 연속된 왼쪽 공백 다 지움
>>> a = " hi "
>>> a.lstrip()
'hi '

# 한 칸 이상 연속된 오른쪽 공백 다 지움
>>> a= " hi "
>>> a.rstrip()
' hi'

# 양쪽 한칸 이상 연속된 공백 다 지움
>>> a = " hi "
>>> a.strip()
'hi'

# 문자열 바꾸기: replace
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'

# 문자열 나누기: split
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a','b','c','d']

# 문자열이 알파벳으로만 구성되어 있는지 확인: isalpha
# 공백, 숫자, 특수문자가 포함되어있어도 Fasle 반환
>>> s = "Python"
>>> s.isalpha()
True
>>> s = "Python3"
>>> s.isalpha()
False
>>> s = "Hello World"
>>> s.isalpha()
False

# 문자열이 숫자로만 구성되어 있는지 확인: isdigit
>>> s = "12345"
>>> s.isdigit()
True
>>> s = "1234a"
>>> s.isdigit()
False
>>> s = "12 34"
>>> s.isdigit()
False

# startswith: 문자열이 특정 문자(열)로 시작하는지 확인
>>> s = "Life is too short"
>>> s.startswith("Life")
True
>>> s.startswith("short")
False

# endswith: 문자열이 특정 문자 (열) 로 끝나는지 확인
>>> s = "Life is too short"
>>> s.endswith("short")
True
>>> s.endswith("too")
False

```
<a id="section-1-3"></a>
## 1-3. 리스트
```python
# 리스트 생김새
>>> 리스트명 = [요소1, 요소2, 요소3, ...]
# 비어있는 리스트
>>> a = list()

# 인덱싱
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> a[0] + a[2]
4
# 리스트의 마지막 요소
>>> a[-1]
3

# 리스트안의 리스트
>>> a = [1, 2, 3, ['a', 'b', 'c']]
>>> a[-1]
['a', 'b', 'c']
# 마지막 요솟값 안에 리스트
>>> a[-1][0]
'a'

# 리스트 슬라이싱
>>> a = [1, 2, 3, 4, 5]
>>> a[0:2]
[1, 2]

# 리스트 연산
문자열과 동일함
더하기(+), 반복하기(*)

# len(): 리스트 길이 구하기
>>> a = [1, 2, 3]
>>> len(a)
3

# 리스트 수정 및 삭제
>>> a = [1, 2, 3]
>>> a[2] = 4
>>> a
[1, 2, 4]

# del: 리스트 요소 삭제
>>> a = [1, 2, 3]
>>> del a[1]
>>> a
[1, 3]
# 한꺼번에 삭제
>>> a = [1, 2, 3, 4, 5]
>>> del a[2:]
>>> a
[1, 2]

# 리스트 요소 추가: append
>>> a.append(4)

# 리스트 정렬: sort
>>> a.sort()

# 리스트 그대로 뒤집기: revers
>>> a.reverse()

# 인덱스 반환: index
# 결과가 0 이면 리스트에 존재하지 않기 때문에 오류가 발생함
>>> a.index(3)
0

# 리스트 요소 삽입: insert, 제거: remove
>>> a = [1, 2, 3]
>>> a.insert(0, 4)
>>> a
[4, 1, 2, 3]
# 첫번째로 나오는 x만 삭제
>>> a = [1, 2, 3, 1, 2, 3]
>>> a.remove(3)
>>> a
[1, 2, 1, 2, 3]

# 리스트 맨 마지막 요소 반환 후 삭제: pop()
>>> a = [1, 2, 3]
>>> a.pop()
3
>>> a
[1, 2]

# 리스트에 포함된 요소 x의 갯수 세기: count
>>> a = [1, 2, 3, 1]
>>> a.count(1)
2

# 리스트 확장: extend
# a.extend([4,5]) 는 a+= [4,5]와 동일
>>> a = [1, 2, 3]
>>> a.extend([4, 5])
>>> a
[1, 2, 3, 4, 5]
>>> b = [6, 7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]

# 리스트 복사
# 변수 사용 시 대입을 이용하여 리스트를 복사하면 그 id 값이 완전히 동일하다. 때문에 id를 다르게해서 복사하게 하기 위해선 콜론이나 copy를 사용해야함
# [:]
>>> a = [1, 2, 3]
>>> b = a[:]
>>> a[1] = 4
>>> a
[1, 4, 3]
>>> b
[1, 2, 3]

# copy
>>> from copy import copy
>>> a = [1, 2, 3]
>>> b = copy(a)
```
<a id="section-1-4"></a>
## 1-4.튜플
```python
# 튜플: () 로 둘러싸며 요솟값을 바꿀 수 없음
# 때문에 sort, insert, remove, pop과 같은 내장 함수가 없음

# 1개의 요소만을 가질 때 요소 뒤에 쉼표(,)를 붙여야함
# 소괄호를 생략해도 됨
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플 더하기: 요솟값이 바뀌는 것이 아니라 더해서 새로운 튜플이 생기는 것임
>>> t1 = (1, 2, 'a', 'b')
>>> t2 = (3, 4)
>>> t3 = t1 + t2
>>> t3
(1, 2, 'a', 'b', 3, 4)
```
<a id="section-1-5"></a>
## 1-5.딕셔너리( 연관 배열, 해시 )
```python
# 딕셔너리: key와 value를 한 쌍으로 가지는 자료형
>>> dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# 딕셔너리 쌍 추가: 가장 끝에 그대로 추가됨 key, value가
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}

# 딕셔너리 요소 삭제: del a[key] 입력 시 해당 key value 가 삭제됨
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 사용 예제
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99

# 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 적용할 수 없음
# 주의사항:
## key가 고유한 값이므로 중복되는 key 값을 설정해놓으면 하나를 제외한 나머지 것들이 모두 무시됨
## key에 리스트를 쓸 수 없음
## 튜플은 key 로 쓸 수 있음

# keys: key 리스트 만들기
>>> a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
# 리스트 고유의 append, insert, pop, remove, sort 함수 수행 불가

# dict_keys 객체를 리스트로 변환
>>> list(a.keys())
['name', 'phone', 'birth']

# valus: value 리스트 만들기
>>> a.values()
dict.values(['pay', '010-9999-1234', '1118'])

# items: key value 쌍 튜플로 얻기
>>> a.items()
dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# clear: keys, values 모두 지우기
>>> a.clear()
>>> a
{}

# get: key로 value 얻기
>>> a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'010-9999-1234'
# 정해진 키가 없을 경우 default 값 설정
>>> a.get('nokey', '정보없음')
'정보없음'

# in: 해당 key가 딕셔너리 안에 있는지 조사
>>> a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
>>> 'email' in a
False

# pop: key로 value 얻고 key가 x 인 항목 삭제 후 그 value 반환
>>> a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
>>> phone = a.pop('phone')
>>> phone
'010-9999-1234'
>>> a
{'name': 'pey', 'birth': '1118'}
```
<a id="section-1-6"></a>
## 1-6.집합
```python
# set(): 중복을 허용하지 않고 순서가 없는(인덱싱 불가) 데이터들의 모임, value 만 있음
# 만드는 방법1: 함수로 만들기
>>> s1 = set([1, 2, 3])
>>> s1
{1, 2, 3}

>>> s2 = set("Hello")
>>> s2
{'e', 'H', 'l', 'o'}

# 집합 자료형 만드는 방법2: 리터럴
>>> s3 = {1, 2, 3}
>>> s3
{1, 2, 3}
>>> s4 = {'a', 'b', 'c'}
>>> s4
{'a', 'c', 'b'}

# 인덱싱을 하기 위해선 리스트나 튜플로 변환을 해야함
>>> s1 = set([1, 2, 3])
>>> l1 = list(s1)
>>> l1
[1, 2, 3]
>>> l1[0]
1
>>> t1 = tuple(s1)
>>> t1
(1, 2, 3)
>>> t1[0]
1

# 교집합 & 혹은 intersection(s1), 합집합 | 혹은 union, 차집합 - 혹은 difference
>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])
>>> s1 & s2
{4, 5, 6}
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1 - s2
{1, 2, 3}
>>> s2 - s1
{8, 9, 7}

# add: 값 1개 추가
>>> s1 = set([1, 2, 3])
>>> s1.add(4)
>>> s1
{1, 2, 3, 4}

# update: 값 여러 개 추가
>>> s1 = set([1, 2, 3])
>>> s1.update([4, 5, 6])
>>> s1
{1, 2, 3, 4, 5, 6}

# remove: 특정 값 제거
>>> s1 = set([1, 2, 3])
>>> s1.remove(2)
>>> s1
{1, 3}

# discart: 특정 값 제거이지만 존재하지 않는 값 제거 시 오류 발생
# clear: 모든 값 제거
```
<a id="section-1-7"></a>
## 1-7.불
```python
# 참과 거짓을 나타냄
>>> a = True
>>> b = False

# type: 자료형 확인
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>

# 참 거짓 구분
# 빈 값은 거짓
값 | 참 or 거짓
“python”  참
””        거짓
[1, 2, 3] 참
[]        거짓
(1, 2, 3) 참
()        거짓
{‘a’: 1}  참
{}        거짓
1         참
0         거짓
None      거짓

# and, or, not
# and: 모두 참이면 참
# or: 하나라도 참이면 참
# not: 조건의 참/거짓을 뒤바꿈
>>> x = 5
>>> y = 10
>>> x > 0 and y > 0
True
>>> x > 10 or y > 5
True
>>> not (x > y)
True
```
<a id="section-1-8"></a>
## 1-8.변수
```python
# 올 바 른 변 수 명 예 시
name = " 홍 길 동"
age = 25
user_name = "gildong"
userName = "gildong" # 카 멜 케 이 스
_private = " 비 공 개"
count1 = 10

# 잘 못 된 변 수 명 예 시
# 1name = " 홍 길 동" # 숫 자 로 시 작 ( 오 류 )
# user-name = " 홍 길 동" # 하 이 픈 사 용 ( 오 류 )
# if = 10 # 예 약 어 사 용 ( 오 류 )
# 예약어
False, None, True, and, as, assert, break, class, continue, def,
del, elif, else, except, finally, for, from, global, if, import,
in, is, lambda, nonlocal, not, or, pass, raise, return, try,
while, with, yield
```

---
<a id="section-1"></a>
# 2. 제어문
<a id="section-2-1"></a>
## 2-1. if
```python
# if, else 기본 구조
# 모든 문장에 들여쓰기를 해야한다.
if 조 건 문 :
	수 행 할_문 장 1
	수 행 할_문 장 2
	...
else:
	수 행 할_문 장 A
	수 행 할_문 장 B
	...

# 예시
# 만 약 3000 원 이 상 의 돈 을 가 지 고 있 으 면 택 시 를 타 고 가 고 , 그 렇 지 않 으 면 걸 어 가 라.
money = 2000
if money >= 3000:
	print("택시를 타고 가라")
else:
    print("걸어가라")
걸어가라

# 조건 연산자: and, or, not
# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸아가라.
>>> money = 2000
>>> card = True
if money >= 3000 or card:
	print(" 택 시 를 타 고 가 라")
else:
	print(" 걸 어 가 라")
>>>
택 시 를 타 고 가 라

# in, not in
in           not in
x in 리스트   x not in 리스트
x in 튜플     x not in 튜플
x in 문자열    x not in 문자열

# 1이 리스트에 있는가?
1 in [1, 2, 3]
True

# 1이 리스트에 없는가?
1 not in [1, 2, 3]
False

# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
택시를 타고 가라

# 조건문에서 아무 일도 하지 않게 설정: pass
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어가라")

# elif: 다양한 조건
# 주 머 니 에 돈 이 있 으 면 택 시 를 타 고 가 고 , 주 머 니 에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
	print("택시를 타고 가라")
elif card:
	print("택시를 타고 가라")
else:
	print("걸어가라")
	
택시를 타고 가라

# 좀 더 간략하게 if문 작성
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print("걸어가라")

# 비교 연산자
x = 5
(1 < x) and (x < 10)
True
(10 <= x) and (x <= 20)
False

# 조건부 표현식
score = 85
if score >= 60:
	result = "합격"
else:
	result = "불합격"
print(result)
합격

# 간단하게 표현
# 변수 = 참일 때 값 if 조건 else 거짓일 때 값
score = 85
result = "합격" if score >= 60 else "불합격"
```
<a id="section-2-2"></a>
## 2-2. while
```python

```
<a id="section-2-3"></a>
## 2-3. for
```python
# 기본 구조
for 변수 in 리스트(또는 튜플, 문자열):
	수행할 문장1
	수행할 문장2
	...

# 기본 for문
test_list = ['one', 'two', 'three']
for i in test_list:
	print(i)
one
two
three

# 다양한 for 문의 사용
# 튜플이기 때문에 각각의 요소가 자동으로 변수에 대입이 됨
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
	print(first + last)
3
7
11

# 응용 문제
# 총 5 명 의 학 생 이 시 험 을 보 았 는 데 시 험 점 수 가 60 점 이 상 이 면 합 격 이 고 그 렇 지 않 으 면 불 합 격 이 다. 합 격 인 지 , 불 합 격 인 지 결 과 를 보 여 주 시 오 .
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
	number = number +1
	if  mark >= 60:
		print("%d 번 학 생 은 합 격 입 니 다." % number)
	else:
		print("%d 번 학 생 은 불합격 입 니 다." % number)

# continue: for 문 안의 문장을 수행하는 도중 continue 문을 만나면 for문의 처음으로 돌아감
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
	number = number +1
	if mark < 60:
		continue
	print("%d번 학생 축하합니다.  합격입니다." % number)

# range: 숫자 리스트를 자동으로 만들어줌
# range(10): 0부터 10미만의 수를 포함하는 range 객체를 만들어줌
# 시작과 끝 지정 지 range(시작_숫자, 끝_숫자) 형태를 사용하는데 이때 끝 숫자는 포함되지 않는다.
a = range(10)
a
range(0, 10)

# 예시: 1에서 10까지 더하는 숫자
add = 0
for i in range(1, 11):
	add = add + 1
print(add)
55

# 합격 축하 문장 출력 예제
# len: 리스트 안의 요소 개수 리턴
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
	if marks[number] < 60:
		continue
	print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# 구구단
# end: 다음줄로 넘기지않고 계속 출력
# print('') 그 다음줄로 구분하기
for i in range(2, 10):
	for j in range(1, 10):
		print(i*j, end=" ")
	print('')

# 리스트 컴프리헨션
# append: 리스트 요소 추가
# 전
a = [1,2,3,4]
result = []
for num in a:
	result.append(num*3)
print(result)
[3, 6, 9, 12]

# 후
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)
[3, 6, 9, 12]

# 인덱스 예시
a = [1, 2, 3, 4]
for idx, num in enumerate(a):
	print(idx, num)
0 1
1 2
2 3
3 4

# 짝수만 3으로 곱하기
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num %2 == 0]:
print(result)
[6, 12]

# break
for i in range(10):
	if i == 5:
		break
	print(i)
0
1
2
3
4

#for-else: for문이 정상적으로 종료되었을 때 (break문으로 빠져나가면 else절은 실행안됨)
for i in range(5):
	print(i)
else:
	print("for문이 정상적으로 종료되었습니다.")
0
1
2
3
4
for문이 정상적으로 종료되었습니다.


# enumerate: 리스트 인덱서와 함께 쓸 때, 0부터 시작하는 인덱스 번호를 자동으로 생성해줌
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
	print(f"{i}: {fruit}")
0: apple
1: banana
2: orange

# enumerate 인덱스 시작 번호를 변경하고 싶을 때
for i, fruit in enumerate(fruits, 1)

# zip: 여러 리스트 함께 순회
# f: 포맷팅
names=['홍길동', '김철수', '이영희']
scores=[85, 92, 78]
for name, score in zip(names, scores):
	print(f"{name}: {score}점")
홍길동: 85점
김철수: 92점
이영희: 78점

names = ['홍길동', '김철수', '이영희']
korean = [85, 92, 78]
english = [90, 88, 95]
for name, kor, eng in zip(names, korean, english):
	print(f"{name}: 국어 {kor}점, 영어 {eng}점")
홍길동: 국어 85점, 영어 90점
김철수: 국어 92점, 영어 88점
이영희: 국어 78점, 영어: 95점

```
