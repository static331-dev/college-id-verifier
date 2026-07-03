from pathlib import Path

def load_images():
    dataset_path = Path("data/raw")

    image_paths = []
    student_count = 0

    for student_folder in dataset_path.iterdir():

        if student_folder.is_dir():

            student_count += 1
            print(f"\nStudent: {student_folder.name}")

            image_count = 0

            for image in student_folder.iterdir():

                if image.suffix.lower() in [".jpg", ".jpeg", ".png"]:

                    image_paths.append(image)
                    image_count += 1

                    print(f"   {image.name}")

            print(f"Images Found: {image_count}")

    print("\n----------------------------")
    print(f"Total Students : {student_count}")
    print(f"Total Images   : {len(image_paths)}")
    print("----------------------------")

    return image_paths


if __name__ == "__main__":
    load_images()