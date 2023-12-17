### FRE-7773-Project
# Go Designer: An AI-powered Interior Design Assistant
## Description
Go Designer: An AI-powered Interior Design Assistant is a transformative project developed by Kabir Jaiswal and Nigam Patel. This project is at the forefront of integrating advanced technology into the realm of interior design. Utilizing the innovative CLIP embeddings, a neural network-based approach, Go Designer excels in interpreting and analyzing both text and image inputs. This unique capability enables the tool to provide personalized furniture and decor recommendations, tailored to the user's preferences gathered from various inputs.

The user experience is significantly enhanced by the incorporation of Streamlit, an open-source application framework. This integration ensures a seamless and intuitive interaction with the AI model, making the process of making design choices more accessible. Furthermore, the project leverages Comet ML for monitoring the performance and progress of the machine learning models. This is crucial in refining the models for greater accuracy and efficiency, guaranteeing that the recommendations are not only relevant but also practical.

Go Designer addresses the complex challenges associated with deploying machine learning models and managing extensive datasets, especially in the context of interior design. This project is a remarkable example of the innovative use of AI in everyday life, paving the way for new avenues in how technology can aid in personalizing and enhancing living environments. The primary dataset for this project is sourced from IvonaTau's IKEA collection on GitHub, offering a comprehensive array of furniture choices for the model to learn from and recommend.

## Installation and Setup

To get started with the Go Designer project, follow these steps to set up your environment and install the necessary dependencies.

### Prerequisites
- Ensure you have Python 3.8 installed on your system. If not, you can download it from the [Python official website](https://www.python.org/downloads/).

### Setting Up a Python Environment
1. **Create a Python Virtual Environment**: It's recommended to use a virtual environment to manage the dependencies for your project. To create a virtual environment, open your terminal or command prompt and navigate to the project directory. Then run:
   ```bash
   python -m venv go_designer_env
   ```
   This command creates a new directory `go_designer_env` which will contain all the necessary executables to use the packages that a Python project would need.

2. **Activate the Virtual Environment**:
   - On Windows, run:
     ```bash
     go_designer_env\Scripts\activate
     ```
   - On macOS and Linux, run:
     ```bash
     source go_designer_env/bin/activate
     ```
   After activation, your command line should prefix with `(go_designer_env)`, indicating that the virtual environment is active.

### Installing Dependencies
1. **Install Required Packages**: With the virtual environment active, install the project dependencies using the `requirements.txt` file in the repository. Run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install CLIP Library**: Go Designer utilizes the CLIP library for processing image and text inputs. Install it using pip:
   ```bash
   pip install git+https://github.com/openai/CLIP.git
   ```

3. **Install Comet ML**: For tracking and optimizing machine learning models, install Comet ML:
   ```bash
   pip install comet_ml
   ```

### Final Steps

Once you have successfully installed all the dependencies, you are ready to launch the Go Designer application. Follow these steps to start the application:

1. **Navigate to the Source Folder**: First, ensure that your virtual environment (`go_designer_env`) is still activated. Then, navigate to the `src` folder within the project directory. You can do this by running:
   ```bash
   cd src
   ```

2. **Run the Flask Application**: Start the Flask server by running the `flask_app.py` file. In your terminal, execute the following command:
   ```bash
   python flask_app.py
   ```
   This command will start the backend server of the Go Designer application. Keep this terminal open and running.

3. **Open a New Terminal Window**: Now, open a new terminal window or tab. Ensure that you activate the virtual environment in this new terminal as well, if it's not already activated.

4. **Run the Streamlit Application**: In the new terminal, navigate to the `src` folder again (if you're not already there) and start the Streamlit application by running `streamlit_app.py`:
   ```bash
   python streamlit_app.py
   ```
   This will launch the Streamlit interface of the Go Designer application.

5. **Access the Application**: After running the Streamlit command, a local URL will be provided in the terminal (typically something like `http://localhost:8501`). Open this URL in your web browser to interact with the Go Designer application.


## Usage
Interacting with the Go Designer Application
1. Open the Application in Your Browser: After starting the Streamlit application as described in the final setup steps, a local URL (typically http://localhost:8501) will be displayed in your terminal. Open this URL in your web browser to access the Go Designer interface.

2. Using the Application: The Go Designer application provides an intuitive and interactive interface for users. Here's how you can use it to get personalized furniture and decor recommendations:

***Input Preferences***: The application will prompt you to input your preferences, either through text or image inputs. This could include descriptions of the style, color, or type of furniture you are interested in.

***Explore Recommendations***: Based on your inputs, the application will use its AI-powered algorithms to generate and display a list of recommended furniture and decor items. These recommendations are tailored to match the preferences you've provided.

***Refine Your Choices***: You can further refine your choices or input additional details to get more specific recommendations. The application is designed to adapt and respond to your inputs dynamically.

## License
This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## References
1. Tautkute, I., Możejko, A., Stokowiec, W., Trzciński, T., Brocki, Ł., & Marasek, K. (2017). What looks good with my sofa: Multimodal search engine for interior design. In M. Ganzha, L. Maciaszek, & M. Paprzycki (Eds.), Proceedings of the 2017 Federated Conference on Computer Science and Information Systems (Vol. 11, pp. 1275-1282). IEEE. https://doi.org/10.15439/2017F56​
​

2. Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., & Sutskever, I. (2021). Learning transferable visual models from natural language supervision. arXiv. https://arxiv.org/abs/2103.00020​
​

3. Schuhmann, C., Vencu, R., Beaumont, R., Kaczmarczyk, R., Mullis, C., Katta, A., Coombes, T., Jitsev, J., & Komatsuzaki, A. (2021). LAION-400M: Open dataset of CLIP-filtered 400 million image-text pairs. arXiv. https://arxiv.org/abs/2111.02114​
​
​

## Authors and Acknowledgment
Kabir Jaiswal
Nigam Patel

