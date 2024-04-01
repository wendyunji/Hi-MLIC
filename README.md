![Hi-MLIC](https://github.com/CSID-DGU/Hi-MLIC/assets/95370711/832a1789-bb5a-419a-b4fb-38a2f362effb)


# Hi-MLIC
Hi-MLIC: Hierarchical Multilayer Lightweight Intrusion Classification for Various Intrusion Scenarios

## Abstract
The need to develop an effective system to detect and classify intrusions in extensive network data exchanges is increasing. We propose ***Hi-MLIC***, a hierarchical multilayer lightweight intrusion classification model that addresses various intrusion types. To address more kinds of intrusion scenarios and validate efficient data formats for intrusion detection, we consolidated packet capture data from two popular benchmark datasets into a new dataset with the two different original dataset formats. We introduced a hierarchical multilayer approach to reduce the misclassification rate of intrusion types caused by an imbalance between benign and malicious data. Layer-1 separates network traffic into malicious and benign. Layer-2 classifies malicious traffic into four groups, and Layer-3 identifies 23 specific intrusion types. By performing misclassification analysis and eliminating unnecessary features, we not only improved performance in relation to non-hierarchical classification but also reduced model complexity. Our model achieved a recall metric performance of up to 98.8%.

### Hierarchical Multilayer Intrusion Machine Learning Classifier Framework/Pipeline
<p align="center">
    <br>
    <img width="654" alt="4" src="https://github.com/CSID-DGU/Hi-MLIC/assets/95370711/629048e5-661d-4dab-ab3f-d5b298aea464">
    <br>
<p>



# Getting Started
## Installation
```
git clone https://github.com/CSID-DGU/Hi-MLIC.git
cd HiMLIC
pip install -e .
```

## Download Datasets
[dataset.md](https://github.com/CSID-DGU/Hi-MLIC/blob/main/dataset.md)

## Download Models
[model.md](https://github.com/CSID-DGU/Hi-MLIC/blob/main/model.md)

## Execution
1. Create directories named "data" and "model" under the Pipeline directory.
2. Under the data directory, store X and y data for each layer in the following tree structure.
3. Under the model directory, store a total of 6 models for each layer in the following tree structure.
4. Execute the HiMLIC.py file.
   
### Directory tree
```
Pipeline/
│
├── data/
│   ├── X_data.csv
│   ├── L1_y_data.csv
│   ├── L2_y_data.csv
│   └── L3_y_data.csv
│
├── model/
│   ├── L1_model.pkl
│   ├── L2_model.pkl
│   ├── L3_1_model.pkl
│   ├── L3_2_model.pkl
│   ├── L3_3_model.pkl
│   └── L3_4_model.pkl
│
├── HiMLIC.py
└── utils.py
```
