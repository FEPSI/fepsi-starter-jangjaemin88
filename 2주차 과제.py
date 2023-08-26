1번 문제
T = int(input())
for i in range(1,T+1):
    A,B = map(int,input().split())
print(A+B)

2번 문제
n = int(input())
if 1 <= n <= 10000: 
    total_sum = 0  
    for i in range(1, n + 1):
        total_sum += i
    print(total_sum)  
else:
    print("n의 범위는 1부터 10000까지입니다.")
    
3번 문제
score = int(input())
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")