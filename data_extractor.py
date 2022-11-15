import mysql.connector
import pandas as pd

class extractor():
    def __init__(self):
        self.db=mysql.connector.connect(user="root", password="U5@rzo7bs1PUygqY",database="laravel_test")
        self.cursor=self.db.cursor()

    def for_hdbscan_model(self):
        ################ for taking first 20000 records #################
        q1="SELECT * FROM posts where post_id" 
        self.cursor.execute(q1)
        result = self.cursor.fetchall()
        q2="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'posts' ORDER BY ORDINAL_POSITION;"
        self.cursor.execute(q2)
        col_names = self.cursor.fetchall()
        fin_col_names=[]
        for tup in col_names:
            if tup[0] not in fin_col_names:
              fin_col_names.append(tup[0])

        self.df=pd.DataFrame(result)
        #print(fin_col_names,len(fin_col_names))
        self.df.columns=fin_col_names

        ################################## Obtaining fisrt 100 records in each catagory #############

        temp_q="select id from categories"
        self.cursor.execute(temp_q)
        self.catagories = self.cursor.fetchall()
        indices=[]
        for cat in self.catagories:
          #print(cat[0])
          indices.append(self.df.loc[self.df["category_id"]==cat[0]][:100].index.to_list()) #obtaing first 100 records in each catagory
        #print(indices)
        indices = [num for sublist in indices for num in sublist]
        # print(indices,len(indices)) #len(indices)-->1421 some of the self.catagories has less than 100 values
        self.df=self.df.iloc[indices]
        self.df=self.replacing_value(self.df) #used to replace numerical values with its corresponding arabic values
        return self.df
        # self.df.to_csv("dataset.csv") #-->uncomment if you want to check the dataset

    def past_two_days_data(self):

        query_3days="SELECT * FROM posts WHERE created_at > date_sub(now(), interval 3 day);"
        self.cursor.execute(query_3days)
        result = self.cursor.fetchall()
        q2="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'posts' ORDER BY ORDINAL_POSITION;"
        self.cursor.execute(q2)
        col_names = self.cursor.fetchall()
        fin_col_names=[]
        for tup in col_names:
            if tup[0] not in fin_col_names:
              fin_col_names.append(tup[0])

        self.df=pd.DataFrame(result)
        #print(fin_col_names,len(fin_col_names))
        self.df.columns=fin_col_names
        self.df=self.replacing_value(self.df)
        return self.df

    def replacing_value(self,df):
        
        ##################### replacing catagory id with its arabic catagory name #######################3
        self.df=df
        q3="select id,category_name_ar from categories"
        self.cursor.execute(q3)
        self.catagories = self.cursor.fetchall()
        self.catagories=dict(self.catagories)
        self.df["category_id"]=self.df["category_id"].apply(lambda data : self.changer(data))
        #self.df.to_csv("dataset.csv")

        #################### replacing agency_id with agency name ################

        q3="select id,agency_name_ar from agencies"
        self.cursor.execute(q3)
        self.catagories = self.cursor.fetchall()
        self.catagories=dict(self.catagories)
        self.df["agency_id"]=self.df["agency_id"].apply(lambda data : self.changer(data))

        return self.df

    def changer(self,data):
            # print(data)
            return self.catagories[data]
        

# obj=extractor()
# obj.for_hdbscan_model()


