input = 20

def find_prime_list_under_number(number):

    prime_list = []

    for n in range(2, number + 1):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

# 20이면 2~20까지 n
# n이 18 이면 (18 / 2),(18 / 3),(18 / 4)... 반복하여 찾아낸다
# 수학적 개념: N 의 제곱근보다 크지 않은 어떤 소수로 나누어 떨어지지 않는다.

"""
주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다. 
수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문
"""
result = find_prime_list_under_number(input)
print(result)
