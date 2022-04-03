"""
Evaluate an image against a neural network
"""
import torchvision.models as models
from torchvision import datasets, transforms as T


class Evaluator:
    def __init__(self):
        self.net = models.resnet152(pretrained=True)

        # transforms from torchvision docs
        self.transform = T.Compose(
            [
                T.Resize(256),
                T.CenterCrop(224),
                T.ToTensor(),
                T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ]
        )

        # set model to eval
        self.net.eval()

    def __call__(self, image):
        """
        Returns predicted class for image
        """
        transformed_image = self.transform(image).unsqueeze(0)
        output = self.net(transformed_image)
        _, predicted = output.max(1)

        return predicted
