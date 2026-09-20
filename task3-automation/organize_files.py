import os
import shutil

source_folder = "source_images"
destination_folder = "sorted_images"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

moved_count = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        moved_count += 1
        print("Moved:", filename)

print("\nDone. Total files moved:", moved_count)
