import os
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
torch.cuda.empty_cache()

SDV5_MODEL_PATH = "./stable-diffusion-v1-5"
SAV_PATH = "./media"

prompt = input("Prompt to generate image: ")

num_inference_steps = 100
height, width = 512, 720

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = f"{filename}({counter}){extension}"
        counter+=1

    return path

print(f"Characters: {len(prompt)} -- limit: 200")

pipe = StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH)
pipe = pipe.to('cpu')

with autocast('cpu'):
    image = pipe(
        prompt, 
        height=height, 
        width=width
    ).images[0]

image_path = uniquify(os.path.join(SAV_PATH, (prompt[:25] + '...') if len(prompt)>25 else prompt) + '.png')
print(image_path)
image.save(image_path)