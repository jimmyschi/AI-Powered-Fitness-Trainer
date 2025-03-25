## AI Fitness Trainer
Utilized Google's MediaPipe pose detection model to extract joint positions from exercise videos uploaded via React Frontend. Implemented real-time chatbot feedback with quantized TinyLlama 1.1B LLM model from Hugging Face Transformers.
# Video Demo
[![Watch the video](https://img.youtube.com/vi/amvVT-QqxZ8/0.jpg)](https://www.youtube.com/watch?v=amvVT-QqxZ8)

# 1. Model Selection
I first started trying to implement DeepSeek-R1 7B for chatbot feedback due to the recent publications and promising potential for performing fast inference on resource constrained devices. However, after deploying the model from Hugging Face Transformers, I realized the inference time of 6039s provided an unreasonable inference time for implementing real-time or near real-time feedback to the user making the application non user-friendly. After realizing this I needed to find a model with less parameters that can be used to provide much better inference time for giving the user a positive experience. After some research into similar chat generation models, I decided to try TinyLlama 1.1B model with significantly less parameters (7B ~ 1B) to see if I could get near real-time feedback from my chatbot model while still maintaining good responses. My initial implementation of the base TinyLlama resulted in much better performance than my DeepSeek model, however, after further examination I realized there was still room for some optimization.

# 2. Quantization

# 3. Django Backend

