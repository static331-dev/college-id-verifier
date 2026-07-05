import torch

from src.model.autoencoder import Autoencoder


def load_model():

    # Create the model architecture
    model = Autoencoder()

    # Load the trained weights
    model.load_state_dict(torch.load("models/autoencoder.pth"))

    # Switch to evaluation mode
    model.eval()

    print("Model loaded successfully!")

    return model


if __name__ == "__main__":

    model = load_model()

    print("\nLoaded Model:\n")
    print(model)