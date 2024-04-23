import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import plotly.express as px
data=pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/unemployment.csv")
#print(data.head())
#Let’s see if this dataset contains missing values or not:
#print(data.isnull().sum())
#While analyzing the missing values, I found that the column names are not correct. So, for a better understanding of this data, I will rename all the columns:

data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]

 #Now let’s visualize the data to analyze the unemployment rate. I will first take a look at the estimated number of employees according to different regions of India:


# data.columns= ["States","Date","Frequency",
#                "Estimated Unemployment Rate","Estimated Employed",
#                "Estimated Labour Participation Rate","Region",
#                "longitude","latitude"]
# plt.title("Indian Unemployment")
# sns.histplot(x="Estimated Employed", hue="Region", data=data)
# plt.show()


#Now let’s see the unemployment rate according to different regions of India:

# plt.figure(figsize=(12, 10))
# plt.title("Indian Unemployment")
# sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
# plt.show()

#Now let’s create a dashboard to analyze the unemployment rate of each Indian state by region. For this, I’ll use a sunburst plot:
unemploment = data[["States", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "States"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")
figure.show()
