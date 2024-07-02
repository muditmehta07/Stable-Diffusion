# Stable Diffusion

This project generates images based on text prompts using the Stable Diffusion model.

Checkout the project's resultant AI Art:
https://www.behance.net/muditmehta07

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project utilizes the Stable Diffusion model to generate images from text prompts. The model can be run on both GPU (CUDA) and CPU, with optional low VRAM mode for better performance on machines with limited resources.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/muditmehta07/Stable-Diffusion.git
    cd Stable-Diffusion
    ```

2. **Install the required packages**:
    ```sh
    pip install torch diffusers
    ```

3. **Download the Stable Diffusion v1.5 Model**:
    ```sh
    git lfs install
    git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
    ```

## Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **Enter the prompt when prompted**:
    ```
    Prompt to generate image: [your prompt here]
    ```

3. **Find the generated images**:
    The images will be saved in the specified directory (`SAV_PATH`).

## Configuration

The script can be configured by setting the following variables:

- **SDV5_MODEL_PATH**: Path to the Stable Diffusion model.
- **SAV_PATH**: Directory to save generated images.
- **num_images_per_prompt**: Number of images to generate per prompt.
- **num_inference_steps**: Number of inference steps.
- **height, width**: Dimensions of the generated images.
- **device_type**: Device to run the model on (`'cuda'` or `'cpu'`).
- **low_vram**: Whether to use low VRAM mode.

Example configuration:

```python
SDV5_MODEL_PATH = "D:/Models/stable-diffusion-v1-5"
SAV_PATH = "media"
num_images_per_prompt = 5
num_inference_steps = 100
height, width = 512, 720
device_type = 'cuda'
low_vram = True
negative_prompt = "bad, low quality"
```

## Contributing

Contributions are important (let's learn a few things from Heinrich Himmler):

1. Fork the repository.
2. Create a new branch by using `git checkout -b new-branch`.
3. Commit your changes by using `git commit -m new-branch`.
4. Push your changes to the branch by using `git push origin new-branch`.

##  License

```
This README provides a comprehensive overview of your project, from installation to usage, configuration, code explanation, contributing guidelines, and license information. You can adapt it further to match any specific details or additional sections you might want to include.
```
