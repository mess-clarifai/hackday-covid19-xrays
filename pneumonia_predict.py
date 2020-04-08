import argparse
from pprint import pprint

from clarifai.rest import ClarifaiApp

parser = argparse.ArgumentParser()
parser.add_argument(
    "--api_key",
    type=str,
    default=None,
    help="API Key for the App that is being used.",
)
parser.add_argument(
    "--model_id",
    type=str,
    default=None,
    help="ID for the model that is being used.",
)
parser.add_argument(
    "--image",
    type=str,
    default=None,
    help="File path to the image to test."
)

def main(args):
  app = ClarifaiApp(api_key=args.api_key)
  # model = app.models.get(model_id=args.model_id)
  model = app.models.get(model_id="Pneumonia Classifier")
  response = model.predict_by_filename(args.image)

  pprint(response)

if __name__ == "__main__":
  args = parser.parse_args()
  _ = main(args)
