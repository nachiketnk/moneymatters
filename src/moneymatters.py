import streamlit as st
from millify import millify
from millify import prettify

def calculated_compounded_return(principal, exp_return, tenor, compounded):
    amount = principal*(pow((1+exp_return/compounded),compounded*tenor))
    return amount



st.title("Welcome to Money Matters")

st.subheader("We dedicate this site to help you understand the power of investing, compounding and getting the most band for your buck")


#st.caption('Let us start with a  _compounding_ as a :blue[classic] example :sunglasses:')

st.header("What Is Compounding?")
st.subheader("Compounding is the process in which an asset’s earnings, from either capital gains or interest, are reinvested to generate additional earnings over time.") 
             
st.subheader("One off investment growth of money = Linear")
st.subheader("Compounding growth of money = Exponential")

tab1, tab2, tab3 = st.tabs(["Compounding", "Linear", "Mixed"])

with tab1:
   st.header("Magic of compounding")
   principal = st.number_input(label="Initial capital", min_value=0, max_value=100000, step=1000, value=1000)
   #exp_return = st.number_input(label="Expected Annual Return", min_value=0.00,max_value=100.00, step=0.5)
   exp_return = st.slider('Expected Annual Return?', 1, 10, 4)
   exp_return = exp_return/100
   
   #monthly_addition = st.number_input(label="Monthly investment", min_value=100, max_value=10000, step=100)
   born = st.slider('When were you born?', 1950, 2050, 1985)
   retirement_age = st.slider('When do you want to retire?', 30, 100, 60)
   tenor =  abs(2023 - (born + retirement_age))
   st.caption(tenor)
   amount = calculated_compounded_return(principal, exp_return, tenor, 1)
   st.write("By the year",born + retirement_age,"you will have amount" )
   st.subheader(prettify(int(amount),   separator="'"))


st.divider()

st.caption("We are interested in sharing the knowledge. No data is collected")


