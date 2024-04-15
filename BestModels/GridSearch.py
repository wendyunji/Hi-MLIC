from utils import search_best_model, save_model, save_prediction, save_result, define_models, define_hyperparameters
import sys
import pandas as pd

class GridSearch:
    def __init__(self, X_train, y_train, X_test, file_name):
        self.models = define_models()
        self.hyperparameters = define_hyperparameters()
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.saved_dir = 'data/'
        self.output_path = 'data/'
        self.file_name = file_name

    def search_best_model(self):
        search_best_model(self.models, self.hyperparameters, self.X_train, self.y_train, self.X_test, self.saved_dir,
                          self.output_path, self.file_name)

    def save_model(self, model):
        save_model(model, self.saved_dir, self.file_name)

    def save_prediction(self, predictions):
        save_prediction(predictions, self.output_path, self.file_name)

    def save_result(self, df):
        save_result(df, self.output_path, self.file_name)

if __name__ == '__main__':
    file_name = sys.argv[1]

    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()

    X_data_path = 'data/X_train.csv'
    y_data_path = 'data/y_train.csv'
    X_test_path = 'data/X_test.csv'

    X_train = pd.read_csv(X_data_path)
    y_train = pd.read_csv(y_data_path)
    X_test = pd.read_csv(X_test_path)

    grid_search_best_model = GridSearch(X_train, y_train, file_name)

