def is_number_exist(number, array):

    for num in array:
        if num == number:
            return True

    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = False 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))

## 빅오 최악의 경우
## 빅오메가 최선의 경우

"""
만약 3일 경우 첫번째 원소 찾으면 바로 반환함 시간 복잡도가 1밖에 안걸림
만약 4일 경우 운이 좋지 않은 경우 시간 복잡도가 n 만큼 걸린다.

빅오 표기법으로 O(n) 이고, 빅 오메가인경우 오메가(1) 이다.
알고리즘은 거의 빅오 표기법으로 표현한다. 즉 최악의 경우를 대비해서 알고리즘의 성능을 비교하는 것이 올바른 분석이기 때문이다.
"""