"""
'Compress' image by resizing 
"""
from PIL import Image
import json


class Compressor:
    def __init__(self, evalutator):
        self.evalutator = evalutator
        with open("imagenet_class_index.json") as f:
            self.idx2label = json.load(f)

    def __iteration(self, image):
        """
        Returns a a resized image that is 10 pixels smaller in both directions
        """
        current_size = image.size
        new_size = (current_size[0] - 10, current_size[1] - 10)
        resized_image = image.resize(new_size, Image.ANTIALIAS)
        return resized_image

    def __to_label(self, pred):
        return self.idx2label[str(int(pred))][1]

    def __call__(self, image):
        initial_prediction = self.evalutator(image)
        print(f"Size of initial image: {image.size}")
        print(f"Initial prediction: {self.__to_label(initial_prediction)}")

        iteration = image
        previous_iteration = image
        iter_prediction = initial_prediction

        while iter_prediction == initial_prediction:
            previous_iteration = iteration
            iteration = self.__iteration(previous_iteration)
            iter_prediction = self.evalutator(iteration)
            print(f"Current image size: {iteration.size}")
            print(f"Current prediction: {self.__to_label(iter_prediction)}")
        else:
            print(f"Size of final image: {previous_iteration.size}")
            return previous_iteration
