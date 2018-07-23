#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)



for point in data:
    salary = point[0]
    if salary > 1000000:
        print(point)
    bonus = point[1]
    if salary > 7000000:
        print(point)
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

eso = []
for data in data_dict:
    item = data_dict[data]["exercised_stock_options"]
    if item != "NaN":
        eso.append(item)

print(max(eso))
print(min(eso))

eso = []
for data in data_dict:
    item = data_dict[data]["salary"]
    if item != "NaN":
        eso.append(item)

print(max(eso))
print(min(eso))

