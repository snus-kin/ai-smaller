"""
'Compress' image by resizing 
"""
import json


class Compressor:
    def __init__(self, evaluator):
        self.evaluator = evaluator
        with open("imagenet_class_index.json") as f:
            self.idx2label = json.load(f)

    def iteration(self, image):
        """
        Returns a a resized image that is 10 pixels smaller in both directions
        """
        current_size = image.size
        new_size = (current_size[0] - 10, current_size[1] - 10)
        image.thumbnail(new_size)
        return image

    def __to_label(self, pred):
        return self.idx2label[str(int(pred))][1]

    def __call__(self, image):
        initial_prediction = self.evaluator(image)
        print(f"Initial prediction: {self.__to_label(initial_prediction)}")

        iteration = image
        previous_iteration = image
        iter_prediction = initial_prediction

        while iter_prediction == initial_prediction:
            previous_iteration = iteration
            iteration = self.iteration(previous_iteration)
            iter_prediction = self.evaluator(iteration)
            print(f"Current prediction: {self.__to_label(iter_prediction)}")
        else:
            print(f"Size of final image: {previous_iteration.size}")
            return previous_iteration
