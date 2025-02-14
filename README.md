# GAN Image Generator

<div align="center">

[![GitHub](https://img.shields.io/github/stars/ArpitKadam/GAN-Image-Generator?style=social)](https://github.com/ArpitKadam/GAN-Image-Generator)
[![GitHub issues](https://img.shields.io/github/issues/ArpitKadam/GAN-Image-Generator)](https://github.com/ArpitKadam/GAN-Image-Generator/issues)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  

[License](https://github.com/ArpitKadam/GAN-Image-Generator/blob/main/LICENS) | [Site](https://gan-image-generator-5etc.onrender.com/)

</div>

✨ **GAN Image Generator** is a web application built using Streamlit that allows users to generate AI-powered images using a Generative Adversarial Network (GAN). This project leverages a pre-trained generator model to create realistic images based on random noise input.

## Features

- User-friendly interface to specify the number of images to generate.
- Displays generated images in a grid format.
- Information about Generative Adversarial Networks (GANs) and useful resources for further learning.

## Requirements

To run this project, you need to have the following installed:

- Python 3.6 or higher
- Streamlit
- TensorFlow
- NumPy
- Matplotlib

You can install the required packages using pip:
```bash
pip install -r requirements.txt
```


## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ArpitKadam/GAN-Image-Generator.git
   cd GAN-Image-Generator
   ```

2. **Download the pre-trained generator model** and save it as `generator_model.keras` in the project directory. (Make sure to replace this with your actual model file.)

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Open your web browser** and go to `http://localhost:8501` to access the application.

## How to Use

- Use the slider in the sidebar to select the number of images you want to generate (between 1 and 100).
- Click the "Generate Images 🚀" button to create the images.
- The generated images will be displayed below the button.

## About GANs

Generative Adversarial Networks (GANs) are a type of artificial intelligence model used to generate realistic images, videos, and even music. They work by training two neural networks – a generator and a discriminator – in a competitive process. The generator tries to create realistic data, while the discriminator tries to differentiate real from fake data.

### Learn More About GANs:

- 📜 **Original Paper (Goodfellow et al., 2014):** [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)
- 📖 **GANs Explained:** [A Beginner’s Guide](https://towardsdatascience.com/overcoming-data-scarcity-imbalance-gans-smote-explained-through-bartending-6a868259b4d9/)
- 🎥 **Video Tutorial:** [GANs Explained Visually](https://www.youtube.com/watch?v=8L11aMN5KY8)
- 🛠 **Hands-on Tutorial:** [Train Your Own GAN](https://www.tensorflow.org/tutorials/generative/dcgan)

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ArpitKadam/GAN-Image-Generator/blob/main/LICENSE) file for details.

---

🚀 *Explore, learn, and start generating your own AI-powered images!*
