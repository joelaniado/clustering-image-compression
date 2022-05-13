from src.web_app import webapp


def main():
    wa = webapp()
    wa.buildapp()

    #im, og_shape = import_image("images/input/{}".format('TEST.JPG'))
    #print(im,og_shape)
    #image_compression(seed, k, im, og_shape, file)


if __name__ == "__main__":
    main()
