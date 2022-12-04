import PIL.Image
import string

# ASCII characters used to build new image
ASCII_CHARS = list(string.printable)
# ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
# Resize image acording to a new width
def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    new_image = image.resize((new_width, new_height))
    return new_image, new_width


# Convert each pixel to grayscale
def convert_to_gray(image):
    return image.convert(mode="L")


# Convert pixels to string of ASCII characters
def convert_pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])


def save_asci_image(image):
    # convert image to ASCII
    new_image, new_width = resize(image)

    ascii_raw_data = convert_pixels_to_ascii(convert_to_gray(new_image))

    # save new image
    pixel_count = len(ascii_raw_data)
    ascii_image = "\n".join(
        [
            ascii_raw_data[index : (index + new_width)]
            for index in range(0, pixel_count, new_width)
        ]
    )
    print(ascii_image)
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


def read_image(path):
    # open image
    try:
        image = PIL.Image.open(path)
    except:
        print("path is not valid")
    return image


def main():
    image = read_image(path="Ladybug.jpg")
    save_asci_image(image)


if __name__ == "__main__":
    main()
