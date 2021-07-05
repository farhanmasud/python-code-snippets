from PIL import Image, UnidentifiedImageError
import sys


def main():
    image_file_name = sys.argv[1]
    output_file_width = sys.argv[2]

    # open image
    try:
        img = Image.open(image_file_name)
    except FileNotFoundError:
        print("Image file not found")
        sys.exit(1)
    except UnidentifiedImageError:
        print("File type not supported")
        sys.exit(1)

    # get image aspect ratio
    img_aspect_ratio = img.width / img.height

    # parse downscale width
    try:
        w = int(output_file_width)
    except ValueError:
        print("Not an integer. Please provide an Integer as downscale width")
        sys.exit(1)

    h = round(w / img_aspect_ratio)

    # Resize smoothly down to 16x16 pixels
    img_small = img.resize((w, h), resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    result = img_small.resize(img.size, Image.NEAREST)

    # save image
    result.save(f"pixelated-{w}x{h}-{image_file_name}")


if __name__ == "__main__":
    main()
