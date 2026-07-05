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

            # Forward pass
            outputs = model(images)

            # Calculate reconstruction loss
            loss = criterion(outputs, images)

            # Backpropagation
            loss.backward()

            # Update model weights
            optimizer.step()

            # Add batch loss
            running_loss += loss.item()

        # Print average loss for this epoch
        avg_loss = running_loss / len(dataloader)

        print(f"Epoch [{epoch + 1}/{epochs}] - Loss: {avg_loss:.6f}")


if __name__ == "__main__":
    train()