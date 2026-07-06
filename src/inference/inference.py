import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from PIL import Image
from torchvision import transforms

from src.model.load_model import load_model


def inference(image_path):

    # Load trained model
    model = load_model()

    # Image Transform
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    # Load Image
    image = Image.open(image_path).convert("RGB")

    # Convert Image to Tensor
    image_tensor = transform(image)

    # Add Batch Dimension
    image_tensor = image_tensor.unsqueeze(0)

    # Disable Gradient Calculation
    with torch.no_grad():
        output = model(image_tensor)

    # Calculate Reconstruction Error
    criterion = nn.MSELoss()
    loss = criterion(output, image_tensor)

    # Decision Threshold
    threshold = 0.05

    if loss.item() < threshold:
        prediction = "Genuine ID"
    else:
        prediction = "Suspicious / Fake ID"

    # Convert tensors back to images
    original = image_tensor.squeeze(0).permute(1, 2, 0).numpy()
    reconstructed = output.squeeze(0).permute(1, 2, 0).numpy()

    # Display Original and Reconstructed Images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(reconstructed)
    plt.title("Reconstructed Image")
    plt.axis("off")

    plt.tight_layout()
    # plt.show()

    # Return values for FastAPI
    return prediction, loss.item()


if __name__ == "__main__":

    prediction, error = inference(
        "data/processed/aadit/WhatsApp Image 2026-06-29 at 5.19.50 PM.jpeg"
    )

    print(f"\nPrediction: {prediction}")
    print(f"Reconstruction Error: {error:.6f}")