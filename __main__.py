from src.data_import import import_image
from src.model import image_compression


def main():
    seed = 24
    k = 250
    file = "josh.jpg"
    im, og_shape = import_image("images/input/{}".format(file))
    image_compression(seed, k, im, og_shape, file)


if __name__ == "__main__":
    main()
