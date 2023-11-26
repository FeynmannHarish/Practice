import streamlit as st
import pickle

c=0
a = st.button("Click me")
d=st.empty()
if a:
    try:
        with open('a',"rb") as f:
            c=pickle.load(f)
        d.text(str(c))

        c+=1
        with open('a',"wb") as f:
            pickle.dump(c,f)
    except:
        d.text(str(c))
        c+=1
        with open('a',"wb") as f:
            pickle.dump(c,f)

    