import asyncio
import fal_client
from dotenv import load_dotenv
from common_utils import encode_image_to_base64
import random


load_dotenv()

async def subscribe():
    handler = await fal_client.submit_async(
        "comfy/robertobalestri/siamesi",
        arguments={
            "loadimage_1": encode_image_to_base64("face_manueste.jpeg"),
            "cliptextencode_text": "Photo of Young, androgynous with oval face, delicate features, fair skin, straight light brown hair styled short, almond-shaped eyes, fine eyebrows, soft lips, small nose, textured skin. Slim build, average height, fair skin, narrow shoulders, smooth, androgynous body, fluid fashion choices, almost naked, sexy. Placed in the methaphorical but physical place of the nothingness, her shoulders emerge from water.",
            "randomnoise_noise_seed": random.randint(0, 999999999),
        },
    )

    async for event in handler.iter_events(with_logs=True):
        print(event)

    result = await handler.get()

    print(result)


if __name__ == "__main__":
    asyncio.run(subscribe())