import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


labels = ['Visibility\nMaterial', 'Functional\nMaterial', 'Menu\nListing', 'Consumption\nActivation', 'Bar\nChecks','Staff\nTraining','Bottles\nat\nBack Bar']
men_means = [20, 34, 30, 35, 30,20,12]
women_means = [25, 32, 34, 20, 25,20,10]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the 

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Budget')
rects2 = ax.bar(x + width/2, women_means, width, label='Execution')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Statistics')
ax.set_title('Scores')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def format_tick(labels):
    def get_label(x, pos):
        try:
            return labels[int(round(x))]
        except IndexError:
            return ''
    return get_label


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
#plt.show()
#plt.gca().xaxis.set_major_formatter(formatter)
plt.savefig('testx.png',bbox_inches='tight',pad_inches=1,orientation="landscape",papertype="legal")