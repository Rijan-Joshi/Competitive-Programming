import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arguments()
    try:
        background = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open('shirt.png')
    size = shirt.size

    muppet = ImageOps.fit(background, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

def check_command_line_arguments():
    if (len(sys.argv[1:])<2):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv[1:])>2):
        sys.exit("Too many command-line arguments")
    input_image = splitext(sys.argv[1])
    output_image= splitext(sys.argv[2])
    if (checkExtension(input_image)==False):
        sys.exit("Invalid input")
    if (checkExtension(output_image) == False):
        sys.exit("Invalid output")
    if (input_image[1].upper() != output_image[1].upper()):
        sys.exit("Input and output have different extensions")

def checkExtension(image):
    if image[1] in ['.jpeg', '.jpg', '.png']:
        return True
    return False

if __name__ == "__main__":
    main()