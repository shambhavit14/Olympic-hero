# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'},inplace = True)
data.head(10)

#Code starts here



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both' , (np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')))

better_event = data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here
z = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = z[0:-1]


def top_ten(dff, colm):
    num = 0
    country_list =  []
    a = top_countries.nlargest(10,colm)
    for i in range(len(a['Country_Name'])):
        b = a['Country_Name'].iloc[num]
        country_list.append(b)
        num +=1
    return country_list
top_10_summer = top_ten(top_countries , 'Total_Summer')
top_10_winter = top_ten(top_countries , 'Total_Winter')
top_10 = top_ten(top_countries , 'Total_Medals')
common = ['United States', 'Sweden', 'Germany', 'Soviet Union']




# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.plot.bar('Country_Name','Total_Summer')
winter_df.plot.bar('Country_Name','Total_Summer')
top_df.plot.bar('Country_Name','Total_Summer')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/ summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio'] == summer_max_ratio]['Country_Name'].iloc[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/ winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio'] == winter_max_ratio]['Country_Name'].iloc[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/ top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio'] == top_max_ratio]['Country_Name'].iloc[0]



# --------------
#Code starts here
data_1 = data[0:-1]
data_1['Total_Points'] = data['Gold_Total']*3 + data['Silver_Total']*2 + data['Bronze_Total'] 

most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points'] == most_points]['Country_Name'].iloc[0]



# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals')
plt.xticks(rotation = 45)


