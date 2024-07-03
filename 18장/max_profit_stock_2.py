#주식 수익 알고리즘 만들기
#며칠에 사서 며칠에 파는게 가장 이익이었을까를 푸는 문제
#한번씩만 계산하고 싶음... 일단 답지를 보기 전에 풀어본 아이디어는 다음과 같다
#근데 풀어보니까 시간선에 대한 개념을 적용을 안해뒀다. 따라서 써먹을 수 없다. 기록은 해두되, 틀린 풀이이니 유념해두자.
def max_profit_stock_2(a):
    n=len(a)
    max_profit=0
    min_profit=0
    for i in range(0, n):
        profit=a[0]-a[i]
        if profit>=max_profit:
            max_profit=profit
        if profit<=min_profit:
            min_profit=profit
    return max_profit-min_profit

stock_price=[10300, 2000, 5000, 6000, 9000, 4000, 10500, 3000]

print(max_profit_stock_2(stock_price))

#답지의 풀이는 다음과 같다: 최대 수익을 저장해두고, 최저 주가를 또 따로 저장해둔다.
#차례차례 날을 넘기면서 최저가에서 당일가의 차를 계산하고, 당일가가 최저가보다 낮으면 최저가를 갱신한다.
def max_profit_stock_3(a):
    n=len(a)
    max_profit=0
    min_price=a[0]
    for i in range(1,n):
        profit=a[i]-min_price
        if profit<0:
            min_price=a[i]
        if profit>max_profit:
            max_profit=profit
    return max_profit

stock_price=[10300, 2000, 5000, 6000, 9000, 4000, 10500, 3000]

print(max_profit_stock_3(stock_price))