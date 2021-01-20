import sqlite3
conn = sqlite3.connect('/home/vikas/Book-Recommendation-Analysis/db.sqlite')
c = conn.cursor()

import pandas as pd

path_for_pkl="/home/vikas/Downloads/rec_data.pkl"
df_data=pd.read_pickle(path_for_pkl)
print(df_data.head())
li=(df_data.columns)#books
li1=(df_data.index)#
# load the data into a Pandas DataFrame
users = pd.read_csv(r'/home/vikas/Downloads/BX-Users.csv', encoding= 'unicode_escape',low_memory=False,sep=';')
books = pd.read_csv(r'/home/vikas/Downloads/BX_Books.csv', encoding= 'unicode_escape',low_memory=False,sep=';')



email_list = ['test'+str(i)+'@gmail.com' for i in range(1,58) ]

users=users.loc[users['User-ID'].isin(li1)]
print(users.columns)
users.columns=['id','location','age']
users['email']= 'test@gmail.com'
users['name']='client'
users['password']='foobar123'

books=books.loc[books['ISBN'].isin(li)]
books.columns=['ISBN','title','author','pubDate','publisher','d','da','bookImage']

books.drop(['d', 'da'], axis=1, inplace=True)
books['book_cost']=110
users.to_sql('user', conn, if_exists='append', index = False)
books.to_sql('books', conn, if_exists='append', index = False)