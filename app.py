import pickle
import pandas as pd
from io import StringIO
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import hstack
import streamlit as st

models = {}

scaler = MinMaxScaler()

prompt = st.chat_input("Say something")
with open('models/gnb.sav', 'rb') as file:
    gnb = pickle.load(file)
with open('models/bnb.sav', 'rb') as file:
    bnb = pickle.load(file)
with open('models/mnb.sav', 'rb') as file:
    mnb = pickle.load(file)
with open('models/svc.sav', 'rb') as file:
    svc = pickle.load(file)
with open('models/lsvc.sav', 'rb') as file:
    lsvc = pickle.load(file)
with open('models/knc.sav', 'rb') as file:
    knc = pickle.load(file)
with open('models/rnc.sav', 'rb') as file:
    rnc = pickle.load(file)
with open('models/dtc.sav', 'rb') as file:
    dtc = pickle.load(file)
with open('models/etc.sav', 'rb') as file:
    etc = pickle.load(file)
with open('models/rfc.sav', 'rb') as file:
    rfc = pickle.load(file)
with open('models/retc.sav', 'rb') as file:
    retc = pickle.load(file)


with open('models/count_vectorizer.sav', 'rb') as file:
    vectorizer = pickle.load(file)


headers = ['Gaussian Naive Bayes', 'Bernoulli Naive Bayes', 'Multinomial Naive Bayes',
           'Support Vector Classifier', 'Linear Support Vector Classifier',
           'K Nearest Classifier', 'Radius Nearest Classifier', 'Decision Tree Classifier',
           'Extra Tree Classifier', 'Random Forest Classifier', 'Random Forest Extra Trees Classifier']
values = []
def remove_select_at_start(query):
    if query.startswith('select'):
        return query[len('select'):].lstrip()
    else:
        return query

def clean_data(input_string):
    input_string=input_string.lower()
    input_string=input_string.strip()
    input_string = remove_select_at_start(input_string)

    data = StringIO(input_string)
    df = pd.read_csv(data, names=['Query'])
    df['lunghezza'] = df['Query'].apply(len)
    df['Select_Count'] = df['Query'].str.count('select')
    df[['lunghezza', 'Select_Count']] = scaler.fit_transform(df[['lunghezza', 'Select_Count']])
    df2 = vectorizer.transform(df['Query'])
    df = hstack([df2, df[['lunghezza', 'Select_Count']].values])
    return df.toarray()


def predict(input, modelo):
    input2 = clean_data(input)
    return modelo.predict(input2)

def color_negative_red(value):
    color=''
    if value == 'Dannosa':
        color = 'red'
    elif value=='Normale':
        color='green'
    return f'background-color: {color}'
def validate(result):
    if result==1:
        return "Dannosa"
    else: return "Normale"
if prompt:
    values=[]
    values.append(validate(predict(prompt,gnb)))
    values.append(validate(predict(prompt, bnb)))
    values.append(validate(predict(prompt, mnb)))
    values.append(validate(predict(prompt, svc)))
    values.append(validate(predict(prompt, lsvc)))
    values.append(validate(predict(prompt, knc)))
    values.append(validate(predict(prompt, rnc)))
    values.append(validate(predict(prompt, dtc)))
    values.append(validate(predict(prompt, etc)))
    values.append(validate(predict(prompt, rfc)))
    values.append(validate(predict(prompt, retc)))
    df = pd.DataFrame({'Nomi modelli': headers, 'Valori predetti': values})
    df= df.style.applymap(color_negative_red)
    st.write(df)