출처: https://wikidocs.net/book/1

- [[#1. 자료형]]
	- [[#1-1. 숫자]]
	- [[#1-2. 문자열]]

---

# 1. 자료형
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
```