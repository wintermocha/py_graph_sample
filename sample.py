import os
import tarfile
from six.moves import urllib
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def fetch_housing_data(housing_url = HOUSING_URL, housing_path = HOUSING_PATH):
   if not os.path.isdir(housing_path):
      os.makedirs(housing_path)
   tgz_path = os.path.join(housing_path, "housing.tgz")
   urllib.request.urlretrieve(housing_url, tgz_path)
   housing_tgz = tarfile.open(tgz_path)
   housing_tgz.extractall(path=housing_path)
   housing_tgz.close()

import pandas as pd
def load_housing_data(housing_path = HOUSING_PATH):
   csv_path = os.path.join(housing_path, "housing.csv")
   return pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
   shuffled_indices = np.random.permutation(len(data))
   test_set_size = int(len(data) * test_ratio)
   test_indices = shuffled_indices[:test_set_size]
   train_indices = shuffled_indices[test_set_size:]
   return data.iloc[train_indices], data.iloc[test_indices]




fetch_housing_data()
housing = load_housing_data()

import matplotlib.pyplot as plt
housing.hist(bins=100, figsize=(20,15))
plt.show()