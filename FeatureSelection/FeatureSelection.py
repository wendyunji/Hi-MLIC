from utils import calculate_FIS, feature_impact_analysis, feature_importance_ranking
import sys

class FeatureSelection():
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        
    def run(self):
        # Calculate FIS
        FIS_values = calculate_FIS(self.data)
        
        # Feature impact analysis
        X = self.data.drop(columns=['attack_category'])
        y_pred = self.data['attack_category']
        y_true = self.data['attack_category']
        F_gaps = feature_impact_analysis(X, y_pred, y_true)
        
        # Feature importance ranking
        num_layers = 3
        feature_importance = feature_importance_ranking(X, y, num_layers)
        
        return FIS_values, F_gaps, feature_importance
    
if __name__ == '__main__':
    data_path = 'data/'+sys.argv[1]
    
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
    
    feature_selection = FeatureSelection(data_path)
    FIS_values, F_gaps, feature_importance = feature_selection.run()
    
    print("FIS values: ", FIS_values)
    print("Feature gaps: ", F_gaps)
    print("Feature importance: ", feature_importance)

"""
How to run:
$ python FeatureSelection.py data.csv
"""