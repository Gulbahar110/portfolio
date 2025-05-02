import streamlit as st
import requests
# from streamlit import st_lottie 
from streamlit_lottie import st_lottie

import streamlit.components.v1 as components

st.set_page_config(layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/d44771d4-bd2c-4da2-9c42-c87c93e72783/SXVqCQcgWi.json")
lottie_coder_1 = load_lottieurl("https://lottie.host/59347f30-0993-4763-808d-7b5ca4ee5cbf/rNgQ7iGqVv.json")
lottie_code = load_lottieurl("https://lottie.host/395ebff1-1504-46e5-a0b5-2b35d123f9fd/JVIy1OKDBA.json")
lottie_code_2 = load_lottieurl("https://lottie.host/d6fbbbbb-9b13-483a-8fce-5539c314bb5a/NKKuzUegFk.json")


if "role" not in st.session_state:
    st.session_state.role = None
ROLES = ["Admin"]

def login():
    
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)
    if st.button("Log in"):
        st.session_state.role = role
        
def logout():
    st.session_state.role = None
    st.rerun()

role = st.session_state.role

def admin_dashboard():
    st.subheader("Hey Guys :wave:")
    st.title("My Portfolio Website")
    st.subheader("Introduction")
    st.write("----- ")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hello,")
            st.title("I'm Gulbahar Ali !")
            st.subheader("BS artificail inteligance student university of sindh jamshoro' AI2k24 Batch ")
            st.write("I am a motivated and dedicated university student with a strong passion for artificial intelligence (AI) and machine learning (ML).My interests include Artificial Intelligence,Machine Learning,Computer Vision and Natural Language Processing .")
            st.write("")
            with open("portfolio.py", "r") as file:
                resume_data = file.read() 
            st.download_button(label="Download Resume", data=resume_data, file_name="portfolio.py")
        st.header("Wants to Know More About Me ?")
        st.text_input("Ask Anything About Me !!")
        with col2:
            st_lottie(lottie_coder)

    st.title("Skills !!!")
    st.write("-----")
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Here,            
            - Technologies:
                - Machine Learning, Deep learning, NLP,Backend Developer
                         
            - Languages:
                - Python, C, C++, Java, SQL, Bash html 

            - Frameworks:
                - TensorFlow, Scikit, NLTK, SpaCy, Keras, Flask, Sreamlit, Java Swing, Springboot 
                         
            - Soft Skills:
                - Leadership, Creativity, Writing, Public Speaking, Time Management, Problem Solving, Communications
            """)

        with col4:
            st_lottie(lottie_coder_1) 

    with st.container():
        st.title("Projects !!!")
        st.write("-----")
        col5, col6 = st.columns([1,1])
        with col5:
            st.write("##")
            st.subheader("What2Watch")
            st.image("download.png", width=300)
            st.write("A web application that will provides you the recommendation of the movies that are similar to the ones you have been watched in the past. Also it provides many interesting facts about the movies and moviemakers.")
        
        with col6:
            st.write("##")
            st.subheader("NewlifyStudio")
            st.image("download.png", width=300)
            st.write("A web application that will provides you the recommendation of the movies that are similar to the ones you have been watched in the past. Also it provides many interesting facts about the movies and moviemakers.")
    
    with st.container():
        col7, col8 = st.columns(2)
        with col7:
            st.write("##")
            st.subheader("TrendyNews")
            st.image("download.png", width=300)
            st.write("A web application that will provides you the recommendation of the movies that are similar to the ones you have been watched in the past. Also it provides many interesting facts about the movies and moviemakers.")

        with col8:
            st.write("##")
            st.subheader("PolygonAreaCalculator")
            st.image("download.png", width=300)
            st.write("A web application that will provides you the recommendation of the movies that are similar to the ones you have been watched in the past. Also it provides many interesting facts about the movies and moviemakers.")
    
    with st.container():
        st.title("Research Works And Publications !!!")
        st.write("---")
        st.write("##")
        col9, col10 = st.columns(2)
        with col9:
            st.write("""
            - Object Detection for Autonomous Vehicle in Hazy Environment using Optimized Deep Learning Techniques. (Implemented the Dark Channel Prior algorithm for Dehazing the frames of the video.) 
            """)
            st.write("""
            - Implemented the multiple pair SMO (MP-SMO), a new solution for the SMO algorithm that consists of optimizing more than one pair of coefficients per iteration simultaeously. We show that MP-SMO enhances the performance of the SMO algorithm compared to other existing solutions. 
            """)
        with col10:
            st_lottie(lottie_code)

    with st.container():
        st.title("Achievements !!!")
        st.write("---")
        st.write("##")
        st.markdown("""
        <ul style='font-size:18px'>
        <li><b>Secured All India Rank of 62 in Amazon ML Challenge'23 among 4k+ teams.</b></li>
                <br>
        <li><b>Secured All India Rank of 12 in MSCI Developer Challenge India 2022 among 5k+ candidates.</b></li><br>
        <li><b>Selected for Amazon Machine Learning Summer School 2022 among 10k+ candidates.</b></li><br>
        <li><b>Secured All India Rank of 59 in Football Hackathon – 'Data-Driven Player Performance Assessment' on Machine Learning among 4500+ registered candidates.</b></li>
        </ul>
        """, unsafe_allow_html=True)
    

    st.title("Services !!!")
    st.write("---")
    st.write("##")
    st.markdown("""
    <ul style='font-size:22px'>
        <li><b>Experience AI Solutions: Transforming Your Ideas into Reality</b></li>
    </ul>
    """, unsafe_allow_html=True) 
    st.write("At our AI Solutions, we specialize in turning your ideas into powerful AI solutions. Whether you have a specific problem to solve or a concept to bring to life, we're here to help. With advanced algorithms and data-driven approaches, we create intelligent systems, predictive models, and data analytics solutions. Unleash the potential of your ideas with our tailored AI solutions. Let's collaborate and make your vision a reality.")
    st.markdown("""
    <ul style='font-size:18px'>
        <b>For more Get in touch with me.</b>
    </ul><br>
    """, unsafe_allow_html=True) 
    st.markdown("""
    <ul style='font-size:22px'>
        <li><b>Book a Meeting : Let's Discuss Your Ideas and Plan for Success</b></li>
    </ul>
    """, unsafe_allow_html=True) 
    st.write("Have a groundbreaking idea that's ready to take the world by storm? Let's connect! We invite you to schedule a meeting with our team to discuss your innovative concept. We're passionate about exploring new possibilities and turning visionary ideas into reality through cutting edge AI solutions.")
    st.markdown("""
    <ul style='font-size:18px'>
        <b>Don't let your idea go untapped — schedule a meeting with us today and let's change the tomorrow .   </b>
    </ul><br>
    """, unsafe_allow_html=True) 

    with st.container():
        st.title("Get In Touch With Me!")
        st.write("---")
        st.write("##")
        col11, col12 = st.columns(2)
        with col11:
            name=st.text_input("Name", placeholder="Your Full Name")
            email=st.text_input("Email", placeholder="Your Email Address") 
            if email:
                if "@" in email and "." in email:
                    st.success("Valid Email")
                    
                else:
                    st.error("Please enter a valid email address.")
            st.text_area("Type Your Message", placeholder="Message", height=400)
            st.button("Send")
        with col12:
            st_lottie(lottie_code_2)

        
        
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")


admin_1 = st.Page(
    admin_dashboard,
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)

account_pages = [logout_page]
admin_pages = [admin_1]

page_dict = {}
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
