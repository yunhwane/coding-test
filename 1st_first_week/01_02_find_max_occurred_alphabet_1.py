def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"
                      , "u", "v", "w", "x", "y", "z"]

    max_occurrence = 0
    max_occurred_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0

        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurred_alphabet = alphabet
            max_occurrence = occurrence

    return max_occurred_alphabet


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

"""
tip : chr : 아스키코드값을 문자로 변환
tip : ord : 문자를 아스키코드값으로 변환

#1. a, b, c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야하는 값을 그 알파벳으로 변환한다.
"""