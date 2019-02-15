""" Work with images """
from PIL import Image


def resize_image(fh, img_prop):
    """ Change image size
    :param fh: A filename (string), pathlib.Path object or a file object.
    :param img_prop: dict containing keys: name, size, dest
    :return: name of created thumbnail
    """
    image = Image.open(fh)
    image.thumbnail(img_prop['size'])
    thumb_name = img_prop['dest'] + '/thumb_' + img_prop['name']
    image.save(thumb_name)

    return thumb_name


def create_thumb_from_file(filename):
    orig_file = 'config/media/images/' + filename
    # Create thumbnail
    thumb_name = resize_image(orig_file, {
        'name': filename,
        'size': [300, 300],  # TODO: move to config
        'dest': 'config/media/images/'
    }
                              )
    return thumb_name
