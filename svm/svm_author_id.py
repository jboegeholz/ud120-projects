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

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# reduce training set size
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
# TODO: http://scikit-learn.org/stable/auto_examples/svm/plot_iris.html
#########################################################
print("Start training")
t0 = time()
clf = svm.SVC(C=10000.0, kernel="rbf")
# C=10.0 -> 0.616
# C=100.0 -> 0.616
# C=1000.0 -> 0.821
# C=10000.0 -> 0.892
clf.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")

print("start predicting")
t0 = time()
# prediction = clf.predict(features_test[50].reshape(1, -1))
prediction = clf.predict(features_test)
#print("Prediction for 10th element: ")
print(list(prediction).count(1))
#print(prediction)
print("predict time:", round(time() - t0, 3), "s")

# accuracy
# print("Calculating accuracy")
# accuracy = accuracy_score(labels_test, prediction)
# print("Accuracy calculated, and the accuracy is", accuracy)
#########################################################


