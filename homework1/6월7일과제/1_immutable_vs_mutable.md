# **Mutable(수정가능) vs Immutable(수정불가능)**

대표적인 mutable 로는 리스트가 있고, immutable로는 문자열이 있습니다.

리스트와 문자열 두 타입 사이에는 큰 차이점이 있습니다. 
바로 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없다는 것입니다. 
**리스트**와 같이 **수정 가능한 자료형**을 **'`mutable`'**한 자료형이라고 부르고, 
**문자열**과 같이 **수정 불가능한 자료형**을 **'`immutable`'**한 자료형이라고 부릅니다. 
숫자, 불린, 문자열은 모두 immutable한 자료형입니다.

```python
# 리스트 데이터 바꾸기
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)
```

```python
[5, 2, 3, 4]
```

리스트 **`numbers`**의 인덱스 **`0`**에 **`5`**를 새롭게 지정해주었습니다. **`[5, 2, 3, 4]`**가 출력되었습니다. 
이처럼 리스트는 데이터의 생성, 삭제, 수정이 가능합니다.

```python
# 문자열 데이터 바꾸기
name = "codeit"
name[0] = "C"
print(name)

```

```python
Traceback (most recent call last):
  File "untitled.py", line 3, in <module>
    name[0] = "C"
TypeError: 'str' object does not support item assignment

```

문자열 **`name`**의 인덱스 **`0`** 에 **`"C"`**를 새롭게 지정해주었더니 오류가 나왔습니다. **`TypeError: 'str' object does not support item assignment`**는 문자열은 변형이 불가능하다는 메시지입니다. 이처럼 문자열은 리스트와 달리 데이터의 생성, 삭제, 수정이 불가능합니다.

Mutable 자료형

- list, dict

Immutable 자료형

- int, float, str, tuple