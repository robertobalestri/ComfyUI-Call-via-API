"""
Face Swapping Script using Replicate API

This script performs face swapping using the Replicate API. It can be run directly
from the command line or imported and used in other Python scripts.

Usage:
    1. Command line:
       python face_swapping_replicate.py --face "face description" --character "character description" --scene "scene description" --image "path/to/face.jpg" --output "output_image_name"

    2. Imported in another script:
       from face_swapping_replicate import run_face_swapping
       output = run_face_swapping(face_input, character_input, scene_input, face_path, output_name)

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
from common_utils import load_json_file, encode_image_to_base64, update_workflow_json
import logging
import time
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def update_face_swapping_workflow_json(workflow_json, face_input, character_input, scene_input, random_seed):
    """Update the workflow JSON with provided inputs and random seed."""
    logging.info("Updating face swapping workflow JSON")
    updates = {
        "191": {"inputs": {"text": face_input}},
        "189": {"inputs": {"text": character_input}},
        "193": {"inputs": {"text": scene_input}},
        "31": {"inputs": {"seed": random_seed}}  # Update the seed in the workflow
    }
    return update_workflow_json(workflow_json, updates)

def run_face_swapping(face_input, character_input, scene_input, face_path, output_name=None):
    """
    Run the face swapping process using the Replicate API.

    Args:
        face_input (str): Description of the face.
        character_input (str): Description of the character.
        scene_input (str): Description of the scene.
        face_path (str): Path to the face image file.
        output_name (str, optional): Name for the output image. If None, a default name will be generated.

    Returns:
        PIL.Image: The output image from the Replicate API.
    """
    logging.info("Starting face swapping process")
    workflow_json = load_json_file("workflows/face_swapping_REPLICATE.json")
    

    # Update the workflow JSON with the provided inputs and random seed
    workflow_json = update_face_swapping_workflow_json(workflow_json, face_input, character_input, scene_input, random.randint(0, 99999999999999999))

    input = {
        "workflow_json": json.dumps(workflow_json),
        "output_quality": 100,
        "input_file": encode_image_to_base64(face_path)
    }

    logging.info("Running the Replicate API for face swapping")
    output = replicate.run(
        "fofr/any-comfyui-workflow:61e713aa841c3a275d7097b209a75873e1f950bb79c5fbec1a94be351cea8fdd",
        input=input
    )
    
    # Download the image from the URL
    image_url = output[0]
    logging.info(f"Downloading image from URL: {image_url}")
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    
    # Generate output name if not provided 
    if output_name is None:
        output_name = f"face_swapped_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
    
    # Convert to RGB mode (in case it's RGBA)
    img = img.convert('RGB')
    # Save as JPG
    img.save(output_name, 'JPEG')
    logging.info(f"Image saved as {output_name}")
    
    return img