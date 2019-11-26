import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/president_heights.csv')
heights = np.array(data['height(cm)'])
print (heights)

#exploratory statistics

print ("Mean height is {}".format(heights.mean()))
print ("Std of height is {}".format(heights.std()))
print ("Min height is {}".format(heights.min()))
print ("Max height is {}".format(heights.max()))
print ("Median of height is {}".format(np.median(heights)))
print ("25th percentile of height is {}".format(np.percentile(heights,25)))
print ("75th percentile of height is {}".format(np.percentile(heights,75)))

#plotting

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show(block=True) #to show figure in terminal
