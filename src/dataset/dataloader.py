from torch.utils.data import DataLoader

from src.dataset.dataset import IDCardDataset

def create_dataloader(batch_size=8):
    
    dataset = IDCardDataset()

    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True
    )

    return dataloader


if __name__ == "__main__":

    dataloader = create_dataloader()

    print("Total Batches :", len(dataloader))

    for batch in dataloader:

        print("Batch Shape :", batch.shape)

        break