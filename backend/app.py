from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import base64
import io

app = Flask(__name__)
CORS(app)

# Load BLIP model and processor
captioning_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
image_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route('/caption', methods=['POST'])
def caption_image():
    """
    Endpoint to generate a caption for a given image.
    
    Expects a JSON payload with a base64 encoded image under the key 'image'.
    Returns a JSON response with the generated caption or an error message.
    """
    try:
        # Retrieve JSON data from the request
        request_data = request.json
        
        # Extract base64 encoded image data
        base64_image = request_data.get("image", "")
        if not base64_image:
            return jsonify({"error": "No image data provided"}), 400
        
        # Decode the base64 string to bytes and open it as a PIL image
        image_bytes = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_bytes))

        # Process the image and generate a caption using the BLIP model
        model_inputs = image_processor(image, return_tensors="pt")
        model_output = captioning_model.generate(**model_inputs)
        generated_caption = image_processor.decode(model_output[0], skip_special_tokens=True)

        # Return the generated caption as a JSON response
        return jsonify({"caption": generated_caption})

    except Exception as error:
        # Return an error message in case of an exception
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)