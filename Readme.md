

<p align="center">
   <img src="assets/polipo.png">
</p>


# Overview

S.Q.l.D (SQL Injection Detector) is a project that aim to achieve the almost perfect 
classification of queries between malicious and good one.
The models used for the training are all parts of the **Scikit-Learn** library, instead the deployment part is all made by
a library called **streamlit**

# Dataset

The dataset used is from Kaggle more precisely is this one :

https://www.kaggle.com/datasets/sajid576/sql-injection-dataset

the dataset is really simple, it is just 2 column one for the queries and another one
for the target variable. There are no null values and no missing ones so you can just use it out of the box


# Project Structure 
```
SQLInjection_Detector/
├── Dataset.csv
├── Readme.md
├── Readme2.md
├── Training.ipynb
├── app.py
├── assets
│   ├── Confusion Matrix
│   │   ├── bnb.png
│   │   ├── dtc.png
│   │   ├── etc.png
│   │   ├── gnb.png
│   │   ├── knc.png
│   │   ├── lsvc.png
│   │   ├── mnb.png
│   │   ├── nc.png
│   │   ├── retc.png
│   │   ├── rfc.png
│   │   ├── rnc.png
│   │   └── svc.png
│   ├── DataVisualization
│   │   ├── Bilanciato.png
│   │   ├── DatasetSporco.png
│   │   └── EsplorazioneDataset.png
│   ├── FeatureEng
│   │   ├── features.png
│   │   ├── lunghezza.png
│   │   ├── normalization.png
│   │   └── select_count.png
│   ├── RocCurve
│   │   ├── bnb.png
│   │   ├── dtc.png
│   │   ├── etc.png
│   │   ├── gnb.png
│   │   ├── knc.png
│   │   ├── lsvc.png
│   │   ├── mnb.png
│   │   ├── retc.png
│   │   ├── rfc.png
│   │   ├── rnc.png
│   │   └── svc.png
│   ├── polipo.png
│   └── svc
│       ├── lsvc.png
│       └── svc.png
└── models.zip

```

# Training operations

1. Data Cleaning
   - deletion of all unnecessary lines
   -  turn everything in lower case
   -  removal of outer spaces
   -  deletion of the first select instruction
2. Feature Engineering
   -  length of the query
   -  number of select instructions in a query

# Model Used

- Naive Bayes
- Support Vector Machines
- Nearest Neighbours
- Decision Tree
- Random Forest

# Results

All the graphics results can be viewed in the directories:
- Confusion Matrix (for all the models)
- RocCurve(Except for Nearest Centroid)
- svc (just for SVMs models)

All the results can be also seen in the [S.Q.l.D_documentazione.pdf](documents%2FS.Q.l.D_documentazione.pdf)


# How to run 

1. create a folder called `models`
2. extract models.zip files content in the models folder
3. run the app with
```bash
   streamlit run app.py
```   

![polipo.gif](assets%2Fpolipo.gif)