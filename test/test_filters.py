from params import *
from PIL import Image

resampling_filters = {
    "NEAREST": Image.NEAREST,
    "BOX": Image.BOX,
    "BILINEAR": Image.BILINEAR,
    "HAMMING": Image.HAMMING,
    "BICUBIC": Image.BICUBIC,
    "LANCOZS": Image.LANCZOS,
}

image = Image.open("filter-origin.png")
image = image.convert(mode="RGB")
for idx, str_filter in enumerate(resampling_filters.keys()):
    image_result = image.resize(size=target_size, resample=resampling_filters[str_filter])
    # image_result.show()
    image_result.save(str(idx) + str_filter + ".png")
