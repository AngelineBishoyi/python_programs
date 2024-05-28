'''import streamlit as st
from PIL import Image
st.title("Welcome to streamlit")
st.header("Machine Learning")
st.subheader("Linear Regression")
st.info("Info details")
st.warning("Come on time")
st.error("Wrong password")
st.success("Congrats!!")
st.write("Employee ")
st.markdown("# Miracle")
st.markdown(":cat:")
st.caption("Here is the caption")
st.latex(r)
st.image(r"C:\Users\abishoyi\function\download.jpg")
#widgets
st.checkbox("Im cute little Panda")
st.button("Click me")
st.radio("Pick the panda",["cute","Beautiful","bad"])
st.selectbox("pick your course",['ML',"python",'data science'])
st.multiselect("Choose the department",['content','sales','marketing'])
st.select_slider("Rating",['good','bad','excellent'])
st.slider("Enter the number",0,100)
st.number_input("pick a number",0,100)
st.text_input("Enter your email ddress")
st.date_input("Opening ceremony")'''


'''st="hello world python"
x=0
while x<len(st):
    if st[x]==0:
        print(st[x].upper() ,end='')
        x=+1
    elif st[x]=="":
        print(st[x+1].upper(),end="")
        x=+2
    else:
        print(st[x],end="")'''

st='tutorjoes'
l={}
for i in st:
    l[i]=l.get(i,0)+1
print(l)
