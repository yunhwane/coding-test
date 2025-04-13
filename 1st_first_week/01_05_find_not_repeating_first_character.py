input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue

        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []

    for i in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[i]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(i + ord('a')))

    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

""" 내 풀이
alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue

        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    for char in string:
        if not char.isalpha():
            continue

        arr_index = ord(char) - ord('a')
        if alphabet_occurrence_array[arr_index] == 1:
            return char

    return "_"
"""