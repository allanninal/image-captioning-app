import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import base64
import io

# Initialize the Flask application
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

# Configure logging to display information level logs
logging.basicConfig(level=logging.INFO)

# Configuration for the model name
MODEL_NAME = "Salesforce/blip-image-captioning-base"

# Load the BLIP model and processor using the specified model name
captioning_model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)
image_processor = BlipProcessor.from_pretrained(MODEL_NAME)

def decode_image(base64_image):
    """
    Decode a base64 encoded string to a PIL image.

    Args:
        base64_image (str): Base64 encoded image string.

    Returns:
        Image: A PIL Image object.

    Raises:
        ValueError: If the image data is invalid or cannot be decoded.
    """
    try:
        # Decode the base64 string to bytes
        image_bytes = base64.b64decode(base64_image)
        # Convert bytes to a PIL Image
        return Image.open(io.BytesIO(image_bytes))
    except Exception as e:
        logging.error("Failed to decode image: %s", e)
        raise ValueError("Invalid image data")

def generate_caption(image):
    """
    Generate a caption for the given image using the BLIP model.

    Args:
        image (Image): A PIL Image object.

    Returns:
        str: The generated caption for the image.

    Raises:
        RuntimeError: If caption generation fails.
    """
    try:
        # Process the image and prepare it for the model
        model_inputs = image_processor(image, return_tensors="pt")
        # Generate a caption using the model
        model_output = captioning_model.generate(**model_inputs)
        # Decode the model output to a human-readable string
        return image_processor.decode(model_output[0], skip_special_tokens=True)
    except Exception as e:
        logging.error("Failed to generate caption: %s", e)
        raise RuntimeError("Caption generation failed")

@app.route('/caption', methods=['POST'])
def caption_image():
    """
    Endpoint to generate a caption for a given image.

    Expects a JSON payload with a base64 encoded image under the key 'image'.
    Returns a JSON response with the generated caption or an error message.

    Returns:
        Response: A Flask JSON response containing the caption or an error message.
    """
    try:
        # Retrieve JSON data from the request
        request_data = request.json
        # Extract base64 encoded image data
        base64_image = request_data.get("image", "")
        if not base64_image:
            return jsonify({"error": "No image data provided"}), 400
        
        # Decode the image and generate a caption
        image = decode_image(base64_image)
        generated_caption = generate_caption(image)
        # Return the generated caption as a JSON response
        return jsonify({"caption": generated_caption})

    except ValueError as ve:
        # Handle invalid image data
        return jsonify({"error": str(ve)}), 400
    except RuntimeError as re:
        # Handle caption generation failure
        return jsonify({"error": str(re)}), 500
    except Exception as error:
        # Handle unexpected errors
        logging.error("Unexpected error: %s", error)
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)