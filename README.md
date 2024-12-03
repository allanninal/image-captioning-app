
# AI-Powered Image Captioning App

This project is an AI-powered image captioning app that allows users to upload images and generates descriptive captions using Salesforce’s BLIP model. It integrates modern web development tools like ReactJS, Flask, and Hugging Face’s AI models to deliver an interactive and responsive experience.

---

## Features

- **Image Upload**: Upload images directly from your device.
- **AI-Generated Captions**: Uses BLIP to produce human-like captions.
- **Responsive UI**: Built with ReactJS for a clean and modern interface.

---

## Tech Stack

### **Frontend**
- ReactJS with Vite for fast development and HMR.
- Axios for API communication.

### **Backend**
- Flask for serving the API.
- Hugging Face’s Transformers for AI model inference.

### **AI Model**
- BLIP (Bootstrapped Language-Image Pretraining) from Salesforce.

---

## Installation and Setup

### Clone the Repository
Start by cloning the repository from GitHub:
```bash
git clone git@github.com:allanninal/image-captioning-app.git
cd image-captioning-app
```

### Backend Setup
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install the dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the React development server:
   ```bash
   npm run dev
   ```

---

## Usage

1. **Upload an Image**: Use the app interface to upload an image.
2. **Generate Captions**: Click the "Generate Caption" button to see AI-generated captions for the uploaded image.
3. **Explore Outputs**: View descriptive and context-aware captions directly on the app.

---

## How It Works

1. The React frontend allows users to upload images and sends them to the Flask backend.
2. Flask processes the image using Hugging Face's BLIP model and returns a caption.
3. The caption is displayed in the frontend, providing users with a seamless experience.

---

## What’s Next?

- Add drag-and-drop functionality for image uploads.
- Generate multiple captions for a single image.
- Enhance styling with Tailwind CSS or Material-UI.
- Deploy the app to platforms like AWS, Heroku, or Vercel.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Support

If you find this project helpful, consider supporting me on Ko-fi:  
[ko-fi.com/allanninal](https://ko-fi.com/allanninal)
