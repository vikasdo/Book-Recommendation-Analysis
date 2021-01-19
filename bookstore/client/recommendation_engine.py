

from bookstore import  app

# from functools import lru
import pandas as pd
import numpy as np
# import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation
from sklearn.metrics.pairwise import pairwise_distances

import warnings
warnings.filterwarnings('ignore')
import numpy as np
import os, sys
import re
k=10
metric='cosine'
# from scipy.sparse import csr_matrix
def recommendItem(user_id, ratings,books, metric=metric):    
    if (user_id not in ratings.index.values) or type(user_id) is not int:
        print ("User id should be a valid integer from this list :\n\n {} ".format(re.sub('[\[\]]', '', np.array_str(ratings.index.values))))
    else:    
        prediction=[]
        
        ## Item based
        if ratings.loc[user_id].value_counts()[0]> (ratings.shape[1])/2  : #that means the user didn't rate
          print("switching to  Item based _content")
          for i in range(ratings.shape[1]):
                              if (ratings[str(ratings.columns[i])][user_id] !=0): #not rated already
                                  prediction.append(predict_itembased(user_id, str(ratings.columns[i]) ,ratings, metric))
                              else:                    
                                  prediction.append(-1)
        else:
        #### user based
          print("switching to  Collabarative(user) based ")

          for i in range(ratings.shape[1]):
              if (ratings[str(ratings.columns[i])][user_id] !=0): #not rated already
                  prediction.append(predict_userbased(user_id, str(ratings.columns[i]) ,ratings, metric))
              else:                    
                  prediction.append(-1) #for already rated items
        # print(prediction)
        prediction = pd.Series(prediction)
        prediction = prediction.sort_values(ascending=False)
        recommended = prediction[:10]
        # print(recommended ,"----")
        # print ("As per {0} approach....Following books are recommended..." .format(select.value))lis
        output=[]
        
        for i in range(len(recommended)):
            output.append(books.ISBN[recommended.index[i]])
            # print ("{0}. {1}".format(i+1,books.ISBN[recommended.index[i]].encode('utf-8')))                       
        return output

#This function predicts the rating for specified user-item combination based on item-based approach
def predict_itembased(user_id, item_id, ratings, metric = metric, k=k):
    prediction= wtd_sum =0
    user_loc = ratings.index.get_loc(user_id)
    item_loc = ratings.columns.get_loc(item_id)
    similarities, indices=findksimilaritems(item_id, ratings) #similar users based on correlation coefficients
    sum_wt = np.sum(similarities)-1
    product=1
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == item_loc:
            continue;
        else:
            product = ratings.iloc[user_loc,indices.flatten()[i]] * (similarities[i])
            wtd_sum = wtd_sum + product                              
    prediction = int(round(wtd_sum/sum_wt))
    
    #in case of very sparse datasets, using correlation metric for collaborative based approach may give negative ratings
    #which are handled here as below //code has been validated without the code snippet below, below snippet is to avoid negative
    #predictions which might arise in case of very sparse datasets when using correlation metric
    if prediction <= 0:
        prediction = 1   
    elif prediction >10:
        prediction = 10

    # print ('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id,item_id,prediction))    
    
    return prediction
def findksimilaritems(item_id, ratings, metric=metric, k=k):
    similarities=[]
    indices=[]
    ratings=ratings.T
    loc = ratings.index.get_loc(item_id)
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute')
    model_knn.fit(ratings)
    
    distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()

    return similarities,indices 
def findksimilarusers(user_id, ratings, metrci = metric,k=k):
  similarities = []
  indicies = []
  model_knn = NearestNeighbors(metric = metric, algorithm = 'brute')
  model_knn.fit(ratings)
  loc = ratings.index.get_loc(user_id)
  distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1,-1), n_neighbors = k+1)
  similarities = 1-distances.flatten()
  return similarities, indices
 
#This function predicts rating for specified user-item combination based on user-based approach
def predict_userbased(user_id, item_id, ratings, metric = metric, k=k):
    prediction=0
    user_loc = ratings.index.get_loc(user_id)
    item_loc = ratings.columns.get_loc(item_id)
    similarities, indices=findksimilarusers(user_id, ratings,metric, k) #similar users based on cosine similarity
    mean_rating = ratings.iloc[user_loc,:].mean() #to adjust for zero based indexing
    sum_wt = np.sum(similarities)-1
    product=1
    wtd_sum = 0 
    
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == user_loc:
            continue;
        else: 
            ratings_diff = ratings.iloc[indices.flatten()[i],item_loc]-np.mean(ratings.iloc[indices.flatten()[i],:])
            product = ratings_diff * (similarities[i])
            wtd_sum = wtd_sum + product
    
    #in case of very sparse datasets, using correlation metric for collaborative based approach may give negative ratings
    #which are handled here as below
    if prediction <= 0:
        prediction = 1   
    elif prediction >10:
        prediction = 10
    
    prediction = int(round(mean_rating + (wtd_sum/sum_wt)))
    # print ('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id,item_id,prediction))
 
    return prediction


#These are file paths for our book,ratingmatrix
path_for_pkl=app.config['RATINGMATRIX']
path_for_pkl_books=app.config['BOOKPKL']



#Thee main class for Implementing the Recommendation...

class Recommendation_engine:

  '''
  constructor to store dataframe as local(self objects)
  '''
  def __init__(self):
         
    self.df_data=pd.read_pickle(path_for_pkl)
    self.book=pd.read_pickle(path_for_pkl_books)
  def getRecommendedBooks(self,user_id):


    
    out=recommendItem(user_id,self.df_data,self.book)
    book=self.book.loc[self.book['ISBN'].isin(out)]

    return book

