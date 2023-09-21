#!/usr/bin/python3

# Import required libraries and modules
import argparse  # For command-line argument parsing
import os  # For interacting with the operating system
import torch  # PyTorch library for deep learning
from torch import autocast  # Context for mixed-precision training
from diffusers import StableDiffusionPipeline  # Import StableDiffusionPipeline from the 'diffusers' module

# Function to generate images using stable diffusion
def stable_diffusion(prompt, samples, height, width):
    # Set the default model name and update it if the directory doesn't exist locally
    model_name = "./stable-diffusion-v1-5"
    model_name = model_name if os.path.exists(model_name) else "runwayml/stable-diffusion-v1-5"
    
    # Set the device to CUDA (GPU) for computation
    device = "cuda"
    
    # Load the StableDiffusionPipeline model and set the data type to float16
    # The data type float16 represents a 16-bit floating-point number with lower precision and reduced memory usage
    # compared to float32 or float64, often used for faster computation in deep learning models.
    pipe = StableDiffusionPipeline.from_pretrained(
        model_name, torch_dtype=torch.float16
    ).to(device)
    
    # Use autocast for mixed-precision inference
    with autocast(device):
        # Generate images using the pipeline
        result = pipe(
            [prompt] * samples,
            height=height,
            width=width,
            generator=torch.Generator(device=device)
        )
    
    # Save generated images
    for i, image in enumerate(result.images):
        image.save(
            "output/n_%d.png"
            % ( i + 1 )
        )
    
# Main function
def main():
    # Create an argument parser with descriptions
    parser = argparse.ArgumentParser(description="Create images from a text prompt.")
    
    # Define command-line arguments
    parser.add_argument(
        "--prompt", type=str,
        nargs="?",
        default="a dog hosting a late night tv show",
        help="The prompt to render into an image"
    )
    parser.add_argument(
        "--n_samples",
        type=int,
        default=1,
        help="Number of images to create per run",
    )
    parser.add_argument(
        "--H",
        type=int,
        default=512,
        help="Image height in pixels"
    )
    parser.add_argument(
        "--W",
        type=int,
        nargs="?",
        default=512,
        help="Image width in pixels"
    )
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the stable_diffusion function with parsed arguments
    stable_diffusion(
        args.prompt,
        args.n_samples,
        args.H,
        args.W
    )

# Execute the main function if the script is run as the main module
if __name__ == "__main__":
    main()