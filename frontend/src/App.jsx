import React, { useState } from "react";
import axios from "axios";

/**
 * App component for the Image Captioning application.
 * Allows users to upload an image and generate a caption using a backend service.
 */
function App() {
    // State to store the selected image as a base64 string
    const [selectedImage, setSelectedImage] = useState(null);
    // State to store the generated caption for the image
    const [generatedCaption, setGeneratedCaption] = useState("");
    // State to store any error messages
    const [errorMessage, setErrorMessage] = useState("");

    // Styles object to manage inline styles for the component
    const styles = {
        container: { padding: "20px", maxWidth: "600px", margin: "0 auto" },
        imagePreview: { width: "100%", maxHeight: "300px" },
        button: { padding: "10px", marginTop: "20px", cursor: "pointer" },
        errorText: { marginTop: "20px", color: "red" },
        captionText: { marginTop: "20px" }
    };

    /**
     * Handles the image upload event.
     * Reads the uploaded file and converts it to a base64 string.
     * @param {Object} event - The file input change event.
     */
    const handleImageUpload = (event) => {
        const [uploadedFile] = event.target.files; // Destructure to get the first file
        if (uploadedFile) {
            const fileReader = new FileReader();
            // Set the selected image state when file reading is complete
            fileReader.onloadend = () => setSelectedImage(fileReader.result);
            // Set an error message if file reading fails
            fileReader.onerror = () => setErrorMessage("Failed to read file.");
            // Read the file as a data URL (base64 string)
            fileReader.readAsDataURL(uploadedFile);
        }
    };

    /**
     * Sends the selected image to the backend to generate a caption.
     * Updates the generated caption or error message based on the response.
     */
    const handleGenerateCaption = async () => {
        try {
            setErrorMessage(""); // Clear any previous error messages
            setGeneratedCaption("Generating caption..."); // Indicate caption generation in progress

            // Extract the base64 part of the image data
            const base64ImageData = selectedImage?.split(",")[1];
            // Send a POST request to the backend with the image data
            const response = await axios.post("http://127.0.0.1:5000/caption", { image: base64ImageData });

            // Update the generated caption with the response or a default message
            setGeneratedCaption(response.data?.caption || "No caption generated.");
        } catch (err) {
            // Set an error message if the request fails
            setErrorMessage("Failed to generate caption. Please try again.");
        }
    };

    return (
        <div style={styles.container}>
            <h1>Image Captioning App</h1>
            {/* File input for uploading images */}
            <input type="file" accept="image/*" onChange={handleImageUpload} />
            {/* Display the selected image if available */}
            {selectedImage && (
                <div style={{ marginTop: "20px" }}>
                    <img src={selectedImage} alt="Preview" style={styles.imagePreview} />
                </div>
            )}
            {/* Button to trigger caption generation */}
            <button onClick={handleGenerateCaption} style={styles.button}>
                Generate Caption
            </button>
            {/* Display the generated caption if available */}
            {generatedCaption && <p style={styles.captionText}>Caption: {generatedCaption}</p>}
            {/* Display an error message if available */}
            {errorMessage && <p style={styles.errorText}>{errorMessage}</p>}
        </div>
    );
}

export default App;
