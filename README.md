# AI Fitness Trainer
Utilized Google's MediaPipe pose detection model to extract joint positions from exercise videos uploaded via React Frontend. Implemented real-time chatbot feedback with quantized TinyLlama 1.1B LLM model from Hugging Face Transformers. Other features include Django user authentification, peak detection algorithm from scipy for counting reps from pose landmarks, and matplotlib plots for displaying reps with concentric/eccentric time spent for each rep for measuring time under tension. Additionally, I made this a scalable and resilient web application on GCP by utilizing Docker for containerization and Kubernetes (GKE) for orchestration. This enabled me to optime resource utilization through auto-scaling policies and improve system integration and performance.

## Video Demo
[![Watch the video](https://img.youtube.com/vi/amvVTQqxZ8/0.jpg)](https://www.youtube.com/watch?v=amvVT-QqxZ8)

## Live Website: http://34.118.173.89/

### 1. LLM Chatbot Feedback
I incorporated Hugging Face Transformers popular text generation models including Deepseek-R1 and TinyLlama to provide the user with recommendations for improving their exercise form based off their uploaded video. I accomplished this by creating a prompt to the chatbot that includes specific directions as to what it should be looking to suggest improvements on. The prompt
consisted of specific instructions along with calculated range of motion angles computed from extracted joint position landmarks using Google's Mediapipe pose detection model. 

### Model Selection
I first started trying to implement DeepSeek-R1 7B for chatbot feedback due to the recent publications and promising potential for performing fast inference on resource constrained devices. However, after deploying the model from Hugging Face Transformers, I realized the inference time of 6039s provided an unreasonable inference time for implementing real-time or near real-time feedback to the user making the application non user-friendly. After realizing this I needed to find a model with less parameters that can be used to provide much better inference time for giving the user a positive experience. After some research into similar chat generation models, I decided to try TinyLlama 1.1B model with significantly less parameters (7B ~ 1B) to see if I could get near real-time feedback from my chatbot model while still maintaining good responses. My initial implementation of the base TinyLlama resulted in much better performance than my DeepSeek model, however, after further examination I realized there was still room for some optimization. I implemented both base models using AutoModelForCausaLLM from transformers library created by Hugging Face Transformers. 

### Base DeepSeek-R1 7B inference time
![B685D96A-5E67-4C8D-A99B-5A349C143168_4_5005_c](https://github.com/user-attachments/assets/778fd76f-92a8-4815-b352-4a2ae69dd6ab)


### Base TinyLlama 1.1B inference time
![8EA06A7F-FA6B-4AE1-813D-9BF3D4903862_4_5005_c](https://github.com/user-attachments/assets/6a2bc65b-145b-4aa0-9e4e-a1b310dc9272)


### 2. Quantization
I applied 8 bit quantization to my TinyLlama 1.1B model for even faster inference speeds to ensure a postive user experience. I utlized llama_cpp to load this quantized TinyLlama model that converts the training parameters from 32 bit floating point numbers to 8 bit integers. This drastically reduced the memory resource usage of my model which is important for enabling other users on less powerful systems to be able to execute the same program without any issues. Decreasing the overall size of the model from switching from 32 bit floating point numbers to 8 bit integers also decreases the overall complexity of the model yielding faster inference times. 

### Base TinyLlama 1.1B memory usage
![80EAE1F2-6362-46A1-BD62-E44D24333A05_4_5005_c](https://github.com/user-attachments/assets/ba102de0-0b16-4b48-aea4-0921a6222bb2)



### Quantized TinyLlama 1.1B memory usage and inference time
![3F17062C-5F1D-49A7-9A84-4F9955664026_4_5005_c](https://github.com/user-attachments/assets/853b04be-842c-443f-8c3c-8bdbd1282e29))

### 3. MediaPipe
Google's MediaPipe is a pose detection algorithm that extracts joint positions from images. I utilized this pose detection algorithm in combination with OpenCV's VideoCapture class to extract each frame from the video and append each joint position to a joint_positions list which would then be used to help calculate force_vectors, joint_angles, and range of motion for a particular exercise. Mediapipe utilization can be seen in read_input_files.py.

### 4. Docker
My docker-compose.yml file defines and manages a multi-container Docker application composed of five services: a React frontend, a Django backend, a Llama model service, a MediaPipe service, and a PostgreSQL database. These services are interconnected through a shared network and utilize volumes for data persistence.

### 5. Kubernetes (GKE)
This project utilizes Kubernetes on Google Kubernetes Engine (GKE) to orchestrate and manage containerized applications, with Docker images stored in Google Container Registry (GCR). The cluster employs multi-architecture node pools to optimize resource usage across different workload requirements. Applications are deployed and scaled using Kubernetes deployment YAML files, while stateful data for the database is managed through a StatefulSet and PersistentVolumeClaims (PVCs) to ensure data durability. External access to the frontend is facilitated by a Google Cloud Load Balancer provisioned via a Kubernetes LoadBalancer service, offering a public IP address for user interaction.

### 6. Django Backend (Code found in /fitness_backend/django_app)

### Models

The Django backend defines many different models in models.py such as UserManager, User, and Exercise. The User model extends Django's AbstractBaseUser to manage user authentication and profiles, including fields like username, email, body weight, and gender. It also includes custom user management via the UserManager. The Exercise model handles exercise video uploads, analysis, and storage. It stores input videos, output videos, and output images for my matplotlib chart to buckets created on Google Cloud Storage. Additional classes can be found in fitness_backend/exercise including my base DeepseekChatbot class and my base TinyLlama class which are not currently being used in my implementation, but was involved in my original attempts in creating a real-time chatbot feedback for exercise improvement recommendations.

### llama_model

This Python file defines a BlokeLlamaChatbot class that utilizes the llama-cpp library to load a quantized TinyLlama LLM to generate text responses based on prompts, specifically for biomechanical analysis of exercise form. It exposes a Flask API endpoint /generate_text which, upon receiving a POST request with joint position data, timestamps, and exercise type, initializes the chatbot, processes the data to generate feedback using the Llama model, and returns the chatbot's response as a JSON.

### mediapipe_model

This Python file defines a MediapipeModel class that processes a video of an exercise using the process_video function that leverages MediaPipe for pose estimation to extract joint positions and timestamps. It calculates force vectors and plots repetitions to provide insights into the exercise, ultimately exposing a Flask API endpoint /process_video that accepts video details and returns the processed video path, a representative image path, joint positions, and timestamps as a JSON response.

### Views

The views.py file defines API views for user authentication, registration, and exercise video processing. LoginView handles user authentication, utilizing Django's authenticate function and Token generation for secure access. NewUserView creates new user accounts, employing User.objects.create_user which automatically hashes passwords for security. FileUploadView processes uploaded exercise videos, storing them in Google Cloud Storage. AnalysisStatusView provides the status of the video analysis and returns the chatbot_response when it is done processing. The file makes extensive use of Django Rest Framework's APIView, Response, and Serializer for API development, and transaction.atomic() for database transaction management.

### Serializers

The serializers.py file defines serializers for the Exercise and User models, leveraging Django REST Framework's ModelSerializer. ExerciseSerializer converts Exercise model instances into JSON format, including all fields, for API responses. Similarly, UserSerializer serializes User model instances, encompassing all user attributes. These serializers facilitate data exchange between the Django backend and the frontend, streamlining the process of converting complex model data into easily consumable JSON.

### 5. React Frontend (Code found in fitness-frontend)

### App
This React component sets up routing for the application, defining paths for user login, new user registration, and the main fitness application interface.

### FitnessApp
This React component, FitnessApp, provides the frontend interface for uploading and analyzing workout videos. It manages user authentication via JWT tokens stored in localStorage, redirecting unauthenticated users to the login page. The component allows users to select an exercise, input the weight lifted, and upload an MP4 video. Upon submission, it sends the video to the Django backend for processing, displaying a loading indicator during upload and analysis. It then polls the backend for analysis status, rendering the processed video and a progress image once available. After the backend's chatbot completes its analysis, the response is displayed to the user. The component uses react-player for video playback and lucide-react for loading spinners, and leverages React hooks like useState, useEffect, and useRef for state management and DOM manipulation. It also incorporates react-router-dom for navigation.

### NewUser
This React component, NewUser, handles user registration. It provides a form for users to input their username, email, password (with password validation), name, weight, and gender. Upon submission, it sends this data to the Django backend to create a new user account. It stores the returned authentication token and user ID in localStorage and redirects the user to the FitnessApp component. It uses useState and useEffect hooks for state management and navigation, and includes password validation logic to ensure secure user credentials.

### UserLogin
This React component, UserLogin, handles user authentication. It provides a login form for users to enter their username and password, with password validation. It communicates with the Django backend to authenticate users, storing the returned authentication token and user ID in localStorage upon successful login. It also implements a login attempt counter and lockout mechanism to prevent brute-force attacks.


### Resources

Kaggle Dataset: https://www.kaggle.com/datasets/hasyimabdillah/workoutfitness-video

DeepSeek-R1 7B: https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat

TinyLlama 1.1B: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0

Quantized TinyLlama 1.1B: https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v0.3-GGUF
