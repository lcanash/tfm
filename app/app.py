import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score 
from scikitplot.metrics import  plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve

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
		model = pickle.loads(modelo.sav)
	else:
		st.stop()  
			

with preprocessing:
	st.header("Preprocessing")

	st.text("Here is a list of the features in the data:")

	if lung_data is not None:
		st.write(lung_data.columns)

	feature = st.text_input("First, choose which feature shall be the the predicted variable for the model:")
