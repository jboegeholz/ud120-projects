#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "number of data points: ", len(enron_data)

print "number of features: ", len(enron_data["METTS MARK"])

poi_count = 0
for entry in enron_data:
    if enron_data[entry]["poi"]:
        poi_count = poi_count + 1

print "number of pois: ", poi_count


