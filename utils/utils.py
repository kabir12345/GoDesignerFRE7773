import torch
import clip
from PIL import Image
import numpy as np
import pandas as pd
import time
from sklearn.metrics.pairwise import cosine_similarity
import ast 
import os
import re


def find_image(root_folder, image_name):
    found_paths = []
    for root, dirs, files in os.walk(root_folder):
        if image_name in files:
            found_paths.append(os.path.join(root, image_name))
    return found_paths

# Load the CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def text_to_embeddings(texts):
    """
    Convert a list of texts to CLIP embeddings.

    :param texts: List of text strings.
    :return: Numpy array of embeddings.
    """
    # Preprocess the texts
    text_tokens = clip.tokenize(texts).to(device)

    # Generate text embeddings
    with torch.no_grad():
        text_embeddings = model.encode_text(text_tokens)
    
    return text_embeddings.cpu().numpy()

def image_to_embeddings(image_paths):
    """
    Convert a list of image file paths to CLIP embeddings.

    :param image_paths: List of paths to image files.
    :return: Numpy array of embeddings.
    """
    images = []

    # Load and preprocess each image
    for path in image_paths:
        image = preprocess(Image.open(path)).unsqueeze(0).to(device)
        images.append(image)

    # Stack images to form a batch
    image_batch = torch.cat(images, dim=0)

    # Generate image embeddings
    with torch.no_grad():
        image_embeddings = model.encode_image(image_batch)
    
    return image_embeddings.cpu().numpy()



def text_matching(input_string, data_file):
    """
    Finds the most similar products based on the description embeddings.

    :param input_string: The input string to compare.
    :param data_file: Path to the pickle file containing product descriptions and their embeddings.
    :return: Top 5 most similar product descriptions and the time taken to run the function.
    """
    start_time = time.time()
    df = pd.read_pickle(data_file)

    # Generate embedding for the input string
    input_embedding = text_to_embeddings([input_string])

    # Extract description embeddings from the DataFrame
    desc_embeddings = np.array(df['desc_embeddings'].tolist())

    # Calculate cosine similarities
    similarities = cosine_similarity(input_embedding, desc_embeddings).flatten()

    # Find the indices of the top 5 most similar products
    most_similar_indices = np.argsort(similarities)[-5:][::-1]

    # Retrieve the most similar products
    most_similar_products = df.iloc[most_similar_indices]

    # Display images of the top 5 products
    for idx in most_similar_indices:
        root_folder = '/Users/kabir/FRE-7773-Project/data/images'
        image_name = re.sub(r'^[^0-9]*', '', df.iloc[idx]['Image'])
        image_path = find_image(root_folder, image_name)
        # img = Image.open(image_path[0])
        # display(img)

    # Calculate the time taken
    time_taken = time.time() - start_time

    return most_similar_products, time_taken

def image_matching(input_image, data_file):
    """
    Finds the most similar room based on the description embeddings.

    :param input_image: The input image to compare.
    :param data_file: Path to the pickle file containing room descriptions and their embeddings.
    :return: Top 5 most similar product descriptions and the time taken to run the function.
    """
    start_time = time.time()
    df = pd.read_pickle(data_file)

    # Generate embedding for the input string
    input_embedding = image_to_embeddings(input_image)

    # Extract description embeddings from the DataFrame
    room_embeddings = np.array(df['image_embeddings'].tolist())

    # Calculate cosine similarities
    similarities = cosine_similarity(input_embedding, room_embeddings).flatten()

    # Find the indices of the top 5 most similar products
    most_similar_indices = np.argsort(similarities)[-5:][::-1]

    # Retrieve the most similar products
    most_similar_rooms = df.iloc[most_similar_indices]

    # Display images of the top 5 products
    for idx in most_similar_indices:
        root_folder = '/Users/kabir/FRE-7773-Project/data/images/room_scenes/'
        image_name = df.iloc[idx]['Room']
        image_path = find_image(root_folder, image_name)
        
        # Check if the image path list is not empty
        # if image_path:
        #     img = Image.open(image_path[0])
        #     display(img)
        # else:
        #     print(f"No image found for {image_name}")

    # Calculate the time taken
    time_taken = time.time() - start_time

    return most_similar_rooms, time_taken

