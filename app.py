# Import necessary libraries
from ocr_imgs.ocr import OCRProcessor
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import google.generativeai as genai
import os
from llm_models.google_gemini.gemini_pro import html_generation
from dotenv import load_dotenv
from logs import logger
# Load environment variables from .env file
load_dotenv()

# Configure Google API key for generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

logger.info("********* PenPalSite started *************")
# Function to perform OCR on the uploaded image
def ocr_func(img):
    # Initialize OCRProcessor
    ocr_processor = OCRProcessor()
    # Extract layout from the image
    layout = ocr_processor.extract_layout(img)
    logger.info(f" layout ----{layout}")
    return layout


# Initialize Streamlit session state variables
if "html" not in st.session_state:
    st.session_state.html = ""
if "image" not in st.session_state:
    st.session_state.image = ''


# Function to process uploaded image and generate HTML code
def image_run():
    html_code = ""
    layout = ocr_func(st.session_state.image)
    if layout != []:
        # Generate HTML code from layout
        html_code = html_generation(layout)

    # Store generated HTML code in session state
    st.session_state.html = html_code
    st.session_state.image = st.session_state.image


# Set Streamlit page title
st.markdown("<h1 style='text-align: center;'>Welcome to PenPalSite 📄</h1>",
            unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:red;'>Transform Your Ideas into Stunning Websites: Introducing Sketch-to-Site, Your Ultimate Web Design Companion</h5>",
            unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Design to Website App</h2>",
            unsafe_allow_html=True)
# Create tabs for different sections
t1, t2, t3 = st.tabs(['Upload an image', 'Output', " Generated code"])

# Upload an image section
with t1:
    # File uploader for image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg",
                                                              "png",
                                                              "jpeg"])

    # If image is uploaded
    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image",
                 use_column_width=True)

        # Save the uploaded image
        image_filename = uploaded_file.name
        image = Image.open(uploaded_file)
        file_name_with_path = "temp_files/"+image_filename
        image.save(file_name_with_path)
        st.session_state.image = file_name_with_path

        # Button to generate code from the uploaded image
        convert_to_html = st.button("Generate code", on_click=image_run)
        if convert_to_html:
            st.balloons()
            st.success("Uploaded image converted into website")
            st.info("Click on Output tab to view")

# Output section
with t2:
    if st.session_state.html != '':
        # Display the generated HTML output
        with st.container():
            components.html(st.session_state.html,
                            width=700,
                            height=650,
                            scrolling=True)
            st.write("Click on Generated code tab to see the code")

# Generated code section
with t3:
    if st.session_state.html != '':
        # Display the source code generated
        with st.expander("See source code"):
            st.code(st.session_state.html)

        st.download_button(
            label="Download data as html",
            data=st.session_state.html,
            file_name='Generate_html.html'
        )
