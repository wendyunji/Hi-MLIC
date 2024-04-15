import pandas as pd
import os
import numpy as np
import warnings
import time
from pathlib import Path 
from sklearn.model_selection import GridSearchCV,StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import make_scorer,recall_score
import joblib

warnings.filterwarnings("ignore")

def define_models():
    models = []
    models.append(('RF', RandomForestClassifier())) 
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('QDA', QuadraticDiscriminantAnalysis()))
    models.append(('LR', LogisticRegression()))
    models.append(('ABoost', AdaBoostClassifier()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('MLP', MLPClassifier()))
    return models

def save_model(model,saved_dir,file_name):
    output_path=os.path.join(saved_dir,file_name)
    joblib.dump(model,output_path)
    print(f'{model} 이 {output_path}에 저장되었습니다.')


def save_prediction(predictions,output_path, file_name):
    prediction_path=os.path.join(output_path, file_name+'result.txt')
    with open(prediction_path,'w') as f:
        for pred in predictions:
            f.write(str(pred) + ',')
    print(f'Predictions saved to {prediction_path}')

def save_result(df,output_path, file_name):
    df.to_csv(os.path.join(output_path, file_name+'result.csv'))
    
def search_best_model(models,hyperparameters,X_train,y_train,X_test,saved_dir,output_path,file_name):
    df=pd.DataFrame(columns=['model','params','rc'])
    cnt=0
    model_eval=[]
    best_rc=0.0
    for name, model in models:
        if name in hyperparameters:
            scorers={
                    'recall_score':make_scorer(recall_score,average='weighted')
            }
            model_eval=[]
            param_grid = hyperparameters[name]
            cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=42).split(X_train,y_train)
            grid_search = GridSearchCV(model, param_grid, scoring=scorers, cv=cv,refit='recall_score')
            grid_search.fit(X_train, y_train)
            model_eval.append(name)
            model_eval.append(grid_search.best_params_)
            model_eval.append(grid_search.best_score_)
            df.loc[cnt]=model_eval
            cnt+=1
            print(f'Best hyperparameters for {name}: {grid_search.best_params_}')
            print(f'Best recall score for {name}: {grid_search.best_score_}')
            if grid_search.best_score_ > best_rc:
                save_model(grid_search.best_estimator_,saved_dir,file_name+'.pkl')
                best_rc=grid_search.best_score_
                predictions=grid_search.best_estimator_.predict(X_test)
                save_prediction(predictions,output_path)
    save_result(df,output_path)


hyperparameters = {
    'KNN': {
        'n_neighbors': [3,5,7],
        'weights': ['uniform', 'distance'],
        'metric' : ['euclidean', 'manhattan', 'minkowski']
    },
    'MLP': {
        'hidden_layer_sizes': [(50,), (100,), (150,)],
        'activation': ['relu', 'tanh'],
        'solver':['adam'],
        'learning_rate':['constant'],
        'power_t':[0.5],
        'alpha':[0.0001],
        'max_iter':[10000],
        'early_stopping':[False],
        'warm_start':[False]
    },
    'RF': {
        'n_estimators': [10, 50, 100],
        'max_depth': [5, 10],
    },
    'CART': {
        'max_depth': [5, 10],
        'min_samples_split':[2,3]
    },
    'NB': {
        "var_smoothing" : [1e-11, 1e-10, 1e-9]
    },
    'LDA': {
        "solver":["svd","lsqr"]
    },
    'QDA': {
        "reg_param":[0.1,0.2,0.3,0.4,0.5]
    },
    'LR': {
        'C': [0.001, 0.01, 0.1, 1.0],
    },
    'ABoost': {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 1.0],
    },
}
