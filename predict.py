import argparse
from keras.models import Model, load_model
import pickle


def predict_video():


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("model", help="model to be executed")
    # args = parser.parse_args()
    # model_file = args.graph

    pickle_in = open("models/EncodedLabels.sav", "rb")
    EncodedLabels = pickle.load(pickle_in)
    model = load_model('modelv2.h5')
