import streamlit as st
st.title("Hello, guest")
st.header("We have a lot of cats here.")
st.subheader("eg, DesertCat")
st.text("It's extremely adorable.")

st.markdown("this is an image of DesertCat: \n \
            ![](https://ts1.cn.mm.bing.net/th?id=OIP-C.ZT7LRblrDj2z7F2Tfv-lhAAAAA&w=201&h=310&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
               ['Feeding cat strips',
                'Grooming a cat',
                'Playing with a cat',
                'Feeding a kitten milk'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    
