import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bokeh

data = pd.read_csv('Fin.csv', index_col=None)
# Loading the csv file

data.info()


# Plotting relationship between height and weight

# Importing the Bokeh package 

from bokeh.io import output_notebook, show
from bokeh.plotting import figure
output_notebook()


output_notebook()
# Creating a scatter plot
p = figure(plot_width=1000, plot_height=400)
p.circle(y='weight', x='height', source=data, size=6, line_color="navy", fill_color="orange", fill_alpha=0.5)
# show the results
show(p) 


data.head()


# Summary stats for height and weight for each gender

# Creating a function to getting the required output
​
def printtable(dat):
    a = min(dat)
    b = np.percentile(dat, 25)
    c = dat.median()
    d = dat.mean()
    e = np.percentile(dat, 75)
    f = max(dat)
​
    print('-'*110)
    print('| Minimum\t|\tQuartile_1st\t|\tMedian\t|\tMean\t|\tQuartile_3rd\t|     Maximum |')
    print('-'*110)
    if (a>=100):
      print('| %.2f\t|\t%.2f\t\t|\t%.2f\t|\t%.2f\t|\t%.2f\t\t|\t%.2f|' % (a,b,c,d,e,f))
    else:
      print('| %.2f\t\t|\t%.2f\t\t|\t%.2f\t|\t%.2f\t|\t%.2f\t\t|\t%.2f|' % (a,b,c,d,e,f))
    print('-'*110)
​
# Printing the stats for Male Heights
​
print("Stats - Height_Male")
printtable(data.height[data['gender']=='Male'])


# Printing the stats for Female Heights

print("Stats - Height_Female")
printtable(data.height[data['gender']=='Female'])


# Printing the stats for Male Weights

print("Stats - Weight_Male")
printtable(data.weight[data['gender']=='Male'])


# Printing the stats for Female Weights

print("Stats - Weight_Female")
printtable(data.weight[data['gender']=='Female'])


# Plotting the Histogram for the Height - Male
import seaborn as sns; sns.set(color_codes=True)

sns.set_style('ticks', {"axes.facecolor": "1",'axes.grid' : True})
plt.hist(data.height[data['gender']=='Male'],bins=30,rwidth=0.9, color='g')
plt.title('Gender - Male')
plt.xlabel('Height in Cms')
plt.ylabel('Weight in Kgs')
plt.show()




sns.set_style('ticks', {"axes.facecolor": "1",'axes.grid' : True})
plt.hist(data.height[data['gender']=='Female'],bins=30,rwidth=0.9, color='g')
plt.title('Gender - Female')
plt.xlabel('Height in Cms')
plt.ylabel('Weight in Kgs')
plt.show()




# creating separate dataframes for gender

dataM = data[data['gender']=='Male']
dataF = data[data['gender']=='Female']

ax1 = dataM.plot(kind='scatter', x='height', y='weight', color='r',figsize=(12,5), label='Male')    
ax2 = dataF.plot(kind='scatter', x='height', y='weight', color='b',figsize=(12,5), ax=ax1, label='Female')    

plt.title('Scatter Plot')
plt.xlabel('Height in Cms')
plt.ylabel('Weight in Kgs')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()





sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(12,5)

labels=['Male','Female']
sns.regplot(x='height', y='weight', data=dataM, ax=ax, label = 'Male')
sns.regplot(x='height', y='weight', data=dataF, ax=ax, label= 'Female')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
sns.despine()
plt.title('Scatter Plot with Best-Fit lines (Regression Line)')
plt.show()





import statsmodels.api as sm

fig, (ax, ax2) = plt.subplots(ncols=2)
fig.set_size_inches(16,9)
ax.set_title('Male - Height')
sm.qqplot(dataM.height, ax=ax, line='s')
ax2.set_title('Female - Height')
sm.qqplot(dataF.height, ax=ax2, line='s')
plt.show()





fig, (ax, ax2) = plt.subplots(ncols=2)
fig.set_size_inches(16,9)
ax.set_title('Male - Weight')
sm.qqplot(dataM.weight, ax=ax, line='s')
ax2.set_title('Female - Weight')
sm.qqplot(dataF.weight, ax=ax2, line='s')
plt.show()