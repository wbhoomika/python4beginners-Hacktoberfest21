"""
Created on Thu Sep 17 18:51:40 2020
@author: ISH KAPOOR
"""
'''
ASCII_CHARS is just a plain idea of decreasing order of density of letters, can be as per your wish.
new_width can also be altered, but make sure it is chnaged in every of its instance.
the output is also printed on the cmd as output and also in a text file named 'ascii_image.txt'.
'''
import PIL.Image

# Ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize image accoarding to a new width
def resize_image(image, new_width = 200):

    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayify(image):

    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(n, new_width = 200):

    # Attempt to open image from user-input
    path = input("Enter a valid path-name to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "isn't a valid path-name to an image.")

    # Convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # Format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # Print the result
    print(ascii_image)

    # Save the result/file to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

for n in range(0, 397):
    main(n)