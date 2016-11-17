from PIL import Image
import requests
import argparse


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
        width = (int)(face['width'] * 1.0)
        height = (int)(face['height'] * 1.3)
        jordan = jordan.resize((width, height), Image.ANTIALIAS)
        image.paste(jordan, (face['x'], face['y']), jordan)


if __name__ == '__main__':
    args = get_args()

    jordan = Image.open(args.jordan)
    image = Image.open(str(args.image))

    faces = get_faces(args.image)
    apply_jordans(image, jordan, faces)

    image.show()
