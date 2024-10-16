"""
Example script for running face swapping and scene generation

This script demonstrates how to import and use the run_face_swapping function
from the face_swapping_replicate module and the run_scene_generation_no_swapping
function from the scene_generation_replicate module in another Python script.

Usage:
    python main.py
"""

from face_swapping_replicate import run_face_swapping
from scene_generation_replicate import run_scene_generation_no_swapping

if __name__ == "__main__":

    # FACE SWAPPING
    face_input = "Male, blonde hair, blue eyes, elf like ears"
    character_input = "Professional in a business suit, holding a cat and kicking a ball"
    scene_input = "The scene happens on a spaceship like environment"
    face_path = "face.png"
    output_name_face_swap = "outputs/output_face_swapped.jpg"  # Custom output name
    print("Running face swapping...")
    run_face_swapping(face_input, character_input, scene_input, face_path, output_name_face_swap)


    # SCENE GENERATION
    scene_only_input = "A ball on a football field, in the distance a player is running"
    output_name_scene = "outputs/output_scene_generated.jpg"  # Custom output name
    output = run_scene_generation_no_swapping(scene_only_input, output_name_scene)
