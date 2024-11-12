#import necessary libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import tree
import seaborn as sns

#create function for CART modeling
def cart_modeling(data, target):
    #load data
    df = pd.read_csv(data)
    #convert non-numeric data into numeric type
    d = {'yes': 1, 'no': 0}
    df= df.apply(lambda col: col.map(d) if col.dtypes == 'object' else col)
    
    #calculate correlation
    corr_matrix = df.corr()
    #create a mask
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    #set up plot
    fig, ax = plt.subplots(figsize=(10,6))
    sns.heatmap(corr_matrix, mask=mask, cmap='coolwarm', ax=ax)
    plt.savefig('heatmap_of_correlation', format='png', dpi=600)

    #features selection
    threshold = 0.05
    feature= []
    for col in corr_matrix.abs().columns:
        if any(corr_matrix[col].abs().drop(col) >= threshold):
            feature.append(col)
    X = df[feature] #features
    y = df[target] #target variable

    #split dataset into train set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    
    #train model
    #create a decision tree classifer object
    clf = DecisionTreeClassifier()
    #train classifer
    clf = clf.fit(X_train,y_train)
    #predict the respone for test dataset
    y_pred = clf.predict(X_test)

    #evaluate model
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred)) #MSE value

    #visualization of tree
    fig, ax = plt.subplots(figsize=(10,6))
    tree.plot_tree(clf, feature_names=feature, class_names=['1', '0'], filled=True)
    plt.savefig('decision_tree_plot.png', format='png', dpi=600)

    #return heatmap plot and model visualization
    return fig, ax
