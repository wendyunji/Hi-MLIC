import pandas as pd
import numpy as np
import xgboost as xgb

def calculate_FIS(data):
    num_attack_categories = len(data['attack_category'].unique())

    intrusion_means = {}
    for attack_category in data['attack_category'].unique():
        intrusion_data = data[data['attack_category'] == attack_category].drop(columns=['attack_category'])
        intrusion_means[attack_category] = intrusion_data.mean()

    FIS_values = {}
    for feature in data.columns:
        if feature != 'attack_category':
            FIS_sum = 0
            for i in range(num_attack_categories):
                for j in range(num_attack_categories):
                    mean_diff = np.abs(intrusion_means[i][feature] - intrusion_means[j][feature])
                    similarity = 1 - mean_diff
                    FIS_sum += similarity
            FIS_values[feature] = FIS_sum / (num_attack_categories ** 2)

    # Rank features by FIS value
    FIS_values = sorted(FIS_values.items(), key=lambda x: x[1], reverse=True)
    
    return FIS_values


def feature_impact_analysis(X, y_pred, y_true):
    # Get intrusion types with recall below 50%
    attack_categorys = np.unique(y_true)
    low_recall_IT = [attack_category for attack_category in attack_categorys if np.mean(y_pred[y_true == attack_category] == attack_category) < 0.5]
    
    # Filter instances by low_recall_IT
    filtered_inst = X[y_true.isin(low_recall_IT)]
    filtered_y_pred = y_pred[y_true.isin(low_recall_IT)]
    filtered_y_true = y_true[y_true.isin(low_recall_IT)]
    
    # Create CG and IG groups
    CG = filtered_inst[(filtered_y_pred == filtered_y_true)]
    IG = filtered_inst[(filtered_y_pred != filtered_y_true)]
    
    # Accumulate feature gap between IG and CG
    F_gaps = {}
    for feature in X.columns:
        avg_CG = np.mean(CG[feature])
        avg_IG = np.mean(IG[feature])
        F_gaps[feature] = abs(avg_CG - avg_IG)

    # Rank features by gap
    F_gaps = sorted(F_gaps.items(), key=lambda x: x[1], reverse=True)
    
    return F_gaps

def feature_importance_ranking(X, y, num_layers):
    feature_importance = {}
    
    for layer in range(1, num_layers + 1):
        # Train XGBoost model for current layer
        model = xgb.XGBClassifier()
        model.fit(X, y[layer])
        
        # Get feature importance scores
        importance_scores = model.feature_importances_
        
        # Accumulate feature importance scores for each layer
        for i, score in enumerate(importance_scores):
            feature = X.columns[i]
            if feature not in feature_importance:
                feature_importance[feature] = [score]
            else:
                feature_importance[feature].append(score)
    
    # Calculate average feature importance across all layers
    avg_feature_importance = {feature: np.mean(scores) for feature, scores in feature_importance.items()}
    
    # Rank features by average importance score
    ranked_features = sorted(avg_feature_importance.items(), key=lambda x: x[1], reverse=True)
    
    return ranked_features