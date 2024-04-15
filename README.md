<p align="center"><img src="Appendix/Image/logo.gif" alt="logo" width="400px" /></p>

<h3 align="center">
<p> Hierarchical Multilayer Lightweight Intrusion Classification <br> for Various Intrusion Scenarios <br></h3>

## Contents
- [Hi-MLIC](#hi-mlic)
    - [Abstract](#abstract)
    - [Pipeline](#pipeline)
- [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Download Datasets](#download-datasets)
    - [Download Models](#download-models)
    - [Execution](#execution)
- [Data Preprocessing](#data-preprocessing)
    - [Format Consolidation](#format-consolidation)
    - [Encoding](#encoding)

# Hi-MLIC
![Hi-MLIC](https://github.com/CSID-DGU/Hi-MLIC/assets/95370711/832a1789-bb5a-419a-b4fb-38a2f362effb)

## Abstract
The need to develop an effective system to detect and classify intrusions in extensive network data exchanges is increasing. We propose ***Hi-MLIC***, a hierarchical multilayer lightweight intrusion classification model that addresses various intrusion types. To address more kinds of intrusion scenarios and validate efficient data formats for intrusion detection, we consolidated packet capture data from two popular benchmark datasets into a new dataset with the two different original dataset formats. We introduced a hierarchical multilayer approach to reduce the misclassification rate of intrusion types caused by an imbalance between benign and malicious data. Layer-1 separates network traffic into malicious and benign. Layer-2 classifies malicious traffic into four groups, and Layer-3 identifies 23 specific intrusion types. By performing misclassification analysis and eliminating unnecessary features, we not only improved performance in relation to non-hierarchical classification but also reduced model complexity. Our model achieved a recall metric performance of up to 98.8%.

## Pipeline
<p align="center">
    <br>
    <img width="654" alt="4" src="https://github.com/CSID-DGU/Hi-MLIC/assets/95370711/629048e5-661d-4dab-ab3f-d5b298aea464">
    <br>
<p>
Layer-1 functions as a malicious detector, detecting whether the traffic is malicious. The model predominantly learns to differentiate between malicious and benign traffic. Layer-2 operates as a NIST standard classifier, categorizing malicious traffic into four categories: Access, DoS, Malware, and Reconnaissance. Layer-3, within the previously classified four intrusion categories, a further subdivision into 23 specific intrusion types takes place. 


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
   
### Directory Tree
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

# Data Preprocessing
## Format Consolidation 
### Download PCAP Datasets

- [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)
- [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset)


### CICFlowMeter
1. Download the CICFlowMeter from the following link.
    - [CICFlowMeter](https://pypi.org/project/cicflowmeter/)
2. Execute the CICFlowMeter to generate the dataset.
### Argus and Bro
1. Download the Argus and Bro from the following link.
    - [Argus](https://openargus.org/using-argus)
    - [Bro](https://old.zeek.org/current/exercises/getting-started/index.html)
2. Execute the Argus and Bro to generate the dataset.
3. Convert the Argus and Bro datasets to csv format.
3. Consolidate the Argus and Bro datasets into a single dataset.

## Encoding
1. Create directories named "data" under the Encoding directory.
2. Under the data directory, store consolidated data. If the dataset is consolidated with the CICFlowMeter dataset, name the file "CICI.csv". If the dataset is consolidated with the Argus and Bro datasets, name the file "UNSW.csv".
3. Execute the Encoding.py file. (You can specify the input and output file names as arguments.)
```
python Encoding.py consolidated_data.csv encoded_data.csv
```
4. The data will be encoded and stored in the same directory as consolidated_data.csv.
### Directory Tree
```
Encoding/
│
├── data/
│   └── consolidated_data.csv (CICI.csv or UNSW.csv)
|   └── encoded_data.csv
│
├── Encoding.py
└── utils.py
```


# Feature Selection
## Execution
1. Create directories named "data" and "model" under the FeatureSelection directory.
2. Under the data directory, store the encoded data.
3. Execute the FeatureSelection.py file.
```python
python FeatureSelection.py encoded_data.csv
```
4. The feature importance will be calculated and printed.

# Best Model Selection
## Execution
1. Create directories named "data" under the BestModelSelection directory.
2. Under the data directory, store the encoded data.
### Directory Tree
```
BestModelSelection/
│
├── data/
│   └── X_train.csv
│   └── X_test.csv
│   └── y_train.csv
│   └── y_test.csv
│
├── GridSearch.py
└── utils.py
```
3. Execute the BestModelSelection.py file.
```python
python BestModelSelection.py filename
```
