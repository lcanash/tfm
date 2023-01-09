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
	if uploaded_file is not None:
		lung_data = pd.read_csv(uploaded_file)
		model = pickle.loads(https://github.com/lcanash/tfm/blob/main/app/modelo.sav)
	else:
		st.stop()  
			

with preprocessing:
	st.header("Preprocessing")

	st.text("Here is a list of the features in the data:")

	if lung_data is not None:
		st.write(lung_data.columns)
