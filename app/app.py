import streamlit as st
import pandas as pd
import pickle

header = st.container()
example = st.container()
dataset = st.container()
preprocessing = st.container()
prediction = st.container()
results = st.container()


MODEL_URL = ("./app/model.sav")
model = pickle.load(open(MODEL_URL)


with header:
	st.title("Application to detect samples with lung cancer from microarray datasets")

with example:
	DATA_URL = ("./app/samplet.csv")
	example = pd.read_csv(DATA_URL)
	st.write(example)
	
with dataset:
	st.header("Load dataset")
	st.text("Select your microarray dataset:") 

	uploaded_file = st.file_uploader("Choose a file")
	if uploaded_file is not None:
		lung_data = pd.read_csv(uploaded_file)
	else:
		st.stop()  
			

with preprocessing:
	st.header("Data")

	st.text("Here is a view of your data:")
	st.write(lung_data)
	

with prediction:
	pred = model.predict(lung_data)

	
with results:
	st.header("Results")
	st.write(pred)
