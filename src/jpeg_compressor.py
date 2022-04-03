"""
    JPEG Compression iterator

    if you save a jpeg with the same quality settings
    it tends to not change it much, here we can just
    save at a random quality level so it does some
    rounding errors
"""
from PIL import Image
from random import randint
from io import BytesIO
from compressor import Compressor


class JPEGCompressor(Compressor):
    def iteration(self, image):
        buffer = BytesIO()
        image.save(buffer, "JPEG", quality=randint(0, 100))
        compressed = Image.open(buffer)
        return compressed
