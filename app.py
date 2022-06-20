#^ to write/rewrite app.py everytime this cell runs

#importing libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#opening saved model
with open('saved_model.pkl','rb') as file:
  data = pickle.load(file)

model = data['model']
job_label = data['job_label']
province_label = data['province_label']
years = data['years']
pol_reg = data['pol_reg']
sc = data['sc']
df = data['df']

st.title('Salary Prediction in Indonesia')
st.write('''### Please input some information as follow:''')

job_list = ['Factory and Manufacturer',
            'Sales',
            'Internet & New Media',
            'Accounting, Finance, Banking',
            'Art & Design',
            'Business',
            'Hospitality & Travel',
            'Administration',
            'Marketing',
            'Human Resources & General Affair',
            'Data Analyst & Data Science',
            'Research & Development'
            'Public Relation']
job = st.selectbox('Job Type',job_list)

province_list = ['Jakarta','Jawa','Sumatera','Kalimantan','Sulawesi','Bali dan Nusa Tenggara','Other']
province = st.selectbox('Province',province_list)

experience = st.slider('Years of experience', 0, 20, 2)

start = st.button('Calculate Salary')

if start:
  X = pd.DataFrame([[job,experience,province]])
  X[0][0] = job_label.transform(np.array(X[0][0]).reshape(-1,1))
  X[2][0] = province_label.transform(np.array(X[2][0]).reshape(-1,1))
  X.astype(float)
  salary = sc.inverse_transform(model.predict(X).reshape(-1,1))
  st.subheader(f'The estimated salary is IDR{salary[0][0]:.0f}')

  df_new = df.loc[(df['Job'] == job)]

  st.write('\n')
  st.write('''\n See the scatter of your job per province:''') #i use DataCleaned for province records
  
  with open('saved_map.pkl','rb') as file:
    data = pickle.load(file)
  
  df_prov = data['prov']
  df_geo = data['geo']

  df = df_prov[df_prov['Job']==job]
  df1 = df['Propinsi'].value_counts().rename_axis('Propinsi').reset_index(name='counts')
  df2 = pd.merge(df_geo[['Propinsi','geometry']], df1, on ='Propinsi', how ='left')
  df2 = df2.replace(np.nan,0)

  fig = plt.figure(figsize=(10, 6))
  ax = fig.add_subplot()
  df2.plot(column='counts', ax=ax, legend=True, legend_kwds={'label': "Number of Job Vacancy in the Province", 'orientation': "horizontal"})
  st.pyplot(fig) 
  st.write('\n')

  st.write('''\n Mean salary per province and the comparison with regional minimum wage (UMR):''')
  
  fgr = plt.figure(figsize=(10, 6))
  ax = fgr.add_subplot()   
  
  colors = ['#ff9f1c','#ffbf69','#f2cc8f','#98c1d9','#2ec4b6','#43aa8b','#a3b18a']
  
  dict_UMR = {'Bali dan Nusa Tenggara': [2209294,'2,209,294'],'Jakarta':[4416186,'4.416.186'],'Jawa': [1940821, '1.940.821'] ,'Kalimantan': [2832495,'2,832,495'],
            'Other': [2994448,'2,994,448'], 'Sulawesi': [2748425,'2,748,425'],'Sumatera': [2747452,'2.747.452']}
  x_label = list(dict_UMR.keys())
  
  for x in x_label:
    if x not in df_new['Province'].unique():
      x_label.remove(x)
  
  ax.bar(x_label, df_new.groupby(['Province'])['Salary'].mean(), color = colors[0:len(x_label)])
  
  UMR_list = []
  UMR_label = []
  for x in x_label:
    UMR_list.append(dict_UMR[x][0])
    UMR_label.append(dict_UMR[x][1])
  
  ax.plot(x_label, UMR_list, label = 'Rata-rata UMR 2021', color = 'k', linewidth = 3)
  for i in range(len(x_label)):
    plt.text(x=i,y=UMR_list[i]+1100000, s=str(UMR_label[i]), size=12, ha='center', va='center')
  
  plt.ylabel('Mean Salary in 10 million IDR', fontsize = 14)
  ax.tick_params(axis='x', labelrotation=45, labelsize=14)
  ax.tick_params(axis='y', labelsize=14)
  ax.set_title('Mean Salary per Province in Indonesia', fontsize=15, fontweight='bold')
  plt.legend()
  
  st.pyplot(fgr) 
  st.write('\n')

  st.write('''Mean salary based on years of experience:''')
  
  figure = plt.figure(figsize=(10, 6))
  ax = figure.add_subplot()
  
  years_list = [0, 0.5, 2, 4, 7.5, 15]
  
  ax.plot(years_list,df_new.groupby(['Years'])['Salary'].mean())
  plt.ylabel('Mean Salary in 10 million IDR', fontsize = 14)
  plt.xlabel('Years of experience', fontsize = 14)
  ax.tick_params(axis='x', labelsize=14)
  ax.tick_params(axis='y', labelsize=14)
  ax.set_title('Mean Salary per Years of Experience', fontsize=15, fontweight='bold')
  
  st.pyplot(figure)
  st.write('\n')