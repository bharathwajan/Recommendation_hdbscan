from preprocessor import *
# import mysql.connector
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import umap # dimensionality reduction
from sklearn.cluster import DBSCAN
# from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import hdbscan
from deep_translator import GoogleTranslator
import pickle

class trainer():
    def __init__(self):
        pass
    
    def train(self):
        dataset=self.df
        ref=dataset
        dataset=dataset[["title",'category_id','contents',"agency_id",'tweet_text']]
        # dataset.head(5)
        dataset.fillna("",inplace=True)
        ####### preprocessing ########
        obj=preprocess(dataset)
        umap_embeddings=obj.process()
        clusters = hdbscan.HDBSCAN(min_cluster_size = 3,
                               metric='euclidean', 
                                ).fit(umap_embeddings)
        ############ obtain past 2 days data from the server #########

        



