#주식 수익 알고리즘 만들기
#며칠에 사서 며칠에 파는게 가장 이익이었을까를 푸는 문제
#우선 단순하게 계산하는 방법을 적용
#원리는 2장의 최대/최소 알고리즘과 같은데, 다만 다루는 항이 두 값의 차로 설정되었으며,
#주식은 먼저 사고 나서 팔기 때문에 j번째 가격-i번째 가격에서 j는 i 이후의 값으로 한정지음
def max_profit_stock_1(a):
    n=len(a)
    max_profit=0
    for i in range(0, n-1):
        for j in range(i+1, n):
            profit=a[j]-a[i]
            if profit>=max_profit:
                max_profit=profit
    return max_profit

stock_price=[10300, 2000, 5000, 6000, 9000, 4000, 10500, 3000]

print(max_profit_stock_1(stock_price))