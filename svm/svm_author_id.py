#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
from __future__ import print_function
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
print("Start training")
t0 = time()
clf = svm.SVC(kernel="linear")
clf.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")

print("start predicting")
t0 = time()
prediction = clf.predict(features_test)
print("predict time:", round(time() - t0, 3), "s")

# accuracy
print("Calculating accuracy")
accuracy = accuracy_score(labels_test, prediction)
print("Accuracy calculated, and the accuracy is", accuracy)
#########################################################


