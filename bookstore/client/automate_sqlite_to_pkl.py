import pickle
import sqlite3
import pandas as pd
import numpy as np
from bookstore import app

def update_rating_matrix():
    data = pd.read_pickle(app.config["RATINGMATRIX"])

    conn = sqlite3.connect(app.config["SQLITE_DB_DIR"])
    c = conn.cursor()

    user = pd.read_sql('Select * from user', conn)

    vals_to_append = []
    for u_id in user.id.values:
        if u_id not in data.index.values:
            vals_to_append.append(u_id)

    if len(vals_to_append) != 0:
        for i in range(vals_to_append[0], vals_to_append[-1]+1):
            data.loc[i] = np.zeros(len(data.columns.values))

        data.to_pickle(app.config["RATINGMATRIX"])
