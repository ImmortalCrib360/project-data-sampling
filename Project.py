import plotly.figure_factory as ff 
import statistics as st 
import random 
import pandas as pd 
import plotly.graph_objects as go
df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
populationMean = st.mean(data)
populationStandardDeviation = st.stdev(data)
print(populationMean)
print(populationStandardDeviation)
graph = ff.create_distplot([data],['reading_time'],show_hist=False)
graph.show()
def randomsetofmean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = st.mean(dataSet)
    return mean 
def showgraph(meanlist):
    data = meanlist
    mean = st.mean(meanlist)
    print(mean)
    graph = ff.create_distplot([data],['average'],show_hist=False)
    graph.add_trace(go.Scatter(x=[mean,mean],y=[0,12],mode='lines',name='Mean'))
    graph.show()
def setup():
    meanlist = []
    for i in range(0,1200):
        setofmeans = randomsetofmean(100)
        meanlist.append(setofmeans)
    stdev = st.stdev(meanlist)
    print(stdev)
    showgraph(meanlist)
setup()

