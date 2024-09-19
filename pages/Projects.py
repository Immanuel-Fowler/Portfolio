import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from Home import get_logo

# ---- current Projects Section----

projects = [
    [
        "Streamlit Portfolio Website",
        "This is a fun project that will remain ongoing that allows to me gain familiartiy with one of my favorite python libraries. Streamlit is a great library for spinning up aesthetically pleasing data science projects. It is also a low effort library/framework to design webapps/websites",
        "https://github.com/Immanuel-Fowler/Portfolio"
    ],
    [
        "Neural Network Builder",
        "This is an on going project that requires me learning the fundamentals of AI and data science. I hope to create a drag and drop neural netowrk builder.",
        "https://github.com/Immanuel-Fowler/"
    ]
]

with st.container():
    st.write('---')
    st.subheader("Here are my current projects:")
    st.write("##")

    for project in projects:
        image_column, text_column = st.columns((1, 2))
        image_column.image(get_logo(project[0]))
        project_link = "[Click here for the code >](" + project[2] + ")"
        with text_column:
            st.subheader(project[0])
            st.write(project[1])
            st.write(project_link)


