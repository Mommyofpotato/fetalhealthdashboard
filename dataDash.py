#!/usr/bin/env python
# coding: utf-8

# #### from jupyter_dash import JupyterDash
# from dash import html, dcc, Input, Output
# import pandas as pd
# import plotly.express as px

# In[1]:


from dash import Dash, dcc, html,dash_table,Input,Output


# In[2]:


import plotly.express as px
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output
import pandas as pd
from sklearn.datasets import load_breast_cancer


# In[3]:


df = pd.read_csv('fetal_health.csv')
print(df)


# In[4]:


app=JupyterDash()


# In[5]:


fetal_num=df['fetal_health'].unique()
print(fetal_num)


# In[6]:


app.layout = html.Div([
    html.H1('Fetal Health Scores'),
    html.P(['This dashboard displays fetal health based on various laboring factors with results of fetal health score of 1-3',
           html.Br()]),dcc.Checklist(id='checklist',options=df['fetal_health'].unique()),dcc.Graph(id='fetal-scatter'),html.Div(id='average-div')])


# In[7]:


@app.callback(
Output('fetal-scatter','figure'),
Input('checklist','value'))
def update_graph(selected_value):
    filtered_health=df[df['fetal_health'].isin(selected_value)]
    scatter_fig=px.scatter(data_frame=filtered_health,x='abnormal_short_term_variability',y='baseline value',title=f'Fetal Health Score {selected_value}')
    return scatter_fig


# In[8]:


if __name__=='__main__':
    app.run_server(mode="external")


# In[ ]:




