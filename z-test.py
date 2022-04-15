import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math score"], show_hist=False)
#fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print(mean, stdev)

def sampling() :
    dataSet = []
    for i in range(0, 100) :
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)

    sampleMean = statistics.mean(dataSet)
    return sampleMean

meanList = []
for i in range(0, 1000) :
    samplingMean = sampling()
    meanList.append(samplingMean)

meanOfSamples = statistics.mean(meanList)
sampleStdev = statistics.stdev(meanList)
print(meanOfSamples, sampleStdev)

stdev_1_start = meanOfSamples-sampleStdev
stdev_1_end = meanOfSamples+sampleStdev
stdev_2_start = meanOfSamples-(2*sampleStdev)
stdev_2_end = meanOfSamples+(2*sampleStdev)
stdev_3_start = meanOfSamples-(3*sampleStdev)
stdev_3_end = meanOfSamples+(3*sampleStdev)

fig = ff.create_distplot([meanList], ["Sampling"], show_hist=False)
fig.add_trace(go.Scatter(x = [meanOfSamples, meanOfSamples], y = [0, 0.2], mode = "lines", name = "Sample Mean"))
fig.add_trace(go.Scatter(x = [stdev_1_start, stdev_1_start], y = [0, 0.2], mode = "lines", name = "Standard deviation 1st start"))
fig.add_trace(go.Scatter(x = [stdev_1_end, stdev_1_end], y = [0, 0.2], mode = "lines", name = "Standard deviation 1st end"))
fig.add_trace(go.Scatter(x = [stdev_2_start, stdev_2_start], y = [0, 0.2], mode = "lines", name = "Standard deviation 2nd start"))
fig.add_trace(go.Scatter(x = [stdev_2_end, stdev_2_end], y = [0, 0.2], mode = "lines", name = "Standard deviation 2nd end"))
fig.add_trace(go.Scatter(x = [stdev_3_start, stdev_3_start], y = [0, 0.2], mode = "lines", name = "Standard deviation 3rd start"))
fig.add_trace(go.Scatter(x = [stdev_3_end, stdev_3_end], y = [0, 0.2], mode = "lines", name = "Standard deviation 3rd end"))
#fig.show()

df1 = pd.read_csv("data1.csv")
data1 = df1["Math_score"].tolist()
mean1 = statistics.mean(data1)
print(mean1)
z1 = (mean1-meanOfSamples)/sampleStdev
fig.add_trace(go.Scatter(x = [mean1, mean1], y = [0, 0.2], mode = "lines", name = "Mean of group 1"))

df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()
mean2 = statistics.mean(data2)
print(mean2)
z2 = (mean2-meanOfSamples)/sampleStdev
fig.add_trace(go.Scatter(x = [mean2, mean2], y = [0, 0.2], mode = "lines", name = "Mean of group 2"))

df3 = pd.read_csv("data3.csv")
data3 = df3["Math_score"].tolist()
mean3 = statistics.mean(data3)
print(mean3)
z3 = (mean3-meanOfSamples)/sampleStdev
fig.add_trace(go.Scatter(x = [mean3, mean3], y = [0, 0.2], mode = "lines", name = "Mean of group 3"))

print(z1, z2, z3)

#fig.show()
