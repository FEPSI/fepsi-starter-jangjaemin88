# 1번 문제
fv = 1000000    # fv = future value
r = 0.1    # r = reate of return
n = 10    # n = number of periods
pv = fv / (1 + r)**n    # pv = present value
print(pv)

# 2번 문제
zero_cash_flow = -10000
first_cash_flow = 3000 / (1.05)
second_cash_flow = 2000 / (1.05)**2
third_cash_flow = 4000 / (1.05)**3
fourth_cash_flow = 5000 / (1.05)**4
print(zero_cash_flow + first_cash_flow + second_cash_flow + third_cash_flow + fourth_cash_flow)

# 3번 문제
rp = 10    # rp = 포토폴리오 수익
rf = 3    # rf = 무위험 이자율
sigma_p = 4    # sigma_p = 포토폴리오의 변동성
sharpe_ratio = (rp - rf) / sigma_p 
print(sharpe_ratio)

# 주피터 노트북으로 돌렸을때는 다 결과가 나왔는데 여기서는 왜 안될까요....