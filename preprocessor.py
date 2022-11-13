import pandas as pd
from bs4 import BeautifulSoup
import re
import umap
# import tensorflow as tf
import tensorflow_hub as hub

class preprocess():
    def __init__(self):
        self.exp='[\u0627-\u064aA-Za-z]+' #re to get arabic and english , i had eliminated numbers and special characters because they dont have much influence 
        self.module_url = "https://tfhub.dev/google/universal-sentence-encoder/4" # this is already a pretrained model ,so need of saving this model with our data
        self.model = hub.load(self.module_url)
        
    def process(self,path):
        self.dataset=pd.read_csv(path,,on_bad_lines='skip')
        self.dataset=self.dataset[["title",'category_id','contents',"agency_id",'tweet_text']]
        self.dataset.fillna("",inplace=True)
        
        self.dataset["title"]=self.dataset["title"].apply(lambda data : " ".join(re.findall(self.exp,data)))
        self.dataset['category_id']=self.dataset["category_id"].apply(lambda data: " ".join(re.findall(self.exp,data)) )
        self.dataset["contents"]=self.dataset['contents'].apply(lambda data : " ".join(re.findall(self.exp,data)))
        self.dataset["agency_id"]=self.dataset["agency_id"].apply(lambda data : " ".join(re.findall(self.exp,data)))
        self.dataset["tweet_text"]=self.dataset["tweet_text"].apply(lambda data: " ".join(re.findall(self.exp,data)))
        ######### removing punctuations
        self.dataset["title"]=self.dataset["title"].apply(lambda data:self.cleanText(data))
        self.dataset["contents"]=self.dataset["contents"].apply(lambda data:self.cleanText(data))
        self.dataset["category_id"]=self.dataset["category_id"].apply(lambda data:self.cleanText(data))
        self.dataset["agency_id"]=self.dataset["agency_id"].apply(lambda data:self.cleanText(data))
        self.dataset["tweet_text"]=self.dataset["tweet_text"].apply(lambda data:self.cleanText(data))
        self.data=self.dataset["title"]+self.dataset["contents"]+self.dataset["category_id"]+dataset["agency_id"]+dataset["tweet_text"]
        self.data=self.data.to_list()
        self.vectorized=self.vectorizing(self.data)
        self.dim_reduced=self.dim_reduction(self.vectorized)
        
        return self.dim_reduced


    def cleanText(self,text):
            text = BeautifulSoup(text, "lxml").text
            text = re.sub(r'\|\|\|', r' ', text) 
            text = re.sub(r'http\S+', r'<URL>', text)
            # text = text.lower()
            # text = text.replace('x', '')
            return text

    def vectorizing(self,data):            
        return self.model(data)
    
    def dim_reduction(self,data):
        return (umap.UMAP(n_neighbors=10, n_components=20, metric='cosine', 
                                random_state=24).fit_transform(data))
