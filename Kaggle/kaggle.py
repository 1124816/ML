# Imports

# pandas
import pandas as pd
from pandas import Series,DataFrame

# numpy, matplotlib, seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

train = pd.read_csv("./csv/train.csv")

train = train.drop(['PassengerId','Name','Ticket'], axis=1)

train["Embarked"] = train["Embarked"].fillna("S")
train["Age"] = train["Age"].fillna(train["Age"].median())

train["Sex"][train["Sex"] == "female"] = 0
train["Sex"][train["Sex"] != 0] = 1

train["Embarked"][train["Embarked"] == "S"] = 0
train["Embarked"][train["Embarked"] == "C"] = 1
train["Embarked"][train["Embarked"] == "Q"] = 2

forest = RandomForestClassifier(max_depth = 20, min_samples_split=2, n_estimators = 100, random_state = 1)
model = forest.fit(train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values, train["Survived"].values)
print(model.score(train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values, train["Survived"].values))

print(train.describe)
