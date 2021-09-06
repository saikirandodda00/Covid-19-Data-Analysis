#!/usr/bin/env python
# coding: utf-8

# # Covid-19 Data Analysis
# 
# by : saikiran.dodda

# In[1]:


# Data Preparation
# import all the required libraries


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as ans
import os


# In[3]:


files = os.listdir('C:/Users/sai kiran.dodda/Downloads/Covid-19-20210721T150729Z-001/Covid-19')
files


# In[4]:


# lets create a function so that we cann easily read the csv files 

def read_data(path,filename):
    return pd.read_csv(path+'/'+filename)
    


# In[5]:


path = 'C:/Users/sai kiran.dodda/Downloads/Covid-19-20210721T150729Z-001/Covid-19'
worldometer_data = read_data(path,'worldometer_data.csv')

worldometer_data.head()


# In[6]:


day_wise  = read_data(path,files[2])
day_wise.head()


# In[7]:


usa_country_wise = read_data(path,'usa_country_wise.csv')


# In[8]:


full_grouped = read_data(path,files[3])


# In[9]:


covid_19_clean_complete = read_data(path,'covid_19_clean_complete.csv')


# In[10]:


country_wise_latest = read_data(path,'country_wise_latest.csv')


# In[11]:


covid_19_clean_complete.shape


# In[12]:


# which country has maximum total cases,deaths,active cases and recovered cases..?
# what is the trend of confirmed deaths recovered active cases


# In[13]:


worldometer_data.head()


# In[14]:


worldometer_data.columns


# In[15]:


# now we'll select only the requiresd columns
# we'ill import plotly for tree map

# what exactly is tree map..?

#The treemap was originally designed to visualize a very large amount of data in a  tree-structured diagram 
#      where the size of the rectangles organized from largest to smallest.
#             Color is used to encode a second dimension. Today, they're often used generally for categorical data


# In[16]:


import plotly.express as px


# In[17]:


columns = ['TotalCases','TotalDeaths','TotalRecovered','ActiveCases']

columns


# In[18]:


for i in columns:
    figure = px.treemap(worldometer_data.iloc[0:20],values=i,path =['Country/Region'],title='Tree map of diff countries wrt to their {}'.format(i))
    figure.show()
        


# In[19]:


#   what is the trend of confirmed deaths recovered active cases..?
# we use line plot if we asked anything that related to trend


# In[20]:


day_wise.head()


# In[21]:


day_wise.columns


# In[22]:


figure2 = px.line(day_wise,x='Date',y=['Confirmed', 'Deaths', 'Recovered', 'Active'],title= 'covid cases w.r.t to date',template='plotly_dark')


# In[23]:


figure2.show()


# In[24]:


worldometer_data.head()


# In[25]:


# visualize population to tests done ratio


# In[26]:


pop_test_ratio = worldometer_data['Population']/worldometer_data['TotalTests'].iloc[0:20]
pop_test_ratio


# In[27]:


figure3 = px.bar(worldometer_data.iloc[0:20],x = 'Country/Region' , y = pop_test_ratio.iloc[0:20],color='Country/Region', title='pop to test done ratio')


# In[28]:


figure3.show()


# In[29]:


# which country is badly affected 

worldometer_data.columns


# In[30]:


px.bar(worldometer_data.iloc[0:20],x= 'Country/Region',y=['Serious,Critical','TotalDeaths','TotalRecovered','ActiveCases','TotalCases'])


# In[31]:


# worst 20 countries having max confirmed cases


# In[32]:


figure4 = px.bar(worldometer_data.iloc[0:20],y='Country/Region',x='TotalCases',text='TotalCases',color='TotalCases',title='Top 20 countires of total confirmed cases',template='plotly_dark')


# In[33]:


figure4


# In[34]:


# worst 20 countries having max  deaths


# In[35]:


worldometer_data.sort_values(by='TotalDeaths',ascending=False).head()


# In[36]:



figure5 = px.bar(worldometer_data.sort_values(by='TotalDeaths',ascending=False)[0:20],y='Country/Region',x='TotalDeaths',text='TotalDeaths',color='TotalDeaths',title='Top 20 countires of total deaths',template='plotly_dark')


# In[37]:


figure5


# In[38]:


# worst 20 countries having max active cases


# In[39]:


figure6 = px.bar(worldometer_data.sort_values(by='ActiveCases',ascending=False)[0:20],y='Country/Region',x='ActiveCases',text='TotalDeaths',color='ActiveCases',title='Top 20 countires of active cases ',template='plotly_dark')


# In[40]:


figure6


# In[41]:


# worst 20 countries having max recovered cases


# In[42]:


figure7 = px.bar(worldometer_data.sort_values(by='TotalRecovered',ascending=False)[0:20],y='Country/Region',x='TotalRecovered',text='TotalRecovered',color='TotalRecovered',title='Top 20 countires of  Recovered cases ',template='plotly_dark')
figure7


# In[43]:


# pie chart rep of stats of worst affected countries


# In[44]:


worldometer_data.head(5)


# In[45]:


cases1 = ['TotalCases','TotalDeaths','TotalRecovered','ActiveCases']


labels = worldometer_data[0:15]['Country/Region'].values

for i in cases1:
    fig8 = px.pie(worldometer_data[0:15],values=i,names=labels,hole=0.3,title="{} recorded w.r.t WHO region of 15 worst countires".format(i))
    fig8.show()


# In[46]:


# deaths to confirmed ratio


# In[47]:


worldometer_data.head(5)


# In[48]:


deaths_to_confirmed = worldometer_data['TotalDeaths']/worldometer_data['TotalCases']
deaths_to_confirmed


# In[49]:


fig10 = px.bar(worldometer_data,x='Country/Region',y=deaths_to_confirmed,title='Deaths to confirmed ratio of wrst effected countries')


# In[50]:


fig10


# In[51]:


#deaths to recovered ratio


# In[52]:


deaths_to_recovered = worldometer_data['TotalDeaths']/worldometer_data['TotalRecovered']
deaths_to_recovered


# In[53]:


fig11 = px.bar(worldometer_data,x='Country/Region',y=deaths_to_recovered,title='Deaths to recovered ratio of wrst effected countries')
fig11


# In[54]:


# test to confirmed ratio


# In[55]:


test_to_confirmed = worldometer_data['TotalTests']/worldometer_data['TotalCases']
test_to_confirmed


# In[56]:


fig12= px.bar(worldometer_data,x='Country/Region',y=test_to_confirmed,title='test to cofirmed cases for countries')
fig12


# In[57]:


# serious to death ratio


# In[58]:


serious_to_death = worldometer_data['Serious,Critical']/worldometer_data['TotalDeaths']
serious_to_death


# In[59]:


fig13= px.bar(worldometer_data,x='Country/Region',y=serious_to_death,title='serious to death rationin countires')
fig13


# In[60]:


# we ill now automate our analysis by using a function for getting our analysis for a particular country


# In[ ]:





# In[61]:


worldometer_data.head(5)


# In[62]:


# well access our grouped data sett


# In[63]:


full_grouped.head()


# In[64]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[69]:


def country_visualization(group_data,country):
    
    data=full_grouped[full_grouped['Country/Region']==country]
    df=data.loc[:,['Date','Confirmed','Deaths','Recovered','Active']]
    fig = make_subplots(rows=1, cols=4,subplot_titles=("Confirmed", "Active", "Recovered",'Deaths'))
    fig.add_trace(
        go.Scatter(name="Confirmed",x=df['Date'],y=df['Confirmed']),row=1, col=1
    )

    fig.add_trace(
        go.Scatter(name="Active",x=df['Date'],y=df['Active']),row=1, col=2
    )
    fig.add_trace(
        go.Scatter(name="Recovered",x=df['Date'],y=df['Recovered']),row=1, col=3
    )

    fig.add_trace(
        go.Scatter(name="Deaths",x=df['Date'],y=df['Deaths']),row=1, col=4
    )

    fig.update_layout(height=600, width=1000, title_text="Date Vs Recorded Cases of {}".format(country),template="plotly_dark")
    fig.show()


# In[70]:


country_visualization(full_grouped,'Angola')


# In[71]:


country_visualization(full_grouped,'US')


# In[ ]:




