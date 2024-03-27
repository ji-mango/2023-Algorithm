'''
'1의 개수 세기'
'''


# 24.03.22 다
A, B = map(int, input().split())

# 누적합 구하기
num_sum = [0 for i in range(60)]
for i in range(1, 60):
    num_sum[i] = num_sum[i - 1] * 2 + 2 ** (i - 1)  # 뒤의 비트열이 똑같은 패턴이므로*2 + 1의 개수가 각각 +1
print(num_sum)
def count_binary(num):
    count = 0
    bin_num = bin(num)[2:]                          # bin() : 숫자의 비트열 구하는 함수
    length = len(bin_num)

    print(num, bin_num)
    for i in range(length):
        if bin_num[i] == '1':
            # num보다 크지 않으면서 가장 큰 2의 제곱수
            val = length - i - 1
            count += num_sum[val]
            print(count, val)

            # 가장 앞자리 1개수를 추가로 더해주기
            count += (num - 2 ** val + 1)
            num = num - 2 ** val
            print(count, val)
            print()

    return count

print(count_binary(B) - count_binary(A-1))
