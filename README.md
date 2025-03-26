# AI Fitness Trainer
Utilized Google's MediaPipe pose detection model to extract joint positions from exercise videos uploaded via React Frontend. Implemented real-time chatbot feedback with quantized TinyLlama 1.1B LLM model from Hugging Face Transformers. Other features include Django user authentification, asynchronous pose detection display and chatbot feedback using asyncio library, peak detection algorithm from scipy for counting reps from pose landmarks, and matplotlib plots for displaying reps with concentric/eccentric time spent for each rep for measuring time under tension. 

## Video Demo
[![Watch the video](https://img.youtube.com/vi/amvVT-QqxZ8/0.jpg)](https://www.youtube.com/watch?v=amvVT-QqxZ8)

## Link to active website:

### 1. Model Selection
I first started trying to implement DeepSeek-R1 7B for chatbot feedback due to the recent publications and promising potential for performing fast inference on resource constrained devices. However, after deploying the model from Hugging Face Transformers, I realized the inference time of 6039s provided an unreasonable inference time for implementing real-time or near real-time feedback to the user making the application non user-friendly. After realizing this I needed to find a model with less parameters that can be used to provide much better inference time for giving the user a positive experience. After some research into similar chat generation models, I decided to try TinyLlama 1.1B model with significantly less parameters (7B ~ 1B) to see if I could get near real-time feedback from my chatbot model while still maintaining good responses. My initial implementation of the base TinyLlama resulted in much better performance than my DeepSeek model, however, after further examination I realized there was still room for some optimization.

### Base DeepSeek-R1 7B inference time

### Base TinyLlama 1.1B inference time

### 2. Quantization
I applied 8 bit quantization to my TinyLlama 1.1B model for even faster inference speeds to ensure a postive user experience. I utlized llama_cpp to apply this 8 bit quantization to convert my training parameters from 32 bit floating point numbers to 8 bit integers. This drastically reduced the memory resource usage of my model which is important for enabling other users on less powerful systems to be able to execute the same program without any issues. Decreasing the overall size of the model from switching from 32 bit floating point numbers to 8 bit integers also 

### Base TinyLlama 1.1B memory usage and inference time

### Quantized TinyLlama 1.1B memory usage and inference time

### 3. Django Backend
My Django backend consists of many advanced features including robust security measures implemented using .

### Resources
Kaggle Dataset:
DeepSeek-R1 7B:
TinyLlama 1.1B:
