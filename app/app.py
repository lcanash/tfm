import streamlit as st
import pandas as pd
import pickle

header = st.container()
example = st.container()
dataset = st.container()
preprocessing = st.container()
prediction = st.container()
results = st.container()
information = st.container()


MODEL_URL = ("./app/modelo.sav")
model = pickle.load(open(MODEL_URL,"rb"))

with header:
	st.title("Application to detect samples with lung cancer from microarray datasets")

with example:
	exampled
	st.header("Example data")
	st.markdown("Click here to see an example prediction with some internal samples.")
	exampled = st.button("Example")
	if exampled:
		DATA_URL = ("./app/sample.csv")
		sample = pd.read_csv(DATA_URL)
		st.markdown("The samples used for this prediction come from the repository Curated Microarray Database(CuMiDa). In this case, 6 samples were extracted from the original dataset randomly. Half of the samples are tumoral and the other half are normal.")
		st.write(sample)
		prueba = st.button("Predict")
		pre = model.predict(sample)
		st.write(pre)
		st.markdown("For more information about the dataset, please see the last section of this app.")
with dataset:
	st.header("Load dataset")
	st.markdown("Select your microarray dataset:") 

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
			
	predict = st.button("Predict")
	if predict:
		pred = model.predict(lung_data)

		with results:
			st.header("Results")
			st.write(pred)

with information:
	st.header("Information")
	st.markdown("You can view some information about the model and the data used to train it.")
	info = st.button("Info")
	if info:
		st.header("About the data...")
		st.markdown("The data comes from the repository Curated Microarray Database(CuMiDa). This database contains 78 sets of cancer microarray datasets from 30.000 different studies that were obtained from the Gene Expression Omnibus(GEO). The sets were handpicked and extensively curated to be used solely for Machine Learning, as well as submitted to background correction, normalization, sample quality analysis and were manually edited to eliminate erroneous probes.")

		st.markdown("The dataset used for the model consists of 114 samples of lung cancer microarrays, each having 54675 different measures of microarrays. The samples have been diagnosed tumoral or normal depending on the presence of cancer or not. In this case 56 of the samples are tumoral and 58 normal.")
		
		st.header("About the model...")
		st.markdown("The model used for the classification consists on a Support Vector Machine. It has been trained with the described dataset and tuned in order to have the best posible efficiency. It's evaluations scores with the original data are:")
		st.markdown("* **Accuracy:** 0.92")
		st.markdown("* **Precision:** 0.92")
		st.markdown("* **Recall:** 0.92")
		st.markdown("* **F1 Score:** 0.92")
		
