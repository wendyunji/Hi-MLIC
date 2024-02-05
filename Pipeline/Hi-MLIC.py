import joblib
import os
import pandas as pd
from utils import test_result

class Pipeline():
    def __init__(self, X_data_path, L1_y_data_path, L2_y_data_path, L3_y_data_path, L1_model_path, L2_model_path, L3_1_model_path, L3_2_model_path, L3_3_model_path, L3_4_model_path):
        self.X_data = pd.read_csv(X_data_path)
        self.L1_y_data = pd.read_csv(L1_y_data_path)
        self.L2_y_data = pd.read_csv(L2_y_data_path)
        self.L3_y_data = pd.read_csv(L3_y_data_path)
        self.L1_model = joblib.load(L1_model_path)
        self.L2_model = joblib.load(L2_model_path)
        self.L3_1_model = joblib.load(L3_1_model_path)
        self.L3_2_model = joblib.load(L3_2_model_path)
        self.L3_3_model = joblib.load(L3_3_model_path)
        self.L3_4_model = joblib.load(L3_4_model_path)

    def run(self):
        # L1 모델 결과 보기
        L1_y_pred = self.L1_model.predict(self.X_data)
        L1_y_test = self.L1_y_data
        test_result(self.L1_model, L1_y_test, L1_y_pred)

        # 리스트 업데이트
        L1_y_pred_list = L1_y_pred.tolist()

        # L2 모델 결과 보기
        malicious_indices = self.L1_y_data[self.L1_y_data['attack_category'] != 0].index
        L2_X_test = self.X_data.iloc[malicious_indices]
        L2_y_pred = self.L2_model.predict(L2_X_test)
        L2_y_test = self.L2_y_data
        test_result(self.L2_model, L2_y_test, L2_y_pred)

        # 리스트 업데이트
        L2_y_pred_list = L1_y_pred_list.copy()
        for i in range(len(L2_y_pred)):
            L2_y_pred_list[malicious_indices[i]] = L2_y_pred[i]

        # L3 모델 결과 보기
        class_models = [self.L3_1_model, self.L3_2_model, self.L3_3_model, self.L3_4_model]
        class_names = ['Reconnaissance', 'Access', 'Dos', 'Malware']

        L3_y_test = self.L3_y_data.iloc[malicious_indices]
        L3_y_pred_list = L1_y_pred_list.copy()

        for class_index, class_model in enumerate(class_models):
            L2_indices = L2_y_pred_list.index(class_index + 1)
            full_indices = malicious_indices[L2_indices]

            X_test_selected = L2_X_test.iloc[L2_indices]
            y_pred = class_model.predict(X_test_selected)
            y_test_selected = L3_y_test.iloc[L2_indices]

            for i in range(len(y_pred)):
                L3_y_pred_list[full_indices[i]] = y_pred[i]

            test_result(class_model, y_test_selected, y_pred)

        test_result('Final', self.L3_y_data, L3_y_pred_list)


if __name__ == '__main__':
    X_data_path = 'data/X_data.csv'
    L1_y_data_path = 'data/L1_y_data.csv'
    L2_y_data_path = 'data/L2_y_data.csv'
    L3_y_data_path = 'data/L3_y_data.csv'
    L1_model_path = 'model/L1_model.pkl'
    L2_model_path = 'model/L2_model.pkl'
    L3_1_model_path = 'model/L3_1_model.pkl'
    L3_2_model_path = 'model/L3_2_model.pkl'
    L3_3_model_path = 'model/L3_3_model.pkl'
    L3_4_model_path = 'model/L3_4_model.pkl'

    pipeline = Pipeline(X_data_path, L1_y_data_path, L2_y_data_path, L3_y_data_path, L1_model_path, L2_model_path, L3_1_model_path, L3_2_model_path, L3_3_model_path, L3_4_model_path)
    pipeline.run()
