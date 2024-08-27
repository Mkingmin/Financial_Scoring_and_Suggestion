#import necessary libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from io import StringIO
from IPython.display import Image 
from sklearn.datasets import load_iris  
import matplotlib.pyplot as plt  
from sklearn import tree

#loading data
df= pd.read_csv('AER_credit_card_data.csv')
df.head()

#convert non-numerical data into numerical data
d= {'yes': 1, 'no': 0}
df['card']= df['card'].map(d)

d= {'yes': 1, 'no': 0}
df['owner']= df['owner'].map(d)

d= {'yes': 1, 'no': 0}
df['selfemp']= df['selfemp'].map(d)

#split dataset in features and target variable => Feature selection
feature= ['reports', 'age', 'income', 'share', 'expenditure', 'owner', 'selfemp', 'majorcards', 'active']
X= df[feature] #features
y= df['card'] #target variable

#split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

#Evaluate the model
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#visualize the result 
plt.figure(figsize=(10, 8))  
tree.plot_tree(clf, feature_names=feature, class_names=['1', '0'], filled=True)  

#save the plot as a image
plt.savefig('decision_tree_plot.png', format='png', dpi=600)