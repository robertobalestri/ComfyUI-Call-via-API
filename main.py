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
    face_input = "Photo of male, pale skin, asymmetric facial features with a scar over the right eye, dark circles under the eyes, shaved head, and one eye glowing faintly red, giving an unsettling and freakish vibe"
    character_input = "Wearing torn, mismatched urban streetwear including a tattered hoodie, ripped jeans, and heavy black combat boots. Accessories include spiked bracelets and a chain hanging from his pocket"
    scene_input = "In an abandoned subway station with graffiti-covered walls, flickering fluorescent lights, and trash scattered across the floor. The atmosphere is tense, with distant sounds of dripping water and the occasional echo of a train in the background"

    face_path = "face.jpeg"
    output_name_face_swap = "outputs/output_face_swapped.jpg"  # Custom output name
    print("Running face swapping...")
    
    
    siamesi = False
    run_face_swapping(face_input, character_input, scene_input, face_path, output_name_face_swap, siamesi)
    
    
    output_name_face_swap = "outputs/output_face_swapped_siamesi.jpg"  # Custom output name
    siamesi = True
    run_face_swapping(face_input, character_input, scene_input, face_path, output_name_face_swap, siamesi)


    # SCENE GENERATION
    scene_only_input = "A ball on a football field, in the distance a player is running"
    output_name_scene = "outputs/output_scene_generated.jpg"  # Custom output name
    output = run_scene_generation_no_swapping(scene_only_input, output_name_scene)
    

