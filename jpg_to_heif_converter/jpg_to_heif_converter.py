import os
from PIL import Image

def convert_image(input_path, output_path):
    with Image.open(input_path) as im:
        heif_path = os.path.splitext(output_path)[0] + '.heif'
        im.save(heif_path, 'HEIF', quality_mode='quality', quality_level=100)

def main():
    print("Welcome to JPG to HEIF Converter!")
    while True:
        jpg_folder = input("Enter the path to the folder containing JPG images: ")
        if os.path.exists(jpg_folder):
            break
        else:
            print("The folder does not exist.")
    while True:
        heif_folder = input("Enter the path to the folder where HEIF images will be saved: ")
        if os.path.exists(heif_folder):
            break
        else:
            print("The folder does not exist.")
    # Create the HEIF folder if it doesn't exist yet
    if not os.path.exists(heif_folder):
        os.makedirs(heif_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            output_path = os.path.join(heif_folder, os.path.splitext(filename)[0] + '.heif')
            convert_image(input_path, output_path)
    print("All images converted successfully!")

if __name__ == "__main__":
    main()

# softy_plug