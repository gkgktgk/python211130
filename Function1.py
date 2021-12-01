# Function1.py

# 함수를 정의
def setValue(newValue):
    #함수 내부에서 초기화 하면 지역변수
    x= newValue
    print("함수 내부:", x)


# 함수를 호출
result = setValue(5)
print(result)

# 다중의 값을 리턴
def swap(x,y):
    return y,x

# 호출
result = swap(5,6)
print(result)
print(result[0], result[1])


# 디버깅 연습(교집합 문자를 리턴)
def union(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print(union("HAM", "SPAM"))