"""
    This script runs a small Flask app to serve the model predictions through a GET endpoint
    that sends back JSON data.
"""
import os,sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from flask import Flask, request, jsonify
from metaflow import Flow
from metaflow import get_metadata, metadata
import uuid
import time
from utils.utils import text_to_embeddings,text_matching


#### THIS IS GLOBAL, SO OBJECTS LIKE THE MODEL CAN BE RE-USED ACROSS REQUESTS ####

# FLOW_NAME = 'SampleRegressionFlow' # name of the target class that generated the model
# # Set the metadata provider as the src folder in the project,
# # which should contains /.metaflow
# metadata('../src')
# # Fetch currently configured metadata provider to check it's local!
# print(get_metadata())

# def get_latest_successful_run(flow_name: str):
#     "Gets the latest successfull run using Metaflow API"
#     for r in Flow(flow_name).runs():
#         if r.successful: 
#             return r

# # get artifacts from latest run, using Metaflow Client API
# latest_run = get_latest_successful_run(FLOW_NAME)
# latest_model = latest_run.data.model
# We initialise the Flask object to run the flask app
app = Flask(__name__)


@app.route('/dashboard', methods=['GET'])
def main():
  """
    This function runs when the endpoint /predict is hit with a GET request.
    
    It looks for an input x value, runs the model and returns the prediction.
  """
  start = time.time()
  input_str = request.args.get('x')
  data_file='/Users/kabir/FRE-7773-Project/data/clean_data/product_embeddings.pkl'
  similar_product, time_taken = text_matching(input_str, data_file)
  print(input_str)
  print("Most Similar Product:", similar_product)
  print("Time Taken:", time_taken, "seconds")
  # returning the response to the client	
  response = {
    'metadata': {
       'eventId': str(uuid.uuid4()),
       'serverTimestamp':round(time.time() * 1000), # epoch time in ms
       'serverProcessingTime': round((time.time() - start) * 1000) # in ms
    },
    'data': 
    {
      'input':input_str,
      'products':similar_product['ProductID'].to_list()
    }
  }
  
  return jsonify(response)
    

if __name__=='__main__':
  # Run the Flask app to run the server
  app.run(debug=True,port=5002)