from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"          # folder for unedited images
path_out = "./editedImgs"  # folder for edited images

# Create the output folder if it doesn't exist
os.makedirs(path_out, exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))

    # Apply image processing (sharpening, BW, rotation)
    edit = img.filter(ImageFilter.SHARPEN)

    # Adjust contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Save the edited image to the output folder
    output_path = os.path.join(path_out, f"edited_{filename}")
    edit.save(output_path)

print("Image processing complete.")

   