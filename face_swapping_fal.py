import asyncio
import fal_client
from dotenv import load_dotenv
from common_utils import encode_image_to_base64
import random
import logging
import time
from PIL import Image
from io import BytesIO
import base64
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

async def run_face_swapping(prompt_input, face_path, output_name=None, siamesi=False):
    """
    Run the face swapping process using the new method with fal_client.

    Args:
        prompt_input (str): Text description for face generation.
        face_path (str): Path to the input face image.
        output_name (str, optional): Name for the output image. If None, a default name will be generated.

    Returns:
        PIL.Image: The output image from the fal_client API.
    """
    logging.info("Starting face swapping process")

    # Base64 encode the input image
    encoded_image = encode_image_to_base64(face_path)
    random_seed = random.randint(0, 999999999)
    
    # Submit the task to fal_client
    handler = await fal_client.submit_async(
        "comfy/Claudio-Loop/siamesi" if siamesi else "comfy/Claudio-Loop/faceswap",
        arguments={
            "loadimage_1": encoded_image,
            "cliptextencode_text": prompt_input,
            "randomnoise_noise_seed": random_seed,
        },
    )

    logging.info("Waiting for task completion")
    # Handle events (for logging or monitoring progress)
    async for event in handler.iter_events(with_logs=True):
        print(event)
    
    # Get the final result
    result = await handler.get()
    logging.info("Task completed")

    
    # Extract the image URL from the response
    try:
        image_url = result['outputs']['9']['images'][0]['url']
        logging.info(f"Image URL: {image_url}")
    except (KeyError, IndexError):
        logging.error("Failed to extract image URL from the response.")
        raise ValueError("Invalid response format: Unable to find image URL.")
    
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
