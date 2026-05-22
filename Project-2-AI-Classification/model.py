from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import numpy as np
import random


def train_models():

    iris = load_iris()

    X = iris.data
    y = iris.target

    noise = np.random.normal(
        0,
        0.8,
        X.shape
    )

    X = X + noise

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.4,
        shuffle=True
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {

    "KNN": KNeighborsClassifier(
        n_neighbors=13
    ),

    "Logistic Regression": LogisticRegression(
        max_iter=50
    ),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=1
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=8,
        max_depth=2
    )
}
    results = []

    best_accuracy = 0
    best_model = ""

    for name, model in models.items():

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        accuracy = round(
            accuracy * 100,
            2
        )

        if accuracy > best_accuracy:

            best_accuracy = accuracy
            best_model = name

        results.append({

            "model": name,
            "accuracy": accuracy

        })

    return results, best_model, best_accuracy