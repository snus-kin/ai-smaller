"""
'Compress' image by resizing
"""
from abc import ABC, abstractmethod

class Compressor(ABC):
    def __init__(self, evaluator):
        self.evaluator = evaluator

    @abstractmethod
    def iteration(self, image):
        pass

    def __call__(self, image):
        initial_prediction = self.evaluator(image)

        iteration = previous_iteration = image
        iter_prediction = initial_prediction

        while iter_prediction == initial_prediction:
            previous_iteration = iteration
            iteration = self.iteration(previous_iteration)
            iter_prediction = self.evaluator(iteration)

        return previous_iteration
