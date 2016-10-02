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
with open('../final_project/poi_names.txt') as f:
    poi_names = f.readlines()

print(len(enron_data))
print(len(enron_data[enron_data.keys()[0]]))
poi_list = list(filter(lambda k: enron_data[k]['poi'], enron_data.keys()))
print(len(poi_list))

poi_str = str(poi_list)

def name_exists(name):
    """Tell whether a name from poi_names is in the dataset."""
    try:
        name_cap = ' '.join(name.split(' ', 1)[1].split(', ')).upper().strip()
        return name_cap in poi_str
    except:
        return False

print(len(filter(name_exists, poi_names)))
print(enron_data['PRENTICE JAMES']['total_stock_value'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print(max(map(lambda k: (k, enron_data[k]['total_payments']),
              ('LAY KENNETH L', 'SKILLING JEFFREY K', 'FASTOW ANDREW S')),
          key=lambda t: t[1]))
print(len(filter(lambda k: enron_data[k]['salary'] != 'NaN',
                 enron_data.keys())))
print(len(filter(lambda k: enron_data[k]['email_address'] != 'NaN',
                 enron_data.keys())))
print(1.0 * len(filter(lambda k: enron_data[k]['total_payments'] == 'NaN',
                       enron_data.keys())) / len(enron_data.keys()))
print(1.0 * len(filter(lambda k: enron_data[k]['total_payments'] == 'NaN',
                       poi_list)) / len(poi_list))
