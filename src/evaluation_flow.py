from comet_ml import Experiment, Artifact
import numpy as np
import os
import os,sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
import re
from PIL import Image
from utils.utils import text_to_embeddings,text_matching
os.environ['COMET_API_KEY'] = 'sC9loWjV0qRd93uQTOOpERUvd'
os.environ['MY_PROJECT_NAME'] = 'team9'

import os,sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
import re
from utils.utils import find_image, image_matching

def main():
    #Exp for text matching
    exp = Experiment(project_name=os.environ['MY_PROJECT_NAME'],
                    auto_param_logging=False)
    input_string = 'red and green beds for my bedroom'
    data_file='/Users/kabir/FRE-7773-Project/data/clean_data/product_embeddings.pkl'
    similar_product, time_taken = text_matching(input_string, data_file)
    print("Most Similar Product:", similar_product)
    print("Time Taken:", time_taken, "seconds")
    similar_product.to_csv('/Users/kabir/FRE-7773-Project/src/tmp/exp.csv')
    artifact = Artifact(name="similar products", artifact_type="dataset-text")
    artifact.add("/Users/kabir/FRE-7773-Project/src/tmp/exp.csv")

    exp.log_artifact(artifact)
    metrics = {"time taken":time_taken,
    }
    exp.log_metrics(metrics)

    #Exp for image matching
    input_image = ['/Users/kabir/FRE-7773-Project/data/tmp/temp_image_8991638.jpg']
    data_file='/Users/kabir/FRE-7773-Project/data/clean_data/room_embeddings.pkl'
    similar_room, time_taken = image_matching(input_image, data_file)
    similar_room.to_csv('/Users/kabir/FRE-7773-Project/src/tmp/exp1.csv')
    artifact1 = Artifact(name="asimilar rooms", artifact_type="dataset-image")
    artifact1.add("/Users/kabir/FRE-7773-Project/src/tmp/exp.csv")

    exp.log_artifact(artifact)
    metrics = {"time taken":time_taken,
    }
    exp.log_text(input_string)
    img = Image.open(input_image[0])
    exp.log_image(img,name='input_image')
    exp.end()
    return


if __name__ == "__main__":
    main()