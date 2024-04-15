import pandas as pd
from utils import devideFeatures, xEncoding, yEncoding, returnData
import sys

class Encoding():
    def __init__(data_path, save_path):
        self.data = pd.read_csv(data_path)
        self.save_path = save_path

    def run(self):
        numeric_features, categorical_features = devideFeatures(self.data)
        X_data = xEncoding(self.data, numeric_features, categorical_features)
        y_data = yEncoding(self.data)
        encoded_data = returnData(X_data, y_data)
        encoded_data.to_csv(self.save_path, index=False)

if __name__ == '__main__':
    data_path = 'data/'+sys.argv[1]
    save_path = 'data/'+sys.argv[2]

    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()

    encoding = Encoding(data_path, save_path)
    encoding.run()





