import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Welcome to My Portfolio Apps Site!!😄")
st.write("🍏😺🍏🐈🍏🐾🍏🐱🍏🐈🍏🐾🍏😸🍏🐈🍏🐾🍏😽🍏🐈🍏🐾🍏😹🍏🐈🍏🐾🍏😺🍏🐈🍏🐾🍏🐱🍏🐈🍏🐾🍏😸🍏🐈🍏🐾🍏😽🍏🐈🍏🐾🍏😹🍏🐈🍏")
st.write("")

column_1, column_2 = st.columns(2)

with column_1:
    st.image("images/ten_and_my_face.jpg")

with column_2:
    st.header("Takiko Miyabori")
    content = """
    I am looking for a chance to work as a Python programmer! Why? 
    Because programmers can work fully remotely and on flextime. In this way, I can be with my cat, Tenka, all the time😊
    
    I hope you like my portfolio website (this website:-)) and apps 💗
    """
    st.info(content)

content2 = """
There are 20 project icons below, however, currently I've finished four projects; 1) Todo App, 2) Portfolio Website (this one:-)), 3) PDF Templates, and 4) PDF Invoices.
I haven't started other projects, but if there is any project you want to see how I can do it, you can drop me a message from the Contact Me shown in the left pane to let me know:)
"""
# st.text(content2) # This was my solution!
st.write(content2)

column_3, empty_column, column_4 = st.columns([1.5, 0.5, 1.5])

dataframe = pandas.read_csv("data.csv", sep=";")

with column_3:
    for index, row in dataframe[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with column_4:
    for index, row in dataframe[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")




