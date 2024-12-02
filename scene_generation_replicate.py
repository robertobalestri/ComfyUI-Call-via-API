"""
Scene Generation Script using Replicate API

This script generates scenes using the Replicate API. It can be run directly
from the command line or imported and used in other Python scripts.

Usage:
    1. Command line:
       python scene_generation_replicate.py --scene "scene description" --output "output_image_name"

    2. Imported in another script:
       from scene_generation_replicate import run_scene_generation_no_swapping
       output = run_scene_generation_no_swapping(scene_input, output_name)

Requirements:
    - replicate
    - python-dotenv
"""

import replicate
from dotenv import load_dotenv
import json
import requests
from PIL import Image
from io import BytesIO
from common_utils import load_json_file, update_workflow_json
import logging
import time
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def run_no_swap(scene_input, output_name=None):
    """
    Run the scene generation process using the Replicate API.

    Args:
        scene_input (str): Description of the scene.
        output_name (str, optional): Name for the output image. If None, a default name will be generated.

    Returns:
        PIL.Image: The output image from the Replicate API.
    """
    logging.info("Starting scene generation process")
    workflow_json = load_json_file("workflows/flux_workflow_only_scene_no_swap_REPLICATE.json")
    

    # Update the workflow JSON with the provided input and random seed
    workflow_json = update_workflow_json(workflow_json, {"25": {"inputs": {"noise_seed": random.randint(0, 99999999999999999)}}})  # Update the seed in the workflow
    workflow_json = update_workflow_json(workflow_json, {"6": {"inputs": {"text": scene_input}}})

    # Print the workflow JSON with indentation
    logging.info(f"Workflow JSON: {json.dumps(workflow_json, indent=2)}")

    input = {
        "workflow_json": json.dumps(workflow_json),
        "output_quality": 100
    }

    logging.info("Running the Replicate API for scene generation")
    output = replicate.run(
        "fofr/any-comfyui-workflow:61e713aa841c3a275d7097b209a75873e1f950bb79c5fbec1a94be351cea8fdd",
        input=input
    )

    # Download the image from the URL
    image_url = output[0]
    logging.info(f"Downloading image from URL: {image_url}")
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # Generate output name if not provided based on time
    if output_name is None:
        output_name = f"outputs/scene_generated_{time.strftime('%Y%m%d_%H%M%S')}.jpg"

    # Convert to RGB mode (in case it's RGBA)
    image = img.convert('RGB')
    # Save as JPG
    image.save(output_name, 'JPEG')
    logging.info(f"Image saved as {output_name}")
    
    return img
