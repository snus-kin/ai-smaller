"""
'Compress' image by resizing
"""
from compressor import Compressor


class ResizeCompressor(Compressor):
    def iteration(self, image):
        """
        Returns a a resized image that is 10 pixels smaller in both directions
        """
        current_size = image.size
        new_size = (current_size[0] - 10, current_size[1] - 10)
        image.thumbnail(new_size)
        return image
