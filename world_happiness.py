#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# # Basic data analysis

# In[2]:


df=pd.read_csv("world-happiness-report.csv")


# In[3]:


df.head(5)


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.year.unique()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.isnull().sum()


# In[10]:


df.duplicated().sum()


# In[11]:


df= df.fillna(df.max())


# In[12]:


df.isnull().sum()


# In[13]:


df2021=pd.read_csv("world-happiness-report-2021.csv")


# In[14]:


df2021.head(5)


# In[15]:


df2021.info()


# In[16]:


df2021.columns


# In[17]:


df2021.shape


# # Count of no of countries per region

# In[18]:


sb.countplot(x="Regional indicator", data=df2021)
plt.xticks(rotation = 80, fontweight="bold")
plt.show()


# # 1 . Happiest country and the factors which they depend on

# In[19]:


def2021_happiest_unhappiest = df2021[(df2021.loc[:, "Ladder score"] > 7.4) | (df2021.loc[:, "Ladder score"] < 3.5)]
sb.barplot( x = "Ladder score", y = "Country name", data=def2021_happiest_unhappiest, palette = "Paired")
plt.title("Happiest and Unhapiest Countries in 2021")
plt.show()


# # Finland is the happiest country and afghanistan is the most unhappiest country in the world 

# In[20]:


plt.figure(figsize=(15,15))  # Set the size of the heatmap
sb.heatmap(df2021.corr(), annot=True, cmap='viridis_r')
plt.title('Heatmap relation diff columns')
plt.show()


# # From the above map we can find the relationship between ladder score and other factors they depend on 
# #1.Completely depend on upperwhisker and lower whisker                                                                             
# #2.Dependability is more on logged gdp,social support,healtht life expectancy and freedom to make life choices
# 
# #3.perception of curruption and residuals holds factor<0.5
# 
# #4.The least applicable factor is the generosity

# # 2.Visualisation related to happiness score and other factors

# In[21]:


a=df2021["Ladder score"]
b=df2021["upperwhisker"]
plt.scatter(a,b)
plt.xlabel("HAppiness score")
plt.ylabel("upperwhisker")
plt.title("Bar Plot")


# #By scatter plot happiness score and upper whisker are completely dependable

# In[22]:


list_features = ["Ladder score", "Logged GDP per capita"]
sb.boxplot(data = df2021.loc[:, list_features], orient = "v", palette = "Set1")
plt.show()


# In[23]:


list_features1 = ["Social support", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]
sb.boxplot(data = df2021.loc[:, list_features1], orient = "v", palette = "Set1") 
plt.show()


# #The above plot indicates the Social support,freedom of life choices and percepption of corruption are the factors on which they depend the most and not on the generosity

# # 3.Top 10 and Bottom 10 countries based on happiness score

# In[24]:


sb.barplot(x = "Ladder score", y = "Country name", data=df2021, palette = "coolwarm")
plt.title("Happiest and Unhappiest Countries in 2021")
plt.show()


# # WE cannot find in this so we can slice the data

# In[25]:


df_sorted = df2021.sort_values(by='Ladder score', ascending=False)


# In[26]:


top_10 = df_sorted.head(10)


# In[27]:


plt.figure(figsize=(10, 6))
plt.bar(top_10['Country name'], top_10['Ladder score'])
plt.xlabel('Country name')
plt.ylabel('Ladder score')
plt.title('Top 10 Maximum Values')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# # .............................................Top 10 happiest countries.

# In[28]:


bot_10 = df_sorted.tail(10)


# In[29]:


plt.figure(figsize=(10, 6))
plt.bar(bot_10['Country name'], bot_10['Ladder score'])
plt.xlabel('Country name')
plt.ylabel('Ladder score')
plt.title('Top 10 Minimum Values')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# # ........................................Bottom 10 happiest countries.

# # 4.Happiest and least happiest countries from above graph is Finland and Afghanisthan respectively

# In[30]:


def2021_happiest_unhappiest = df2021[(df2021.loc[:, "Ladder score"] > 7.4) | (df2021.loc[:, "Ladder score"] < 3.5)]
sb.barplot( x = "Ladder score", y = "Country name", data=def2021_happiest_unhappiest, palette = 'Blues_d')
plt.title("Happiest and Unhapiest Countries in 2021")
plt.show()


# ................................................................................................................................

# # 5.Relationship between happiness and income

# In[31]:


a=df2021["Ladder score"]
b=df2021["Logged GDP per capita"]
plt.plot(a,b)
plt.xlabel("Happiness score")
plt.ylabel("income")
plt.title("line Plot")


# #They are linearly related approximately 70% they both rely on eachother

# # 6.Relationship Between Happiness and Freedom

# In[32]:


a=df2021["Ladder score"]
b=df2021["Freedom to make life choices"]
plt.scatter(a,b)
plt.xlabel("Happiness score")
plt.ylabel(" Freedom to make life choices ")
plt.title("line Plot")


# #The above relationship indicates linear relation of about 60% among them with some major outliers present

# # 7.Relationship Between Happiness and Corruption

# In[33]:


a=df2021["Ladder score"]
b=df2021["Perceptions of corruption"]
plt.plot(a,b)
plt.xlabel("Happiness score")
plt.ylabel("Perceptions of corruption")
plt.title("line Plot")


# #By the above plots we get to know that there is no relationship  among the happiness and corruption ,and ther relation is 0% among them

# # 8.Ladder score distrubution by Regional indicator

# In[34]:


sb.swarmplot(x = "Regional indicator", y = "Ladder score", data = df2021)
plt.xticks(rotation = 90)
plt.title("Ladder score by Regional Indicator in 2021")
plt.show()


# In[35]:


df2=df2021["Ladder score"]
df2
plt.figure(figsize = (15,8))
sb.kdeplot(x=df2,hue = df2021["Regional indicator"],fill=True)
plt.show()


# # Ladder score is more in western europe and least in south asia

# # 9.Ladder score distribution by countries in map view

# In[36]:


import plotly.express as px
fig = px.choropleth(df.sort_values("year"),
                   locations = "Country name",
                   color = "Life Ladder",
                   locationmode = "country names",
                   animation_frame = "year")
fig.update_layout(title="Life ladder comparison by countries")


# # 10. Most Generous and Most Ungenerous Countries in 2021

# In[37]:


df2021_g =df2021[(df2021.loc[:,"Generosity"] > 0.4)]
sb.barplot(x = "Generosity", y = "Country name", data= df2021_g)
plt.title("Most generous and most generois countries in 2021")
plt.show()


# # Indonasia is the most generous country

# In[38]:


df2021_g =df2021[(df2021.loc[:,"Generosity"] < -0.2)]
sb.barplot(x = "Generosity", y = "Country name", data= df2021_g)
plt.title("Most generous and most generois countries in 2021")
plt.show()


# # Greece is least generous

# # 11.Relationship between features

# In[39]:


sb.heatmap(df.corr(), annot = True, fmt = ".2f", linewidth = .7,cmap='viridis_r')
plt.title("Relationship Between Features")
plt.show()


# # 12.Conclusion

# 1.The realtionship among datasets indicates the factors by which the countries happiness can be measured
# 
# 2.Different factors help us to see statistics about the country like the gdp,social factors ,corruptions ,healthy life expectancy and generosity
# 
# 3.Different maps and figures above help us to visualize the relations easily and come to a conclusion among the observed results
# 
# 4.The above dataset is cleaned before visualization and are very helpful to preedict the future happiness using ml models

# In[ ]:




