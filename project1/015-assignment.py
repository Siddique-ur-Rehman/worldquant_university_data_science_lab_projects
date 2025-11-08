#!/usr/bin/env python
# coding: utf-8

# <font size="+3"><strong>1.5. Housing in Brazil 🇧🇷</strong></font>

# In[1]:


# Import Matplotlib, pandas, and plotly
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# **Task 1.5.1** 

# In[2]:


df1 = pd.read_csv("data/brasil-real-estate-1.csv")
df1.head()


# **Task 1.5.2** 

# In[5]:


df1.dropna(inplace=True)
df1.head()


# **Task 1.5.3** 

# In[11]:


df1[["lat", "lon"]] = df1['lat-lon'].str.split(",",expand=True).astype(float)
df1.head()


# **Task 1.5.4** 

# In[12]:


df1["state"] = df1['place_with_parent_names'].str.split("|",expand=True)[2]
df1.head()


# **Task 1.5.5** 

# In[14]:


df1["price_usd"] =df1['price_usd'].str.replace("$","").str.replace(",","").astype(float)
df1.head()


# **Task 1.5.6** 

# In[18]:


df1=df1.drop(columns=['place_with_parent_names','lat-lon'])
df1.head()


# **Task 1.5.7** 

# In[32]:


df2 = pd.read_csv("data/brasil-real-estate-2.csv")
df2.head()


# In[33]:


df2.info()


# **Task 1.5.8** 

# In[34]:


df2["price_usd"] =df2['price_brl']/3.19
df2.head()


# **Task 1.5.9** 

# In[35]:


df2=df2.dropna()
df2=df2.drop(columns=["price_brl"])
df2.head()


# **Task 1.5.10** 

# In[39]:


df = pd.concat([df1,df2])
print("df shape:", df.shape)
df.head()


# ### Explore

# In[44]:


fig = px.scatter_mapbox(
    df2,
    lat="lat", 
    lon="lon", 
    center={"lat": -14.2, "lon": -51.9},  # Map will be centered on Brazil
    width=600,
    height=600,
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

fig.update_layout(mapbox_style="open-street-map")

fig.show()


# **Task 1.5.11** 

# In[48]:


summary_stats = df[['area_m2','price_usd']].describe()
summary_stats


# <div class="alert alert-info" role="alert">
#   <strong>Slight Code Change</strong>
# 
# In the following task, you'll notice a small change in how plots are created compared to what you saw in the lessons.
# While the lessons use the global matplotlib method like <code>plt.plot(...)</code>, in this task, you are expected to use the object-oriented (OOP) API instead.
# This means creating your plots using <code>fig, ax = plt.subplots()</code> and then calling plotting methods on the <code>ax</code> object, such as <code>ax.plot(...)</code>, <code>ax.hist(...)</code>, or <code>ax.scatter(...)</code>.
# 
# If you're using pandas’ or seaborn’s built-in plotting methods (like <code>df.plot()</code> or <code>sns.lineplot()</code>), make sure to pass the <code>ax=ax</code> argument so that the plot is rendered on the correct axes.
# 
# This approach is considered best practice and will be used consistently across all graded tasks that involve matplotlib.
# </div>
# 

# **Task 1.5.12** 

# In[56]:


# Don't change the code below 👇
fig, ax = plt.subplots()

# Build histogram
ax.hist(df['price_usd'].head(20000));

# Label axes
plt.xlabel("Price [USD]")
plt.ylabel("Frequency")
# Add title
plt.title("Distribution of Home Prices");


# **Task 1.5.13** 

# In[58]:


# Don't change the code below 👇
fig, ax = plt.subplots()

#Build box plot
ax.boxplot(df['area_m2'],vert=False)

# Label x-axis
plt.xlabel("Area [sq meters]")
# Add title
plt.title("Distribution of Home Sizes")


# **Task 1.5.14** 

# In[67]:


mean_price_by_region = df.groupby('region')['price_usd'].mean().sort_values()
mean_price_by_region_df = pd.DataFrame(mean_price_by_region)
mean_price_by_region_df


# **Task 1.5.15** 

# In[74]:


# Don't change the code below 👇
fig, ax = plt.subplots()


# Build bar chart, label axes, add title
mean_price_by_region.plot(
    kind="bar",ax=ax,xlabel=("Region"),ylabel="Mean Price [USD]",
    title="Mean Home Price by Region"
     );


# **Task 1.5.16**

# In[ ]:





# In[76]:


df_south = df[df['region']=="South"]
df_south.head()


# **Task 1.5.17** 

# In[95]:


homes_by_state = df_south['state'].value_counts()
homes_by_state


# **Task 1.5.18** 

# In[102]:


# Subset data
df_south_rgs = df[df['state']=="Rio Grande do Sul"]

# Don't change the code below 👇
fig, ax = plt.subplots()


# Build scatter plot
ax.scatter(x=df_south_rgs['area_m2'],y=df_south_rgs['price_usd'])

# Label axes
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")

# Add title
plt.title("Rio Grande do Sul: Price vs. Area")
plt.show()


# **Task 1.5.19** 

# In[117]:


# Alternative approach using groupby
south_states_corr = df[df['state'].isin(['Rio Grande do Sul', 'Santa Catarina', 'Paraná'])].groupby('state').apply(lambda x: x['area_m2'].corr(x['price_usd'])).to_dict()

south_states_corr


# ---
# Copyright 2024 WorldQuant University. This
# content is licensed solely for personal use. Redistribution or
# publication of this material is strictly prohibited.
# 
