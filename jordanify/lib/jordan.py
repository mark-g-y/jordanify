from PIL import Image
import requests
import argparse

from jordanify import settings


def get_args():
    parser = argparse.ArgumentParser(
        description='When there are so many crying Jordan faces you need a script to apply them all.')
    parser.add_argument(
        'image',
        type=str,
        help='the path of the image to apply the Jordan face to')
    parser.add_argument(
        '--jordan',
        type=str,
        default='jordan.png',
        help='the path of the Jordan face image')

    args = parser.parse_args()

    return args


def get_faces(imagepath):
    url = 'https://apicloud-facerect.p.mashape.com/process-file.json'
    headers = {
        'X-Mashape-Key': 'fV0GgxeAUSmshfE4aN38Q6MKpliDp1gJoxbjsnepusXS2CnRt3'}
    files = {'image': open(imagepath, 'rb')}
    r = requests.post(url, headers=headers, files=files)

    return r.json().get('faces')


def apply_jordans(image, jordan, faces):
    for face in faces:
        width = (int)(face['width'] * 1.25)
        height = (int)(face['height'] * 1.6)
        jordan = jordan.resize((width, height), Image.ANTIALIAS)
        image.paste(jordan, (face['x'] - (int)(width * 0.05), face['y'] - (int)(height * 0.2)), jordan)
        
    return image


def jordanify(filepath, jordanpath):
    jordan = Image.open(jordanpath)
    image = Image.open(filepath)

    faces = get_faces(filepath)
    image = apply_jordans(image, jordan, faces)

    return image


if __name__ == '__main__':
    args = get_args()
    image = jordanify(str(args.image), args.jordan)
    image.show()
