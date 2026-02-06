import streamlit as st
import base64


#Placing Bacground Image.

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    page_bg_img = f'''
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_png_as_page_bg('static/background.png')



#TextBox Placement 
input_style = """
<style>
    /* 1. Main container centering */
    [data-testid="stVerticalBlock"] {
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    /* 2. Styling the label with your chosen font/color */
    label[data-testid="stWidgetLabel"] p {
        font-family: 'Comic Sans MS', cursive, sans-serif; 
        font-size: 24px !important;                      
        font-weight: bold;                               
        color: #FF8C00;                                  
        display: flex;
        justify-content: center;
    }

    /* 3. Adjusting the width of the input box */
    div[data-testid="stTextInput"] {
        width: 100%;
        max-width: 450px;
        margin: 0 auto;
    }

    /* 4. Centering the success message text */
    div[data-testid="stNotification"] {
        display: flex;
        justify-content: center;
        width: max-content;
        margin: 10px auto;
    }
</style>
"""

st.markdown(input_style, unsafe_allow_html=True)

# 5. Using columns to keep horizontal center
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.write("##") 
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")

    name = st.text_input("Type in all your names, even the middle ones!", placeholder="Full Name")
    age = st.text_input("Age Also!", placeholder="Age")
    
    if st.button("Submit"):
        st.success(f"WELCOME ! {name.title()}")

