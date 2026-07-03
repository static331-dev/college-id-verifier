import cv2
from pathlib import Path
from image_loader import load_images


def preprocess():

    # Get all image paths
    image_paths = load_images()

    # Output folder
    output_folder = Path("data/processed")
    output_folder.mkdir(exist_ok=True)

    # Process every image
    for image_path in image_paths:

        # Read image
        image = cv2.imread(str(image_path))

        # Resize image
        image = cv2.resize(image, (224, 224))

        student_folder = output_folder / image_path.parent.name
        
        student_folder.mkdir(exist_ok=True)

        output_path = student_folder / image_path.name

        cv2.imwrite(str(output_path), image)

        print(f"Processed: {image_path.name}")

    print("\nAll images processed successfully!")


if __name__ == "__main__":
    preprocess()