import streamlit as st
import pandas as pd
import joblib
import json

# load model
with open('pipeline.pkl', 'rb') as file_1:
    pipeline = joblib.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
    list_num_cols = json.load(file_2)

with open('list_cat_cols.txt', 'r') as file_2:
    list_cat_cols = json.load(file_2)


# Run function stelah loading
def run():
    with st.form(key='Heart Disease Prediction Form'):
        age = st.number_input('Age', min_value=16, max_value=60, value=25, step=1, help='Patient Age')
        anaemia = st.radio('anaemia', ('Yes', 'No'), help='Anemia Status')
        creatinine_phosphokinase = st.number_input('creatinine_phosphokinase', min_value=22, max_value=334, value=70)
        diabetes = st.radio('diabetes', ('Yes', 'No'), help='Diabetes Status')
        ejection_fraction = st.number_input('Ejection Fraction', min_value=0, max_value=1000000000000000, value=0)
        high_blood_pressure = st.radio('high_blood_pressure', ('Yes', 'No'), help='Hypertension Status')
        platelets = st.number_input('Platelets', min_value=0, max_value=1000000000000000, value=0)
        serum_creatinine = st.number_input('Serum Creatinine', min_value=0, max_value=1000000000000000, value=0)
        serum_sodium = st.number_input('Serum Sodium', min_value=0, max_value=1000000000000000, value=0)
        sex = st.radio('sex', ('Male', 'Female'))
        
        smoking = st.radio('smoking', ('Yes', 'No'), help='Smoker Status')
        time = st.number_input('Follow up', min_value=0, max_value=1000000000000000, value=0)
        st.markdown('---')

        sex_dict = {'Male': 1, 'Female': 0}
        sex = sex_dict[sex]

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'age': age,
        'anaemia': anaemia,
        'creatinine_phosphokinase': creatinine_phosphokinase,
        'diabetes': diabetes,
        'ejection_fraction': ejection_fraction,
        'high_blood_pressure': high_blood_pressure,
        'platelets': platelets,
        'serum_creatinine': serum_creatinine,
        'serum_sodium': serum_sodium,
        'sex' : sex,
        'smoking': smoking,
        'time': time        
    }   

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Create a dictionary to map radio button choices to integer values
        radio_dict = {'Yes': 1, 'No': 0}

        # Loop through categorical columns and update the values in data_inf DataFrame
        for col in list_cat_cols:
            data_inf[col] = data_inf[col].map(radio_dict)
            # Predict using LinReg
        
        
        y_pred_inf = pipeline.predict(data_inf)

        if y_pred_inf.any() == 1:
            st.write('You potentially will die from a heart failure, consult to your doctor!')
        else:
            st.write('You probably safe from heart failure, keep healthy!')


# calling function
if __name__ == '__main__':
   run()