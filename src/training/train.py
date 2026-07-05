import torch
import torch.nn as nn
import torch.optim as optim

from src.dataset.dataloader import create_dataloader
from src.model.autoencoder import Autoencoder


def train():

    # Create DataLoader
    dataloader = create_dataloader(batch_size=8)

    # Create Model
    model = Autoencoder()

    # Loss Function
    criterion = nn.MSELoss()

    # Optimizer
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Number of epochs
    epochs = 5

    # Training Loop
    for epoch in range(epochs):

        running_loss = 0.0

        for images in dataloader:

            # Clear previous gradients
            optimizer.zero_grad()

            # Forward Pass
            outputs = model(images)

            # Calculate Loss
            loss = criterion(outputs, images)

            # Backward Pass
            loss.backward()

            # Update Weights
            optimizer.step()

            # Add Batch Loss
            running_loss += loss.item()

        # Average Loss for one epoch
        avg_loss = running_loss / len(dataloader)

        print(f"Epoch [{epoch + 1}/{epochs}] - Loss: {avg_loss:.6f}")

    # Save the trained model
    torch.save(model.state_dict(), "models/autoencoder.pth")

    print("\nModel saved successfully!")
    print("Location: models/autoencoder.pth")


if __name__ == "__main__":
    train()