import streamlit as st
import requests
import os,sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from utils.utils import find_image,image_matching
import re
from PIL import Image
import io
import random
import pandas as pd

# Set the configuration for the Streamlit page
st.set_page_config(page_title="Godesigner", layout="wide")
st.title("GoDesigner")
input_room_path=''
# Allow the user to input a numerical value
input_text = st.text_input("Describe the room you are trying to build...")
input_room = st.file_uploader("Enter an image of your current room",type=['png', 'jpg'])

if input_room is not None:
    # To read file as bytes:
    bytes_data = input_room.getvalue()

    # Generate a random integer
    random_int = random.randint(99, 9999999)

    # Define the path for the temporary file with the random integer in the filename
    
    input_room_path= f"/Users/kabir/FRE-7773-Project/data/tmp/temp_image_{random_int}.jpg"

    # Write the bytes data to a temporary file
    with open(input_room_path , "wb") as f:
        f.write(bytes_data)
input_room_path=[input_room_path]
room_root_folder='/Users/kabir/FRE-7773-Project/data/clean_data/room_embeddings.pkl'

img_root_folder = '/Users/kabir/FRE-7773-Project/data/images'

# Define the action when the 'Predict' button is clicked
if st.button("Get Reccomendations"):
    # Handle the request and response
    try:
        # Send a GET request to the prediction server
        response = requests.get(f"http://127.0.0.1:5002/dashboard?x={input_text}")
        
        # Process a successful response
        st.success("Product Reccomendations")
        if response.status_code == 200:
            prediction = response.json()['data']
            for i in range(len(prediction['products'])):
                prediction['products'][i]=re.sub(r'^[^0-9]*', '', prediction['products'][i])+'.jpg'
                image_path = find_image(img_root_folder, prediction['products'][i])
                st.image(image_path)
            st.success("Room Reccomendations")
            similar_room, time_taken = image_matching(input_room_path, room_root_folder)
            for idx in similar_room['Room'].to_list():
                root_folder = '/Users/kabir/FRE-7773-Project/data/images/room_scenes/'
                image_name = idx
                image_path = find_image(root_folder, image_name)
                
                # Check if the image path list is not empty
                if image_path:
                    st.image(image_path)
                else:
                    print(f"No image found for {image_name}")
            
        else:
            # Handle unsuccessful response
            st.error("Server response error. Please try again later.")
    except requests.exceptions.RequestException as error:
        # Handle request exceptions
        st.error(f"Connection error: {error}")

# Instructions for the user
#st.caption("To receive a prediction, please enter a numerical value and click on 'Make Prediction'.")


