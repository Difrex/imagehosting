from PIL import Image

def resize_image(fh, img_prop):
    im = Image.open(fh)
    # size = 100, 100
    im.thumbnail(img_prop['size'])
    #print(img_prop['size'])
    # im.thumbnail(size)
    thumb_name = img_prop['dest'] + '/thumb_' + img_prop['name']
    im.save(thumb_name)

    return thumb_name
