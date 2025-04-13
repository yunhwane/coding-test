def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue

        # 아스키코드값을 문자로 변환
        array_index = ord(char) - ord('a')
        alphabet_occurrence_array[array_index] += 1

    max_occurrence = 0
    max_alphabet_occurrence = 0

    for i in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[i]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_occurrence = i

    return chr(max_alphabet_occurrence + ord('a'))

result = find_max_occurred_alphabet

print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))