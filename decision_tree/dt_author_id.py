#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#print len(features_train[0])
print("Start training")
t0 = time()
clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")

print("start predicting")
t0 = time()
# prediction = clf.predict(features_test[50].reshape(1, -1))
prediction = clf.predict(features_test)

print("predict time:", round(time() - t0, 3), "s")

# accuracy
print("Calculating accuracy")
accuracy = accuracy_score(labels_test, prediction)
print("Accuracy calculated, and the accuracy is", accuracy)

