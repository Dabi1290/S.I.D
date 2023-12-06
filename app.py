import pickle
import pandas as pd
from io import StringIO
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import hstack
import streamlit as st


scaler = MinMaxScaler()
prompt = st.chat_input("Say something")
with open('models/svc.sav', 'rb') as file:
    loaded_model = pickle.load(file)
with open('models/count_vectorizer.sav', 'rb') as file:
    vectorizer = pickle.load(file)
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


def predict(input):
    input = clean_data(input)
    return loaded_model.predict(input)

if prompt:

    st.write(predict(prompt))