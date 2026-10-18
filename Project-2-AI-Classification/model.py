"""Train deterministic classifiers on a stratified Iris holdout set."""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


RANDOM_STATE = 42


def train_models():
    """Fit four classifiers on the same reproducible train/test split.

    Scaling is applied only to distance- and gradient-based models. Tree-based
    models use the original Iris measurements. The function returns the table
    data, best model name, and best holdout accuracy for the terminal UI.
    """
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        stratify=y,
        random_state=RANDOM_STATE,
    )

    models = {
        "KNN": make_pipeline(
            StandardScaler(),
            KNeighborsClassifier(n_neighbors=5),
        ),
        "Logistic Regression": make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=1000, random_state=RANDOM_STATE),
        ),
        "Decision Tree": DecisionTreeClassifier(random_state=RANDOM_STATE),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
    }

    results = []
    best_model = ""
    best_accuracy = -1.0

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = round(accuracy_score(y_test, predictions) * 100, 2)
        results.append({"model": name, "accuracy": accuracy})

        if accuracy > best_accuracy:
            best_model = name
            best_accuracy = accuracy

    return results, best_model, best_accuracy
