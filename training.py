import hdbscan
from preprocessor import preprocess
import pickle
class trainer():
    def __init__(self):
        pass
    def train(self,dataset_path,min_cluster_size=3,metric="euclidean",cluster_selection_method='eom'):
        obj=preprocess()
        umap_embedding=obj.process(dataset_path)
        clusters = hdbscan.HDBSCAN(min_cluster_size = min_cluster_size,
                                    metric=metric, 
                                    cluster_selection_method=cluster_selection_method).fit(umap_embedding)

        pick
