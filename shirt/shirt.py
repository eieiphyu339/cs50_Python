import sys
import os

from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = [".jpg",".jpeg",".png"]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Input and output files must have .jpg, .jpeg or .png extensions")

    if input_ext != output_ext:
        sys.exit("Input and output files must have the same extensions")

    if not os.path.isfile(input_file):
        sys.exit(f"Input file {input_file} does not exist")

    try:
        input_image = Image.open(input_file)
        shirt = Image.open("shirt.png")

        size = shirt.size
        input_image = ImageOps.fit(input_image,size)

        input_image.paste(shirt,shirt)
        input_image.save(output_file)
    except FileNotFoundError:
        sys.exit("The file was not found in the current directory")


if __name__ == "__main__":
    main()
