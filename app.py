import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the model
pickle_in = open("classifier.pkl",'rb')
classifier = pickle.load(pickle_in)

def welcome():
        return 'welcome all'

def prediction(Sales_Before, Sales_After, Customer_Satisfaction_Before, Customer_Satisfaction_After, Group_Control,                 Customer_Segment_Low_Value, Customer_Segment_Medium_Value):
        input_data =[[Sales_Before, Sales_After, Customer_Satisfaction_Before, Customer_Satisfaction_After, Group_Control, Customer_Segment_Low_Value, Customer_Segment_Medium_Value]]

        predict = classifier.predict(input_data)
        prediction=predict.astype(int)
        

        return prediction

def main():

        html_temp = """
        <div style="background-color:purple;padding:13px">
        <h1 style="color:red;text-align:center;">Sales data Prediction</div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)

        Sales_Before = st.text_input("Sales_Before", "")
        Sales_After = st.text_input("Sales_After", "")
        Customer_Satisfaction_Before = st.text_input("Customer_Satisfaction_Before", "")
        Customer_Satisfaction_After = st.text_input("Customer_Satisfaction_After", "")
        Group_Control = st.text_input("Group_Control [0-1]", "")
        Customer_Segment_Low_Value = st.text_input("Customer_Segment_Low_Value [0-1]", "")
        Customer_Segment_Medium_Value = st.text_input("Customer_Segment_Medium_Value [0-1]", "")

        if st.button("Predict"):
                try:
                        Sales_Before = float(Sales_Before)
                        Sales_After = float(Sales_After)
                        Customer_Satisfaction_Before = float(Customer_Satisfaction_Before)
                        Customer_Satisfaction_After = float(Customer_Satisfaction_After)
                        Group_Control = float(Group_Control)
                        Customer_Segment_Low_Value = float(Customer_Segment_Low_Value)
                        Customer_Segment_Medium_Value = float(Customer_Segment_Medium_Value)

                        result = prediction(Sales_Before, Sales_After, Customer_Satisfaction_Before, Customer_Satisfaction_After, Group_Control, Customer_Segment_Low_Value, Customer_Segment_Medium_Value)

                        if result == 1:
                                result = "made"
                        else:
                                result = "doesn't made"

                        st.success(f"Customer {result} the purchase")
                except ValueError as e:
                        st.error(f"Error in input values: {e}")

        st.title("Sales Dataset")
        df=pd.read_csv("Sales dataset.csv")
        st.write(df.head(5))

        df_subset=df.head(10)
        fig,axes=plt.subplots(1,2,figsize=(12,6))
        sns.barplot(x='Sales_Before', y='Customer_Satisfaction_Before', data=df_subset, ax=axes[0])
        axes[0].set_title('Sales Before vs Customer Satisfaction Before')

        sns.barplot(x='Sales_After', y='Customer_Satisfaction_After', data=df_subset, ax=axes[1])
        axes[1].set_title('Sales After vs Customer Satisfaction After')

        st.pyplot(fig)

if __name__ == "__main__":
        main()
