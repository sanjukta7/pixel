from PIL import Image


def pimage(input_file_path: str, output_file_path: str, pixel_size: int):
    with Image.open(input_file_path) as image:
        image = image.resize(
            (image.size[0] // (pixel_size), image.size[1] // (pixel_size)),
            Image.NEAREST
        )
        image = image.resize(
            (image.size[0] * pixel_size, image.size[1] * pixel_size),
            Image.NEAREST
        )
        image.save(output_file_path)