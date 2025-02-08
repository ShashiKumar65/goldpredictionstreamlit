# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:25:05 2025

@author: shashikumar
"""

import pickle
import streamlit as st
model=pickle.load(open(r"gold_model.sav",'rb'))
def main():
    st.title("Gold Prediction App")
    spx=st.number_input("SPX")
    uso=st.number_input("USO")
    slv=st.number_input("SLV")
    EUR_USD=st.number_input("EUR/USD")
    if st.button("Predict"):
        input_lst=[spx,uso,slv,EUR_USD]
        pred=model.predict([input_lst])
        st.success(pred)
if __name__=="__main__":
    main()