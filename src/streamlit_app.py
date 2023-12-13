import streamlit as st
import requests
import os, sys
import re
from utils.utils import find_image, image_matching
import random

# Set the configuration for the Streamlit page
st.set_page_config(page_title="GoDesigner", layout="wide")
st.title("GoDesigner")

# Allow the user to input a numerical value
input_text = st.text_input("Describe the room you are trying to build...")
input_room = st.file_uploader("Enter an image of your current room", type=['png', 'jpg'])

input_room_path = ''
if input_room is not None:
    # To read file as bytes:
    bytes_data = input_room.getvalue()
    # Generate a random integer
    random_int = random.randint(99, 9999999)
    # Define the path for the temporary file with the random integer in the filename
    input_room_path = f"/Users/kabir/FRE-7773-Project/data/tmp/temp_image_{random_int}.jpg"
    # Write the bytes data to a temporary file
    with open(input_room_path, "wb") as f:
        f.write(bytes_data)

input_room_path = [input_room_path]
room_root_folder = '/Users/kabir/FRE-7773-Project/data/clean_data/room_embeddings.pkl'
img_root_folder = '/Users/kabir/FRE-7773-Project/data/images'

# Define the action when the 'Get Recommendations' button is clicked
if st.button("Get Recommendations"):
    # Handle the request and response
    try:
        # Send a GET request to the prediction server
        response = requests.get(f"http://127.0.0.1:5002/dashboard?x={input_text}")
        
        # Process a successful response
        st.success("Roduct Recommendations")
        if response.status_code == 200:
            prediction = response.json()['data']
            
            # Set up a container for horizontal layout for product images
            cols = st.columns(len(prediction['products']))
            
            # Display each product image in a column
            for idx, product in enumerate(prediction['products']):
                product = re.sub(r'^[^0-9]*', '', product) + '.jpg'
                image_path = find_image(img_root_folder, product)
                with cols[idx]:
                    st.image(image_path)

            # Process room recommendations
            st.success("Room Recommendations")
            similar_room, time_taken = image_matching(input_room_path, room_root_folder)
            # Set up a container for horizontal layout for room images
            room_cols = st.columns(len(similar_room['Room']))
            
            # Display each room image in a column
            for idx, room in enumerate(similar_room['Room'].to_list()):
                root_folder = '/Users/kabir/FRE-7773-Project/data/images/room_scenes/'
                image_name = room
                image_path = find_image(root_folder, image_name)
                
                # Display the image if the path is found
                if image_path:
                    with room_cols[idx]:
                        st.image(image_path)
                else:
                    print(f"No image found for {image_name}")
        else:
            # Handle unsuccessful response
            st.error("Server response error. Please try again later.")
    except requests.exceptions.RequestException as error:
        # Handle request exceptions
        st.error(f"Connection error: {error}")
