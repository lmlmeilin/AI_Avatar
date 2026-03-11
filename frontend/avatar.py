from diffusers import StableDiffusionPipeline
import torch
import os
from config import AVATAR_OUTPUT_DIR

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to("cuda")

def generate_avatar(prompt: str, filename: str) -> str:
    image = pipe(prompt).images[0]
    path = os.path.join(AVATAR_OUTPUT_DIR, filename)
    image.save(path)
    return path