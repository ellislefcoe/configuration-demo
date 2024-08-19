import argparse
import os
from PIL import Image
from tqdm import tqdm # progress bar

def parse_args(): # Changed slightly from the chatGPT output because I dont like main()
    parser = argparse.ArgumentParser(description="Resize images in a folder.")

    # Input folder
    parser.add_argument('input_folder', type=str, help="Path to the input folder containing images.")

    # Output width and height
    parser.add_argument('width', type=int, help="The desired output width.")
    parser.add_argument('height', type=int, help="The desired output height.")

    # Scaling flag
    parser.add_argument('--relative', action='store_true', help="If set, width and height are relative scaling factors (as a percentage).")

    # Optional output folder
    parser.add_argument('--output_folder', type=str, help="Path to the output folder. If not provided, a new folder will be created with the input folder's name + '_RESIZED'.")

    args = parser.parse_args()

    # Handle output folder
    if not args.output_folder:
        args.output_folder = f"{args.input_folder.rstrip('/')}_RESIZED"
        os.makedirs(args.output_folder, exist_ok=True)

    return args


# if __name__ == "__main__": should be standard practice,
# its a little faster just because of how python
# treats local variables vs global variables
if __name__ == "__main__":
    args = parse_args()

    for file_ in tqdm(os.listdir(args.input_folder)): # loop over all the files in the folder
        # skip if not an image file
        if not file_.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp')):
            continue

        # resize the image
        img = Image.open(os.path.join(args.input_folder, file_))

        if not args.relative:
            img = img.resize((args.width, args.height))
        else: # relative scaling
            img = img.resize((img.size[0] * (args.width/100), img.size[1] * (args.height/100)))


        img.save(os.path.join(args.output_folder, file_))


