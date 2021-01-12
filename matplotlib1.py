import matplotlib.pyplot as plt
Day = {"Thứ 2": 50, "Thứ 3": 70, "Thứ 4": 100, "Thứ 5": 50, "Thứ 6": 120, "Thứ 7": 170, "Chủ nhật":20}
Counts = sorted(Days.values(), reverse = True)
Counts = sorted(Days_night.values(), reverse = True)
Days = sorted(Days_morning, key = Days_morning.__getitem__, reverse = True)
ind_Days = range(len(Day))

plt.bar(ind_Days_mornings, Counts, align = 'center')
plt.xticks(ind_Days_mornings, Days_mornings)
plt.xlabel("Thứ ")
plt.ylabel("Lượng mưa (ml)")
plt.title("Lượng mưa Thừa Thiên Huế tuần 1")
for x, y in zip(ind_Days_mornings, Counts):
    plt.text(x + 0.02, y + 0.05, '%d' % y, ha = 'center', va = 'bottom')
plt.ylim(0, Counts[0] + 20)
plt.show()