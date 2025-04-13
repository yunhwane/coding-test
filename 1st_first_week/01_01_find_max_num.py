def find_max_num(array):
    max_num = array[0]

    for number in array:
        if max_num < number:
            max_num = number
    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

""" 내 첫번째 풀이 
def find_max_num(array):
    max_num = 0;

    for i in array:
        if max_num < i:
            max_num = i
            continue
    return max_num
"""