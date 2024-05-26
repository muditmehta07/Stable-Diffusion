import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
torch.cuda.empty_cache()

from prompt import art_styles

SDV5_MODEL_PATH = "D:\Models\stable-diffusion-v1-5"
SAV_PATH = "media"

prompt = input("Prompt to generate image: ")
num_images_per_prompt = 5

num_inference_steps = 100
height, width = 512, 720

device_type = 'cuda'
low_vram = True
negative_prompt = "bad, low quality, blurry, pixelated, deformed, disfigured, grainy, low resolution, out of focus, overexposed, underexposed, oversaturated, undersaturated, noisy, poor lighting, incorrect anatomy, unnatural, distorted, cropped"


def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{filename}({counter}){extension}"
        counter+=1
    return path

def render_prompt():
    shortened_prompt = (prompt[:25] + '...') if len(prompt)>25 else prompt
    shortened_prompt = shortened_prompt.replace(' ', '_')

    generation_path = os.path.join(SAV_PATH, shortened_prompt.removesuffix('...'))

    if not os.path.exists(SAV_PATH):
        os.mkdir(SAV_PATH)
    if not os.path.exists(generation_path):
        os.mkdir(generation_path)

    if device_type == 'cuda':
        if low_vram:
            pipe = StableDiffusionPipeline.from_pretrained(
                torch_dtype = torch.float16,
                revision = 'fp16'
            )
        else:
            pipe = StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH)

        pipe = pipe.to('cuda')

        if low_vram:
            pipe.enable_attention_slicing()
    
    elif device_type == 'cpu':
        pipe = StableDiffusionPipeline.from_pretrained(SDV5_MODEL_PATH)
    else:
        print('Invalid Device Type')
        return

    for style_type, style_prompt in art_styles.items():
        prompt_stylized = f"{prompt}, {style_prompt}"

        print(f"Full Prompt:\n{prompt_stylized}\n")
        print(f"Characters: {len(prompt)} -- limit: 200")

        for i in range(num_images_per_prompt):
            if device_type == 'cuda':
                with autocast('cuda'):
                    image = pipe(
                        prompt_stylized,
                        negative_prompt=negative_prompt,
                        height=height,
                        width=width
                    ).images[0]
            else:
                image = pipe(prompt).images[0]

            image_path = uniquify(os.path.join(SAV_PATH, shortened_prompt + '.png'))
            print(image_path)
            image.save(image_path)
    print("Render Finished")

render_prompt()