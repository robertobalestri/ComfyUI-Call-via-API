"""
Example script for running face swapping and scene generation

This script demonstrates how to import and use the run_face_swapping function
from the face_swapping_replicate module and the run_scene_generation_no_swapping
function from the scene_generation_replicate module in another Python script.

Usage:
    python main.py
"""

#from face_swapping_replicate import run_face_swapping
from face_swapping_fal import run_face_swapping
from scene_generation_fal import run_no_swap
from common_utils import run_asyncio_task
#from scene_generation_replicate import run_no_swap
import asyncio

if __name__ == "__main__":

    
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # FACE SWAPPING
    prompt_input = "A photo of a young, androgynous person with an oval face, delicate features, fair skin, straight light brown hair styled short, almond-shaped eyes, fine eyebrows, soft lips, and a small nose. They have a slim build, average height, fair skin, narrow shoulders, and a smooth, androgynous body. Their style is casual yet edgy, with a minimalist look, tailored jackets, fitted pants, and fluid fashion choices. The background is an abandoned subway station with graffiti-covered walls, flickering fluorescent lights, and trash scattered across the floor. The atmosphere is tense, with distant sounds of dripping water and the occasional echo of a train in the background. The subject is placed in front of the camera, 3 meters away."
    
    face_path = "face_manueste.jpeg"
    output_name_face_swap = "outputs/output_face_swapped.jpg"  # Custom output name
    print("Running face swapping...")
    
    
    siamesi = False
    run_asyncio_task(run_face_swapping, prompt_input, face_path, output_name_face_swap, siamesi)
    
    
    output_name_face_swap = "outputs/output_face_swapped_siamesi.jpg"  # Custom output name
    siamesi = True
    run_asyncio_task(run_face_swapping, prompt_input, face_path, output_name_face_swap, siamesi)


    # SCENE GENERATION
    prompt_input = "A photo of a lone figure clad in weathered, metallic armor adorned with faint glowing runes that pulse softly in contrasting hues of warm gold and cold blue, standing in a profile view against the backdrop of a dimly lit medieval chamber. The figure’s iron mask is featureless yet polished enough to faintly reflect the interplay of light, and a dark hooded cloak cascades behind them, adding to the imposing aesthetic. The tilt-shift angle creates a dynamic focus on the character, while the edges reveal subtle details such as a weathered altar with scattered chains and faint symbols etched into the stone floor. The atmosphere is a blend of mysticism and foreboding, with warm torchlight and cool moonlight intersecting to create a dramatic play of shadows and light. Muted tones of silver, black, and gold dominate the palette, reinforcing the dark medieval theme with a hint of transcendence."
    output_name_scene = "outputs/output_scene_generated.jpg"  # Custom output name
    run_asyncio_task(run_no_swap, prompt_input, output_name_scene)
    

