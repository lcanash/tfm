import streamlit as st
import pandas as pd
import pickle

header = st.container()
dataset = st.container()
preprocessing = st.container()
model = st.container()
results = st.container()

with header:
	st.title("Application to detect samples with lungh cancer from microarray datasets")

with dataset:
	st.header("Load dataset")
	st.text("Select your microarray dataset:") 

	uploaded_file = st.file_uploader("Choose a file")
	uploaded_model = st.file_uploader("Choose a model")
	if uploaded_file is not None:
		lung_data = pd.read_csv(uploaded_file)
		model = pickle.loads(uploaded_model.read())
	else:
		st.stop()  
			

with preprocessing:
	st.header("Preprocessing")

	st.text("Here is a view of your data:")
	st.write(lung_data)
