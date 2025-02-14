import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load the pre-trained generator model
generator = load_model('generator_model.keras')

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>✨ GAN Image Generator ✨</h1>", 
    unsafe_allow_html=True
)
st.markdown("Generate AI-powered images using a Generative Adversarial Network (GAN)!")

st.sidebar.header("Settings")
num_images = st.sidebar.slider("Number of images:", min_value=1, max_value=100, value=10)

# Generate button
if st.sidebar.button("Generate Images 🚀"):
    with st.spinner("Generating images... Please wait!"):
        # Generate images
        LATENT_DIM = 100
        noise = np.random.normal(size=(num_images, LATENT_DIM))
        generated_images = generator.predict(noise)
        generated_images = (generated_images + 1) / 2  # Rescale images to [0, 1]

        # Display images in a grid (5 images per row)
        st.subheader(f"🎨 Generated Images ({num_images})")
        cols_per_row = 5  # Number of images per row
        rows = (num_images // cols_per_row) + (num_images % cols_per_row > 0)

        for row in range(rows):
            cols = st.columns(cols_per_row)
            for col_idx in range(cols_per_row):
                img_idx = row * cols_per_row + col_idx
                if img_idx < num_images:
                    with cols[col_idx]:
                        st.image(generated_images[img_idx], caption=f"Image {img_idx+1}", use_container_width=True)

    st.success("✅ Images generated successfully!")


# --- About GANs Section ---
st.markdown("---")
st.markdown("## ℹ️ About GANs")
st.write(
    "Generative Adversarial Networks (GANs) are a type of artificial intelligence model used to generate realistic images, videos, and even music. "
    "They work by training two neural networks – a generator and a discriminator – in a competitive process. The generator tries to create realistic data, "
    "while the discriminator tries to differentiate real from fake data."
)

st.markdown("### 🔗 Learn More About GANs:")
st.markdown(
    "- 📜 **Original Paper (Goodfellow et al., 2014):** [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)  \n"
    "- 📖 **GANs Explained:** [A Beginner’s Guide](https://towardsdatascience.com/overcoming-data-scarcity-imbalance-gans-smote-explained-through-bartending-6a868259b4d9/)  \n"
    "- 🎥 **Video Tutorial:** [GANs Explained Visually](https://www.youtube.com/watch?v=8L11aMN5KY8)  \n"
    "- 🛠 **Hands-on Tutorial:** [Train Your Own GAN](https://www.tensorflow.org/tutorials/generative/dcgan)"
)

st.markdown("🚀 *Explore, learn, and start generating your own AI-powered images!*")

