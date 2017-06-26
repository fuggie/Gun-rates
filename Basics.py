
# coding: utf-8

# In[6]:


import csv
f= open("guns.csv", 'r')
reader = csv.reader(f)
data = list(reader)
print(data[:5])


# In[7]:


headers = data[0]
data = data[1:]
print(headers)
print(data[:5])


# In[8]:


years = [row[1]for row in data]
year_counts = {}
for year in years:
    if year not in year_counts:
        year_counts[year]= 0
    else:
        year_counts[year] += 1
print(year_counts)


# In[9]:


import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
dates[:5]


# In[18]:


date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    date_counts[date]+= 1
date_counts


# In[15]:


sexes = [row[5] for row in data]
sex_counts = {}
for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 0
    sex_counts[sex] += 1
sex_counts


# In[17]:


races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1
race_counts


# In[19]:


import csv
with open("census.csv", 'r') as f:
    reader = csv.reader(f)
    census = list(reader)
census


# In[24]:


mapping = {
    "White": 197318956,
    "Hispanic":44618105,
    "Black":40250635,
    "Native American/Native Alaskan": 3739506,
    "Asian/Pacific Islander": 15159516 + 674625
}

race_per_hundredk = {}
for k, v in race_counts.items():
    race_per_hundredk[k] = (v/ mapping[k])*100000
    
race_per_hundredk


# In[25]:


intents = [row[3]for row in data]
homicide_race_counts = {}
for i, race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1
race_per_hundredl = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v/mapping[k]) * 100000
race_per_hundredk


# In[ ]:




