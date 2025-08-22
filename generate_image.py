import streamlit as st
import keras_cv
from tensorflow import keras

# Initialize the model
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

# Streamlit UI
st.title("🖌️ Text-to-Image Generator with Stable Diffusion")
prompt = st.text_input("Describe what you would like to draw:")

if prompt:
    with st.spinner("Generating images..."):
        images = model.text_to_image(prompt, batch_size=3)
    st.success("Here are your images:")

    # Display images
    for i, img in enumerate(images):
        st.image(img, caption=f"Image {i+1}", use_column_width=True)
