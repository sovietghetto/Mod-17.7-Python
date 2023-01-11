per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(per_cent)
# dict > list
per_cent_list = list(per_cent.values())
# tkb, skb, vtb, sber
tkb, skb, vtb, sber = per_cent_list[0], per_cent_list[1], per_cent_list[2], per_cent_list[3]
# расчёты
money = float(input("ВВЕДИТЕ СУММУ:"))
tkb_dep = round(money*tkb/100, 2)
skb_dep = round(money*skb/100, 2)
vtb_dep = round(money*vtb/100, 2)
sber_dep = round(money*sber/100, 2)
all_dep = (tkb_dep, skb_dep, vtb_dep, sber_dep)
print('Накопленные средства за год вклада в каждом из банков', all_dep)
# сортировка и отбор
print("Максимальная сумма, которую вы можете заработать —", sorted(all_dep)[3])