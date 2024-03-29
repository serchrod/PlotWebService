
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Plot(object):

    def __init__(self,width=None):
        #title of the chart
        self.title=''
        #labels on Y
        self.labels_y=''
        #Dots Per Inch
        self.dpi=None
        #Labels X
        self.labels_x=[]
        #Legends
        self.legend=[]
        #Value of Group Data
        self.valueGroup1=[]
        self.valueGroup2=[]
        #X value of label locations
        self.x=[]
        #width 
        self.width=width

        #instance plot objects
        self.ax=None
        self.fig=None
        self.filename='Graph.png'

        #Plot Configuration
        self.orientation='landscape'

        #If doesnt have value, insert default value
        if self.width == None:
            self.width=0.35

    def createGroupBarPlot(self):
        self.x = np.arange(len(self.labels_x))  # the label locations
        self.fig, self.ax = plt.subplots()
        rects1 = self.ax.bar(self.x - self.width/2, self.valueGroup1, self.width, label=self.legend[0])
        rects2 = self.ax.bar(self.x + self.width/2, self.valueGroup2, self.width, label=self.legend[1])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        self.ax.set_ylabel(self.labels_y)
        self.ax.set_title(self.title)
        self.ax.set_xticks(self.x)
        self.ax.set_xticklabels(self.labels_x)
        self.ax.legend()
        self.autolabel(rects1)
        self.autolabel(rects2)
        self.fig.tight_layout()
        plt.savefig(self.filename,bbox_inches='tight',pad_inches=1,orientation=self.orientation,papertype="legal",dpi=self.dpi)

    def createPieChart(self):
        self.fig, self.ax = plt.subplots()
        self.ax.pie(self.valueGroup1, labels=self.labels_x, autopct='%1.1f%%',shadow=True, startangle=90)
        self.ax.axis('equal')
        plt.savefig(self.filename,bbox_inches='tight',pad_inches=1,orientation=self.orientation,papertype="legal",dpi=self.dpi)
        

    def autolabel(self,rects):
        for rect in rects:
            height = rect.get_height()
            self.ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
