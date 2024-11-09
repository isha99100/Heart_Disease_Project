# import streamlit as st
# import pickle

# # Set up the page configuration
# st.set_page_config(
#     layout="centered",
#     initial_sidebar_state="auto",
#     page_title="Heart Disease Prediction",
#     page_icon=None,
# )

# # Load the custom CSS for styling
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# # Load the trained machine learning model
# model = pickle.load(open('model.sav', 'rb'))

# # Title and description of the app
# st.title("Heart Disease Prediction using Machine Learning")
# st.text("Enter the patient's information to predict the likelihood of heart disease.")

# # Create input fields for user data
# col1, col2, col3 = st.columns(3)

# with col1:
#     age = st.number_input('Age', min_value=1, step=1)

# with col2:
#     sex = st.radio("Sex", ('M', 'F'))
#     sex = 1 if sex == 'M' else 0

# with col3:
#     cp = st.number_input('Chest Pain types', min_value=0, max_value=3, step=1)

# with col1:
#     trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, step=1)

# with col2:
#     chol = st.number_input('Serum Cholesterol in mg/dl', min_value=20, max_value=300, step=1)

# with col3:
#     fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1, step=1)

# with col1:
#     restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, step=1)

# with col2:
#     thalach = st.number_input('Maximum Heart Rate achieved', min_value=50, max_value=220, step=1)

# with col3:
#     exang = st.number_input('Exercise Induced Angina', min_value=0, max_value=1, step=1)

# with col1:
#     oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, step=0.1)

# with col2:
#     slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1)

# with col3:
#     ca = st.number_input('Major vessels colored by fluoroscopy', min_value=0, max_value=3, step=1)

# with col1:
#     thal = st.selectbox('Thalassemia', ('normal', 'fixed', 'defect'))
#     thal = {'normal': 0, 'fixed': 1, 'defect': 2}[thal]

# # Prepare the input data for prediction
# input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

# # Button to get the diagnosis
# if st.button('Get the diagnosis'):
#     prediction = model.predict(input_data)
#     if prediction[0] == 1:
#         diagnosis = 'The person is having heart disease'
#     else:
#         diagnosis = 'The person does not have any heart disease'
#     st.success(diagnosis)
    
# import streamlit as st
# import pickle
# import matplotlib.pyplot as plt  # Import matplotlib.pyplot for creating plots

# # Set up the page configuration
# st.set_page_config(
#     layout="centered",
#     initial_sidebar_state="auto",
#     page_title="Heart Disease Prediction",
#     page_icon=None,
# )

# # Load the trained machine learning model
# model = pickle.load(open('model.sav', 'rb'))

# # Initialize variables for user input
# age = None
# sex = None
# cp = None
# trestbps = None
# chol = None
# fbs = None
# restecg = None
# thalach = None
# exang = None
# oldpeak = None
# slope = None
# ca = None
# thal = None

# # Title and description of the app
# st.title("Heart Disease Prediction using Machine Learning")
# st.text("Enter the patient's information to predict the likelihood of heart disease.")

# # Create input fields for user data
# col1, col2, col3 = st.columns(3)

# with col1:
#     age = st.number_input('Age', min_value=1, step=1, value=age)

# with col2:
#     sex = st.radio("Sex", ('M', 'F'), index=0 if sex is None else 0 if sex == 'M' else 1)
#     sex = 1 if sex == 'M' else 0

# with col3:
#     cp = st.number_input('Chest Pain types', min_value=0, max_value=3, step=1, value=cp)

# with col1:
#     trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, step=1, value=trestbps)

# with col2:
#     chol = st.number_input('Serum Cholesterol in mg/dl', min_value=20, max_value=300, step=1, value=chol)

# with col3:
#     fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1, step=1, value=fbs)

# with col1:
#     restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, step=1, value=restecg)

# with col2:
#     thalach = st.number_input('Maximum Heart Rate achieved', min_value=50, max_value=220, step=1, value=thalach)

# with col3:
#     exang = st.number_input('Exercise Induced Angina', min_value=0, max_value=1, step=1, value=exang)

# with col1:
#     oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, step=0.1, value=oldpeak)

# with col2:
#     slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1, value=slope)

# with col3:
#     ca = st.number_input('Major vessels colored by fluoroscopy', min_value=0, max_value=3, step=1, value=ca)

# with col1:
#     thal = st.selectbox('Thalassemia', ('absent','normal', 'fixed', 'defect'), index=0 if thal is None else thal)
#     thal = {'absent':0,'normal': 1, 'fixed': 2, 'defect': 3}[thal]

# # Button to get the diagnosis
# if st.button('Get the diagnosis'):
#     prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
#     if prediction[0] == 1:
#         diagnosis = 'The person is having heart disease'
#     else:
#         diagnosis = 'The person does not have any heart disease'
#     st.success(diagnosis)
# # 
# # Display graph showing input values and prediction result
#     st.subheader("Input Values and Prediction Result Visualization")
#     labels = ['Age', 'Sex', 'Chest Pain', 'Resting BP', 'Cholesterol', 'Fasting BS', 
#               'Resting ECG', 'Max HR', 'Exercise Angina', 'ST Depression', 'Peak Slope', 
#               'Num Vessels', 'Thalassemia','Prediction']
#     user_values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
#     user_values.append(prediction[0])  # Append the prediction result to user values
#     fig, ax = plt.subplots(figsize=(10, 6))
#     ax.barh(labels, user_values, color=['lightblue']*len(labels) + ['orange'])
#     ax.set_xlabel('Value')
#     ax.set_title('Input Values and Prediction Result')
#     st.pyplot(fig)
import streamlit as st
import pickle
import matplotlib.pyplot as plt

# Set up the page configuration
st.set_page_config(
    layout="centered",
    initial_sidebar_state="auto",
    page_title="Heart Disease Prediction",
    page_icon=None,
)

# Load the trained machine learning model
model = pickle.load(open('model.sav', 'rb'))

# Initialize variables for user input
age = None
sex = None
cp = None
trestbps = None
chol = None
fbs = None
restecg = None
thalach = None
exang = None
oldpeak = None
slope = None
ca = None
thal = None

# Title and description of the app
st.title("Heart Disease Prediction using Machine Learning")
st.text("Enter the patient's information to predict the likelihood of heart disease.")

# Create input fields for user data
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=1, step=1, value=age)

with col2:
    sex = st.radio("Sex", ('M', 'F'), index=0 if sex is None else 0 if sex == 'M' else 1)
    sex = 1 if sex == 'M' else 0

with col3:
    cp = st.number_input('Chest Pain types', min_value=0, max_value=3, step=1, value=cp)

with col1:
    trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, step=1, value=trestbps)

with col2:
    chol = st.number_input('Serum Cholesterol in mg/dl', min_value=20, max_value=300, step=1, value=chol)

with col3:
    fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', min_value=0, max_value=1, step=1, value=fbs)

with col1:
    restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, step=1, value=restecg)

with col2:
    thalach = st.number_input('Maximum Heart Rate achieved', min_value=50, max_value=220, step=1, value=thalach)

with col3:
    exang = st.number_input('Exercise Induced Angina', min_value=0, max_value=1, step=1, value=exang)

with col1:
    oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, step=0.1, value=oldpeak)

with col2:
    slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1, value=slope)

with col3:
    ca = st.number_input('Major vessels colored by fluoroscopy', min_value=0, max_value=3, step=1, value=ca)

with col1:
    thal = st.selectbox('Thalassemia', ('absent','normal', 'fixed', 'defect'), index=0 if thal is None else thal)
    thal = {'absent':0,'normal': 1, 'fixed': 2, 'defect': 3}[thal]

# Button to get the diagnosis
if st.button('Get the diagnosis'):
    # Prepare the input data for prediction
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

    # Perform prediction
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        diagnosis = 'The person is predicted to have heart disease'
    else:
        diagnosis = 'The person is predicted to not have heart disease'
    st.success(diagnosis)

    # Prepare labels and values for visualization
    labels = ['Age', 'Sex', 'Chest Pain', 'Resting BP', 'Cholesterol', 'Fasting BS', 
              'Resting ECG', 'Max HR', 'Exercise Angina', 'ST Depression', 'Peak Slope', 
              'Num Vessels', 'Thalassemia']
    user_values = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    # Create a horizontal bar plot for visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(labels, user_values, color='lightblue')
    ax.set_xlabel('Value')
    ax.set_title('Input Values')
    
    # Add annotation for each bar
    for i, v in enumerate(user_values):
        ax.text(v + 0.1, i, str(v), color='black', va='center')

    # Highlight the predicted diagnosis with a different color
    if prediction[0] == 1:
        ax.barh('Prediction', 1, color='orange')
    else:
        ax.barh('Prediction', 0, color='orange')

    # Add legend and display the plot
    ax.legend(['Input Values', 'Prediction'])
    st.pyplot(fig)
