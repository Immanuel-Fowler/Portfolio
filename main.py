import streamlit as st

def get_logo(name):
    if name == "Accenture North America - Data Analytics and Visualization":
        return "images/accenture_logo_white.svg"
    if name == "CBRE - Project Management":
        return "images/CBRE_logo.png"
    if name == "Google Analytics":
        return "images/goole_logo.png"
    if name == "Skyscanner Front-End Software Engineering":
        return ("images/Skyscanner_logo.png")
    if name =="Dupont":
        return("images/dupont_logo.png")
    if name =="Rocket Mortgage":
        return("images/rocket_mortgage_logo.png")
    if name == "Zeta Learning":
        return("images/zetaLearning_logo.jpeg")

    return ("images/goole_logo.png")


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":robot:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Immanuel :wave:")
    st.title("An aspiring Software Engineer & Data Scientist")
    st.write(
        "I am passionate about finding ways to use data to solve problems and help people."
    )
    st.write(
        "[Find me on linkedin here >](https://www.linkedin.com/in/immanuel-fowler-59480b1b5/)"
    )

# ---- WHAT I DO SECTION ----

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader(
            "**I am currently researching at University of Delaware in collaboration with NASA through the Delaware Space Observation Center :rocket:**"
        )
        st.write("""
            - Developing a payload to participate in the NASA RockSat-C Mission
            - Programming and Engineering micro-controllers and SBC's to be launched into space
            - Apply advanced and semi-automated Data Analysis of data recovered from space

            If this sounds interesting to you connect with me on LinkedIn and let's talk!
            """)
    with right_column:
        st.image("images/website_pic.jpeg", width=300)

# ---- CURRENT CERTIFICATIONS SECTION ----

certifications = [
    [
        "Accenture North America - Data Analytics and Visualization",
        "Learned how to use tools such as Power BI, Excel Spreadsheets and Power Point to effectivley visualize and analyze data for a coporate audience",
        "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Accenture%20North%20America/hzmoNKtzvAzXsEqx8_Accenture%20North%20America_CoHTn6ywugE2wRRXv_1710292872703_completion_certificate.pdf"
    ],
    [
        "CBRE - Project Management",
        "Gained familiarity with project managements techniques and tools such as gaants charts and project process terminology",
        "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/CBRE/STkypM8iMfn4Gk9BF_CBRE_CoHTn6ywugE2wRRXv_1710278558564_completion_certificate.pdf"
    ],
    [
        "Google Analytics",
        "Gained familiarity with Google Analytics tools and techniques such as Google Analytics, Google Tag Manager, Google Analytics",
        "https://skillshop.credential.net/2ba2f66c-4f2c-45c9-9252-7d3084c37371"
    ],
    [
        "Skyscanner Front-End Software Engineering",
        "Gained familiarity with React JS, HTML/CSS/Javascript, andFront end development techniques/methodlodigies",
        "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Skyscanner/km4rw7dihDr3etqom_Skyscanner_CoHTn6ywugE2wRRXv_1710467856568_completion_certificate.pdf"
    ]
]

with st.container():
    st.write('---')
    st.subheader("Here are my current certifications:")
    st.write("##")

    for cert in certifications:
        image_column, text_column = st.columns((1, 2))
        image_column.image(get_logo(cert[0]))
        cert_link = "[Find my certification here >](" + cert[2] + ")"
        with text_column:
            st.subheader(cert[0])
            st.write(cert[1])
            st.write(cert_link)

# ---- INTERNSHIPS SECTION ----

internships = [
    [
        "Dupont",
        "At Dupont I worked with Power BI, Power Apps, and Power Automate to create a centralized data metrics system for the contract administration department of two of their Delaware Sites"
    ],
    [
        "Rocket Mortgage",
        "At Rocket Mortgage I programmed with C# and Angular on the .NET framework to refactor code and impliment new features to production pipline to withstand code mutation"
    ],
    [
        "Zeta Learning",
        "At Zeta Learning I developed using swift and figma to revise and improve the user experience of the Zeta Learning platform"
    ]
]

with st.container():
    st.write('---')
    st.subheader("Here are some of my internships:")
    st.write("##")

    for x in internships:
        image_column, text_column = st.columns((1, 2))
        image_column.image(get_logo(x[0]))
        image_column.write("##")
        with text_column:
            st.subheader(x[0])
            st.write(x[1])
            st.write('##')
