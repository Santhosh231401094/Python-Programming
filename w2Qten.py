N = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())
P4 = int(input())

can_buy_P1 = P1 % N == 0
can_buy_P2 = P2 % N == 0
can_buy_P3 = P3 % N == 0
can_buy_P4 = P4 % N == 0

print(can_buy_P1, can_buy_P2, can_buy_P3, can_buy_P4)
