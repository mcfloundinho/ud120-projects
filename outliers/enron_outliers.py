#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
k = reduce(lambda k1, k2:
           k1 if data_dict[k1]['salary'] > data_dict[k2]['salary'] else k2,
           filter(lambda k: data_dict[k]['salary'] != 'NaN', data_dict.keys()))
print(k, data_dict[k]['salary'])
data_dict.pop(k)
data = featureFormat(data_dict, features)
print(list(filter(
    lambda k: data_dict[k]['bonus'] > 5e6 and data_dict[k]['salary'] >= 1e6,
    filter(lambda k: data_dict[k]['salary'] != 'NaN' and
           data_dict[k]['bonus'] != 'NaN', data_dict.keys())
)))


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
