
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from azureml.core import Workspace, Dataset
import argparse
from azureml.core.run import Run


def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # Load dataset
    subscription_id = '4999417e-f032-4d4c-982a-c229e26aa825'
    resource_group = 'udacity-learning'
    workspace_name = 'udacity'

    workspace = Workspace(subscription_id, resource_group, workspace_name)

    dataset = Dataset.get_by_name(workspace, name='heart_failure_dataset')
    df = dataset.to_pandas_dataframe()
    
    X, y = df.iloc[:,:-1], df['DEATH_EVENT']

    model = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(class_weight='balanced', C=args.C, max_iter=args.max_iter))
        ])

    auc_scorer = make_scorer(roc_auc_score, greater_is_better=True)
    score = cross_val_score(model, X, y, cv=4, n_jobs=-1, scoring=auc_scorer)
    run.log("AUC_weighted", np.float(np.mean(score)))


if __name__ == '__main__':
    main()
