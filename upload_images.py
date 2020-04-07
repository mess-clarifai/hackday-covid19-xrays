import os
import argparse

from tqdm import tqdm
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

parser = argparse.ArgumentParser()
parser.add_argument(
    "--image_dir",
    type=str,
    default='./images',
    help="The directory in which the images are stored."
)
parser.add_argument(
    "--api_key",
    type=str,
    default=None,
    help="API Key for the App that is being used.",
)


def main(args):
    print("API Key: {}".format(args.api_key))
    app = ClarifaiApp(api_key=args.api_key)
    for folder in os.listdir(args.image_dir):
        folder = os.path.join(args.image_dir, folder)
        if os.path.isdir(folder):
            path, base = os.path.split(folder)
            for image_file in tqdm(os.listdir(folder), desc=base):
                image_file_path = os.path.join(folder, image_file)
                try:
                    app.inputs.create_image_from_filename(
                        image_file_path,
                        concepts=[base],
                    )
                except:
                    continue


if __name__ == "__main__":
    args = parser.parse_args()
    _ = main(args)
