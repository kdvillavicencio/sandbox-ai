# Sample AI App

## 1. img2audio

Takes an image input and outputs an audio file narrating a short story about the image.

The AI pipeline is composed of the following:
- img2text: uses `transformers` pipeline function
- txt2scenario: uses Llama2 local deployment via `llama-cpp-python`
- scenario2audio: uses HuggingFace inference API

**Notes**
- input and output files are hard-coded
- provision for a Streamlit layer is available

**Commands**
```
streamlit run /path/to/file.py
```

## 2. viltAPI

Uses a Vision-and-Language-Transformer (ViLT) model to answer a question about the uploaded image. Serves an endpoint for the inference using FastAPI.

## References
https://www.linkedin.com/posts/yuhongsun_host-a-llama-2-api-on-gpu-for-free-activity-7095057739793518592-JN7y