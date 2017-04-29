import pandas as pd
from pandas import Series,DataFrame


import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import xgboost as xgb
from sklearn.grid_search import GridSearchCV

train = pd.read_csv("./csv/train.csv")[:600]
test = pd.read_csv("./csv/train.csv")[600:]

train = train.drop(['PassengerId','Name','Ticket'], axis=1)
test = test.drop(['PassengerId','Name','Ticket'], axis=1)

train["Embarked"] = train["Embarked"].fillna("S")
train["Age"] = train["Age"].fillna(train["Age"].median())

train["Sex"][train["Sex"] == "female"] = 0
train["Sex"][train["Sex"] != 0] = 1

train["Fare"] = train["Fare"].fillna(train["Fare"].median())

train["Embarked"][train["Embarked"] == "S"] = 0
train["Embarked"][train["Embarked"] == "C"] = 1
train["Embarked"][train["Embarked"] == "Q"] = 2

test["Embarked"] = test["Embarked"].fillna("S")
test["Age"] = test["Age"].fillna(test["Age"].median())

test["Sex"][test["Sex"] == "female"] = 0
test["Sex"][test["Sex"] != 0] = 1

test["Fare"] = test["Fare"].fillna(test["Fare"].median())

test["Embarked"][test["Embarked"] == "S"] = 0
test["Embarked"][test["Embarked"] == "C"] = 1
test["Embarked"][test["Embarked"] == "Q"] = 2
#print(train.describe)
cv_params = {'max_depth': [3,5,7], 'min_child_weight': [1,3,5]}
ind_params = {'learning_rate': 0.1, 'n_estimators': 1000, 'seed':0, 'subsample': 0.8, 'colsample_bytree': 0.8,
             'objective': 'binary:logistic'}

#forest = GridSearchCV(xgb.XGBClassifier(**ind_params), cv_params, scoring = 'accuracy', cv = 5, n_jobs = -1)

forest = RandomForestClassifier(max_depth = 10, min_samples_split=8, n_estimators = 1000, random_state = 2)
model = forest.fit(train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch"]].values, train["Survived"].values)
print(model.score(test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch"]].values, test["Survived"].values))
print(model.feature_importances_)
#, "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"
#, "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"
#my_prediction = forest.predict(test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch"]].values)


#PassengerId =np.array(test["PassengerId"]).astype(int)
#my_solution = pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"])
#print(my_solution)


#print(my_solution.shape)


#my_solution.to_csv("my_solution.csv", index_label = ["PassengerId"])
