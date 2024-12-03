import React, { useState } from "react";
import axios from "axios";

function App() {
    const [image, setImage] = useState(null);
    const [caption, setCaption] = useState("");
    const [error, setError] = useState("");

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setImage(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleGenerateCaption = async () => {
        try {
            setError("");
            setCaption("Generating caption...");

            const base64Image = image.split(",")[1]; // Extract base64 part
            const response = await axios.post("http://127.0.0.1:5000/caption", { image: base64Image });

            setCaption(response.data.caption || "No caption generated.");
        } catch (err) {
            setError("Failed to generate caption. Please try again.");
        }
    };

    return (
        <div style={{ padding: "20px", maxWidth: "600px", margin: "0 auto" }}>
            <h1>Image Captioning App</h1>
            <input type="file" accept="image/*" onChange={handleImageUpload} />
            {image && (
                <div style={{ marginTop: "20px" }}>
                    <img src={image} alt="Preview" style={{ width: "100%", maxHeight: "300px" }} />
                </div>
            )}
            <button
                onClick={handleGenerateCaption}
                style={{ padding: "10px", marginTop: "20px", cursor: "pointer" }}
            >
                Generate Caption
            </button>
            {caption && <p style={{ marginTop: "20px" }}>Caption: {caption}</p>}
            {error && <p style={{ marginTop: "20px", color: "red" }}>{error}</p>}
        </div>
    );
}

export default App;
