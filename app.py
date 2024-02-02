from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import cv2
from mtcnn import MTCNN
from PIL import Image

