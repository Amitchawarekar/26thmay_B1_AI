#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import warnings
import tkinter as tk

warnings.filterwarnings('ignore')


# In[105]:


cols = 'user_id item_id rating timestamp'.split()
df = pd.read_csv('u.data',sep='\t',names=cols)
cols_movies = ['item_id', 'title']+[str(i) for i in range(22)]
movie_titles = pd.read_csv('u.item',sep='|',names=cols_movies,encoding='latin-1')
movie_titles = movie_titles[['item_id','title']]
data = pd.merge(df,movie_titles, on='item_id')
rating = pd.DataFrame(data.groupby('title')['rating'].mean())
rating['count'] = data['title'].value_counts()
pivot_df = data.pivot_table(index = 'user_id', columns = 'title', values = 'rating')

app=tk.Tk()
app.title('Recommender System')
app.geometry('500x300')
app.config(bg='white')

title =tk.Label(app, text="Movie Recommender System", font=("goudy old style", 15, "bold"), bg="#033054",
                      fg="white").place(x=0, y=0, width=500, height=25)
f= tk.Frame(app,width=460,height=250,bd=5,bg='white',relief="ridge").place(x=20,y=30)
tk.Label(f,text='Movie You Watched:',font=("quiche sans", 12, "bold"),bg='white',fg='blue').place(x=40,y=50)
tk.Label(f,text='Recommended:',font=("quiche sans", 12, "bold"),bg='white',fg='blue').place(x=40,y=170)
tk.Label(f,text='Also try:',font=("quiche sans", 12, "bold"),bg='white',fg='blue').place(x=40,y=220)

movie_var= tk.Variable(app)
tk.Entry(f,textvariable=movie_var,bg='light yellow',font=('arial',10)).place(x=220,y=50,width=220,height=22)

recommend_var =tk.Variable(app)
recommend_var.set('Type movie name.....')
tk.Label(app,textvariable=recommend_var,bg='white',font=('arial',12)).place(x=220,y=170)

also_try_var= tk.Variable(app)
also_try_var.set('Type movie name.....')
tk.Label(app,textvariable=also_try_var,bg='white',font=('arial',12)).place(x=220,y=220)


def find_recommendation():
    movie=movie_var.get().lower().strip() 
    if movie:
        try:
            movie=movie_titles['title'][ movie_titles['title'].apply(lambda x : movie in x.lower())].values[0]
            movie_var.set(movie)
        except IndexError:
            recommend_var.set('Movie not found')
            also_try_var.set('Movie not found')
        else:
            corr_df = pd.DataFrame(pivot_df.corrwith(pivot_df[movie]),columns = ['Correlation'])
            corr_df.dropna(inplace=True)
            corr_df = corr_df.join(rating['count'])
            recommend_var.set(corr_df[(corr_df['count']>200) & (corr_df['Correlation']>0.4)].sort_values(by='Correlation',ascending=False).index[1])
            also_try_var.set(corr_df[corr_df['Correlation']>0.4].sort_values(by='Correlation',ascending=False).index[0])
    
def clear():
    movie_var.set("")
    recommend_var.set("Type movie name.....")
    also_try_var.set("Type movie name.....")
    
tk.Button(f,text='Suggestion',command=find_recommendation,font=('arial',12,'bold'),bg='#f44336',fg='white').place(x=220,y=100,width=100,height=30)

tk.Button(f,text='Clear',command=clear,font=('arial',12,'bold'),bg='#4caf50',fg='white').place(x=330,y=100,width=100,height=30)


app.mainloop()


# In[ ]:





# In[ ]:




