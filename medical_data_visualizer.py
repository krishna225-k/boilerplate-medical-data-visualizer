import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight']=np.where((df['weight']/np.square(df['height']/100))>25,1,0)
df['cholesterol']=np.where(df['cholesterol']==1,0,1)
df['gluc']=np.where(df['gluc']==1,0,1)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.copy()

    # 6
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    df_cat = df_cat.value_counts().sort_index().reset_index()
    df_cat.columns=['cardio', 'variable', 'value', 'total']
    
    fig=sns.catplot(data=df_cat,x='variable',y='total',kind='bar',aspect=1,hue='value',col='cardio')
    
    fig=fig.figure
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    print(df.columns)
    df_heat=df[
    (df['ap_lo'] <= df['ap_hi'])&
    (df['height'] >= df['height'].quantile(0.025))&
    (df['height'] <= df['height'].quantile(0.975))&
    (df['weight'] >= df['weight'].quantile(0.025))&
    (df['weight'] <= df['weight'].quantile(0.975))
]
    # 12
    print(df_heat.columns)
    # df_heat = df_heat.drop(columns=['bmi'])
    corr = df_heat.corr()
    
    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(corr,
            vmin=0,
            vmax=0.25,
            fmt='.1f',
            linewidths=1,
            mask=mask,
            annot=True,
            square=True,
            cbar_kws={'shrink':.82}
           )

    # 16
    fig.savefig('heatmap.png')
    return fig