from pathlib import Path
from PIL import Image

import torch
from torch.utils.data import Dataset
from torchvision import transforms


class IDCardDataset(Dataset):

    def __init__(self, dataset_path="data/processed"):

        self.dataset_path = Path(dataset_path)

        self.image_paths = []

        for student_folder in self.dataset_path.iterdir():

            if student_folder.is_dir():

                for image in student_folder.iterdir():

                    if image.suffix.lower() in [".jpg", ".jpeg", ".png"]:

                        self.image_paths.append(image)

        self.transform = transforms.ToTensor()

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):

        image_path = self.image_paths[index]

        image = Image.open(image_path).convert("RGB")

        image = self.transform(image)

        return image


if __name__ == "__main__":

    dataset = IDCardDataset()

    print("Total Images :", len(dataset))

    image = dataset[0]

    print("Tensor Shape :", image.shape)