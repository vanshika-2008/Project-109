import random
import csv
import pandas as pds
import plotly.express as px
import plotly.figure_factory as pxfig
import statistics as stats
import plotly.graph_objects as pxgo

df = pds.read_csv('StudentsPerformance.csv')
data = df['reading score'].tolist()


Mean = stats.mean(data)
Median = stats.median(data)
Mode = stats.mode(data)
Sd = stats.stdev(data) 

fsds, fsde = Mean-Sd,Mean+Sd
ssds,ssde = Mean-(2*Sd),Mean+(2*Sd)
tsds,tsde = Mean-(3*Sd),Mean+(3*Sd)

fig = pxfig.create_distplot([data],["Reading Data"],show_hist=False)
fig.add_trace(pxgo.Scatter(x=[Mean,Mean],y=[0,0.17],mode = 'lines',name = 'MEAN'))
fig.add_trace(pxgo.Scatter(x=[fsds,fsds],y=[0,0.17],mode = 'lines',name = 'START OF FIRST STANDARD DEVIATION'))
fig.add_trace(pxgo.Scatter(x=[fsde,fsde],y=[0,0.17],mode = 'lines',name = 'END OF FIRST STANDARD DEVIATION'))
fig.add_trace(pxgo.Scatter(x=[ssds,ssds],y=[0,0.17],mode = 'lines',name = 'START OF SECOND DEVIATION'))
fig.add_trace(pxgo.Scatter(x=[ssde,ssde],y=[0,0.17],mode = 'lines',name = 'END OF SECOND DEVIATION'))
fig.add_trace(pxgo.Scatter(x=[tsds,tsds],y=[0,0.17],mode = 'lines',name = 'START OF THIRD DEVIATION'))
fig.add_trace(pxgo.Scatter(x=[tsde,tsde],y=[0,0.17],mode = 'lines',name = 'END OF THIRD DEVIATION'))
fig.show()
Sd1List = [result for result in data if result>fsds and result <fsde]
Sd2List = [result for result in data if result>ssds and result <ssde]
Sd3List = [result for result in data if result>tsds and result <tsde]
print('Mean of this data is : {}'.format(Mean))
print('Median of this data is : {}'.format(Median))
print('Mode of this data is : {}'.format(Mode))
print('Deviation of this data is : {}'.format(Sd))
print('{}% of data lies within 1st Standard Deviation'.format(len(Sd1List)*100/len(data)))
print('{}% of data lies within 2nd Standard Deviation'.format(len(Sd2List)*100/len(data)))
print('{}% of data lies within 3rd Standard Deviation'.format(len(Sd3List)*100/len(data)))
