#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# for C in (10.0, 100.0, 1000.0, 10000.0):
    # clf = SVC(kernel='rbf', C=C)
    # size_train = len(features_train) / 100
    # clf.fit(features_train[:size_train], labels_train[:size_train])
    # pred = clf.predict(features_test)
    # print('%f:\t%f' % (C, accuracy_score(labels_test, pred)))

clf = SVC(kernel='rbf', C=10000.0)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
for i in (10, 26, 50):
    print('%d:\t%d' % (i, pred[i]))
print('#Chris: %d' % sum(pred))
print(accuracy_score(labels_test, pred))

#########################################################


