
def classify(features_train, labels_train): 
  from sklearn.naive_bayes import GaussianNB
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
 
    clf = GaussianNB()
	clf.fit(features_train,labels_train)
	pred = clf.pred()
    ### your code goes here!
    
    