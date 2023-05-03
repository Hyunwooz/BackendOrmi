## for문을 이용한 피보나치 수열 구하기

```python

curr = 1
_next = 1

for i in range(1,6):
    curr , _next = _next , curr + _next

결과값 : 13

# 구할 수 없음.

for i in range(1,6):
  _next = curr + _next
  curr = _next

결과값 : 32



```
