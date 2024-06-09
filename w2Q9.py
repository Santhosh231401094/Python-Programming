weapons_count = int(input())
soldiers_count = int(input())

can_win_battle = (weapons_count % 3 == 0) and (soldiers_count % 2 == 0)

print(can_win_battle)
