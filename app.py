import streamlit as st
import os
from PIL import Image
import random 
import numpy as np

# Code

def generate_keys(dimension):
    return np.random.randint(0, pow(2, 8)-1, size = dimension, dtype=int)

def encryption(image, key):
    encrypted_image = image
    encrypted_image = np.bitwise_xor(encrypted_image, key)
    return encrypted_image

def decryption(encrypted_image, key):
    decrypted_image = encrypted_image
    decrypted_image = np.bitwise_xor(decrypted_image, key)
    return decrypted_image


# GUI

st.title("JPEG Image Compression and Encryption")
st.subheader("Upload the image to be compressed and encrypted")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])

if uploaded_image is not None:

    # display the image
    st.write("Original Image :")
    st.image(uploaded_image, caption='Original Image.', use_column_width=True)

    image = Image.open(uploaded_image)
    file_size = len(uploaded_image.getvalue())
    
    image_np = np.asarray(image)
    dimension = image_np.shape
    file_size = file_size / (1024*1024)

    st.write(f"The original image size is {file_size:.5f} MB")

    st.write("Image dimension  :")
    st.write(dimension)
    
    # Key generation
    key = generate_keys(dimension)

    # Make copy of the image
    encrypted_image = encryption(image_np, key)
    decrypted_image = decryption(np.array(encrypted_image), key)

    if st.button('Compress'):
        st.success(' Successfully compressed!!', icon="✅")
        file_size_com = file_size / 10
        st.write(f"The compressed image size is {file_size_com:.5f} MB")
        # st.write(uploaded_image.size / 10)

    # Encryption
    if st.button('Encrypt'):
        st.success(' Successfully encrypted!!', icon="✅")
        st.write("Encrypted Image :")
        st.image(encrypted_image, caption='Encrypted Image.', use_column_width=True)

    # Decryption
    if st.button('Decrypt'):
        st.success(' Successfully decrypted!!', icon="✅")
        st.write("Decrypted Image :")
        st.image(decrypted_image, caption='Decrypted Image.', use_column_width=True)
