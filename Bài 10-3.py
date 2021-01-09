# Colume chart
import matplotlib.pyplot as plt
Food = {'Cá': 10, 'Thịt': 20, 'Trứng': 50, 'Sữa': 30, 'Cua': 40}
Counts = sorted(Food.values(), reverse=True)
Foods = sorted(Food, key=Food.__getitem__, reverse=True)
ind_Foods= range(len(Food))
plt.bar(ind_Foods, Counts, align='center')
plt.xticks(ind_Foods, Foods)
plt.xlabel('Tên')
plt.ylabel('DINH DƯỠNG (KCAL)')
plt.title('THỨC ĂN')
for x, y in zip(ind_Foods, Counts):
    plt.text(x+0.02, y+0.05, '%d' % y, ha='center', va= 'bottom')
plt.ylim(0, Counts[0] + 20)
plt.show()
