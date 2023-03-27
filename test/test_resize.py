from params import *
from PIL import Image

target_sizes = [
    (9, 16),
    (18, 32),
    (36, 64),
    (72, 128),
    (135, 240)
]

image = Image.open("origin.png")
image = image.convert(mode="RGB")
for target_size in target_sizes:
    image_result = image.resize(size=target_size, resample=Image.LANCZOS)
    # image_result.show()
    image_result.save(str(target_size) + ".png")
