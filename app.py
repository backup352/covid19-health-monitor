%%writefile app.py
import streamlit as st
import pandas as pd

st.title('COVID-19 Health Monitoring and Symptom Tracker')

# Upload the dataset
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    # Display the uploaded data
    st.write("Uploaded Data:")
    st.write(data)

    # Symptom Tracking Interface
    st.header('Symptom Tracker')
    name = st.text_input('Name')
    date = st.date_input('Date')

    # Example symptoms: Fever, Cough, Fatigue, etc.
    symptoms = {
        'Fever': st.slider('Fever (0-10)', 0, 10, 0),
        'Cough': st.slider('Cough (0-10)', 0, 10, 0),
        'Fatigue': st.slider('Fatigue (0-10)', 0, 10, 0),
        'Shortness of Breath': st.slider('Shortness of Breath (0-10)', 0, 10, 0),
        'Loss of Taste/Smell': st.slider('Loss of Taste/Smell (0-10)', 0, 10, 0)
    }

    # Health Score Calculation Function
    def calculate_health_score(symptoms):
        total_symptoms = sum(symptoms.values())
        max_score = len(symptoms) * 10
        health_score = ((max_score - total_symptoms) / max_score) * 100
        return health_score

    health_score = calculate_health_score(symptoms)
    st.write(f'Health Score: {health_score:.2f}')

    # Custom Alerts and Notifications
    if health_score < 50:
        st.warning('Health Alert: Your health score is low. Please seek medical attention.')
    elif health_score < 75:
        st.info('Health Alert: Your health score is moderate. Monitor your symptoms closely.')
    else:
        st.success('Health Alert: Your health score is good. Keep monitoring your health.')

    # Personalized Guidance
    if health_score < 50:
        st.write('Please visit the nearest healthcare center immediately.')
    elif health_score < 75:
        st.write('Stay hydrated, get plenty of rest, and monitor your symptoms closely.')
    else:
        st.write('Keep up the good health practices. Maintain social distancing and wear a mask.')

    if st.button('Submit'):
        new_entry = {
            'Name': name,
            'Date': date,
            'Fever': symptoms['Fever'],
            'Cough': symptoms['Cough'],
            'Fatigue': symptoms['Fatigue'],
            'Shortness of Breath': symptoms['Shortness of Breath'],
            'Loss of Taste/Smell': symptoms['Loss of Taste/Smell'],
            'Health Score': health_score
        }
        data = data.append(new_entry, ignore_index=True)
        data.to_excel("updated_dataset.xlsx", index=False)
        st.success('Entry added successfully!')

    st.write('Updated Data:')
    st.write(data)

else:
    st.write("Please upload a dataset to proceed.")
