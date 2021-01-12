import matplotlib.pyplot as plt
Days_morning = {"Thứ 2": 18, "Thứ 3": 17, "Thứ 4": 19, "Thứ 5": 22, "Thứ 6": 24, "Thứ 7": 24, "Chủ nhật":23}
Days_night = {"Thứ 2": 15, "Thứ 3": 15, "Thứ 4": 15, "Thứ 5": 15, "Thứ 6": 16, "Thứ 7": 19, "Chủ nhật":20}
Counts = sorted(Days_morning.values(), reverse = True)
Counts = sorted(Days_night.values(), reverse = True)
Days_mornings = sorted(Days_morning, key = Days_morning.__getitem__, reverse = True)
Days_nights = sorted(Days_night, key = Days_night.__getitem__, reverse = True)
ind_Days_mornings = range(len(Days_morning))
ind_Days_nights = range(len(Days_night))
plt.bar(ind_Days_mornings, Counts, align = 'center')
plt.xticks(ind_Days_mornings, Days_mornings)
plt.xlabel("Thứ ")
plt.ylabel("Nhiệt độ ('C)")
plt.title("Nhiệt độ Thừa Thiên Huế tuần 1")
for x, y in zip(ind_Days_mornings, Counts):
    plt.text(x + 0.02, y + 0.05, '%d' % y, ha = 'center', va = 'bottom')
plt.ylim(0, Counts[0] + 20)
plt.show()