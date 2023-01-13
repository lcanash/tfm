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
	st.header("Example data")
	st.text("Click here to see an example prediction with some internal samples")
	exampled = st.button("Example")
	if exampled:
		DATA_URL = ("./app/sample.csv")
		sample = pd.read_csv(DATA_URL)
		st.markdown("The samples used for this prediction come from the repository Curated Microarray Database(CuMiDa). In this case, 6 samples were extracted from the original dataset randomly. Half of the samples are tumoral and the other half are normal.")
		st.write(sample)
		prueba = st.button("Predict")
		if prueba:
			    st.write(model.predict(sample))
		st.markdown("For more information about the dataset, please see the last section of this app.")
with dataset:
	st.header("Load dataset")
	st.text("Select your microarray dataset:") 

	uploaded_file = st.file_uploader("Choose a file")
	submitted = st.button("Submit")
	if uploaded_file is not None:
		lung_data = pd.read_csv(uploaded_file)
	else:
		st.stop()  
			

with preprocessing:
	st.header("Data")
	if submitted:
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
	st.text("You can view some information about the model and the data used to train it.")
	
