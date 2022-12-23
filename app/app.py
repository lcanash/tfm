import streamlit as st
import pandas as pd
import sklearn as sk
import scikitplot as skplt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score 

header = st.container()
dataset = st.container()
preprocessing = st.container()
modelTraining = st.container()
results = st.container()

with header:
	st.title("Application to detect samples with lungh cancer from microarray datasets")

with dataset:
	st.header("Load dataset")
	st.text("Select your microarray dataset:") 

	uploaded_file = st.file_uploader("Choose a file")
	if uploaded_file is not None:
		lung_data = pd.read_csv(uploaded_file)
	else:
		st.stop()  
			

with preprocessing:
	st.header("Preprocessing")

	st.text("Here is a list of the features in the data:")

	if lung_data is not None:
		st.write(lung_data.columns)

	feature = st.text_input("First, choose which feature shall be the the predicted variable for the model:")

	if feature is not None:
		try:
			l1=LabelEncoder()
			l1.fit(lung_data[[feature]])
			lung_data[feature]=l1.transform(lung_data[feature])
		except KeyError:
			st.error("Please enter a valid input")

	micros = st.number_input("Second, select from which column are the microarrays data:", min_value=0, step=1)

	if micros is not None:
		try:
			size = st.slider("Lastly, select how many data shall be splitted into testing data:", min_value=0.1, max_value=0.5, value=0.3, step=0.01)

			x = lung_data.values[:,micros:]
			y = lung_data[[feature]]

			train_micro, test_micro, train_tipo, test_tipo = train_test_split(x, y, test_size = size, random_state = 12345)

			st.text("The data was standarized substracting the mean and then divided by the standard deviation.  It was first applied to the training data, and then to the testing data using the same parameters used for the training part. The application of the same parameters and not a direct standardization to the testing is important to...")

			norm = StandardScaler()	
			train_micro = norm.fit_transform(train_micro)
			test_micro = norm.transform(test_micro)
		except ValueError:
			st.write("Please insert a valid input")
			st.stop()
		except KeyError:
			st.stop()	

	with modelTraining:
		st.header("Model training")
		st.text("The model selected for this project is a Support Vector Machine due to...")
		st.text("The hyperparameters selected are:")

		st.markdown("* **C:** 0.1 ")
		st.markdown("* **gamma:** 1 ")
		st.markdown("* **kernel:** linear")

		st.text("These parameters were the most optimal due to their high performance results.")

		try:
			svc = SVC(C = 0.1, gamma = 1, kernel = "linear", random_state = 12345)
			svc.fit(train_micro, train_tipo)
			pred = svc.predict(test_micro)
		except NameError:
			st.stop()
			
	with results:
		try:
			st.set_option('deprecation.showPyplotGlobalUse', False)
			st.header("Results")

			class_names = ["tumoral", "normal"]

			st.subheader("Model score:")

			st.write("Accuracy: ", svc.score(test_micro, test_tipo).round(2))
			st.write("Precision: ", precision_score(test_tipo, pred, labels=class_names).round(2))
			st.write("Recall: ", recall_score(test_tipo, pred, labels=class_names).round(2))

			st.subheader("Confusion Matrix") 
			skplt.metrics.plot_confusion_matrix(svc, test_micro, test_tipo, display_labels=class_names)
			st.pyplot()
		        
			st.subheader("ROC Curve") 
			skplt.metrics.plot_roc_curve(svc, test_micro, test_tipo)
			st.pyplot()

			st.subheader("Precision-Recall Curve")
			skplt.metrics.plot_precision_recall_curve(svc, test_micro, test_tipo)
			st.pyplot()
		except NameError:
			st.stop()

