el_cnt_1 = int(input("Введите количество элементов в первом списке: "))
lst_1 = list(map(int, input().split()))
el_cnt_2 = int(input("Введите количество элементов во втором списке: "))
lst_2 = list(map(int, input().split()))

ans = []
a, b = 0, 0
while len(ans) < (el_cnt_1+el_cnt_2):
    if a < el_cnt_1 and b < el_cnt_2 and lst_1[a] <= lst_2[b]:
        ans.append(lst_2[b])
        b += 1
    elif a < el_cnt_1 and b < el_cnt_2 and lst_1[a] > lst_2[b]:
        ans.append(lst_1[a])
        a += 1
    else:
        if a >= el_cnt_1:
            ans.extend(lst_2[b:])
        else:
            ans.extend(lst_1[a:])
        break

print(ans)
