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

if __name__ == '__main__':


    enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
    print "number of data points: ", len(enron_data)

    print "number of features: ", len(enron_data["METTS MARK"])

    poi_count = 0
    for entry in enron_data:
        if enron_data[entry]["poi"]:
            poi_count = poi_count + 1

    print "number of pois: ", poi_count


    with open("./poi_names.txt") as f:
        lines = f.readlines()
        print len(lines)

    print enron_data["PRENTICE JAMES"]

    print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

    print enron_data["FASTOW ANDREW S"]["total_payments"]
    print enron_data["LAY KENNETH L"]["total_payments"]
    print enron_data["SKILLING JEFFREY K"]["total_payments"]

    # How many folks have a quantified salary?
    print len(dict((key, value) for key, value in enron_data.items() if value["salary"] != 'NaN'))

    # How many with a known email address?
    print len(dict((key, value) for key, value in enron_data.items() if value["email_address"] != 'NaN'))

    #number of pois with nan as total_payments
    print(len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN')))

    # percentage of people with nan
    poi_payments = dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN' and value["poi"])
    print(len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN' )) / float(poi_count) )

