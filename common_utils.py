"""
Common utility functions for ComfyUI workflows
"""

import json
import base64
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_json_file(file_path):
    """Load and return JSON data from a file."""
    logging.info(f"Loading JSON file from {file_path}")
    with open(file_path, "r") as file:
        return json.load(file)

def encode_image_to_base64(image_path):
    """Encode an image file to base64."""
    logging.info(f"Encoding image to base64 from {image_path}")
    with open(image_path, "rb") as image_file:
        imgValue = 'data:image/jpeg;base64,' + base64.b64encode(image_file.read()).decode('utf-8')
        return imgValue

def update_workflow_json(workflow_json, updates):
    """Update the workflow JSON with provided updates."""
    logging.info("Updating workflow JSON with provided updates")
    for node_id, node_updates in updates.items():
        if node_id in workflow_json:
            workflow_json[node_id]["inputs"].update(node_updates["inputs"])
            logging.debug(f"Updated node {node_id} with inputs: {node_updates['inputs']}")
    return workflow_json
