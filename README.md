# LASL: Live Arabic Sign Language Recognition & Translation

![LASL Banner](handsign_app/static/main_resources/images/hello-wordle.png)

## Overview

**LASL** (Live Arabic Sign Language) is a web-based application that enables real-time recognition of Arabic sign language gestures using a webcam. The system translates recognized signs into grammatically correct English and Arabic text, providing an accessible communication bridge for the deaf and hard-of-hearing community.

The project leverages:
- **Streamlit** for the live sign recognition interface
- **Django** for the main website and embedding the Streamlit app
- **TensorFlow/Keras** for gesture recognition (deep learning)
- **MediaPipe** for hand/pose landmark detection
- **Google Translate** for English-to-Arabic translation
- **LanguageTool** for local grammar correction

---

## Features

- 🎥 **Live webcam sign detection**
- 🤖 **Deep learning model for gesture recognition**
- 📝 **Automatic grammar correction (local LanguageTool server)**
- 🌐 **Instant English-to-Arabic translation**
- 🖼️ **Modern, mobile-friendly UI with custom backgrounds**
- 🔄 **Automatic detection loop (no buttons needed)**
- 🖥️ **Camera selection for multi-camera setups**
- 🔒 **User authentication via Django**

---

## Project Structure

```
handsign_project/
├── handsign_app/
│   ├── static/
│   │   └── main_resources/images/
│   ├── templates/handsign_app/
│   │   └── embedded_streamlit.html
│   ├── views.py
│   └── ...
├── lasl/
│   ├── main.py         # Streamlit app
│   ├── best_model.keras
│   └── my_functions.py
├── manage.py
└── ...
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/lasl.git
cd lasl
```

### 2. Install Python Dependencies

It is recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Key dependencies:**
- streamlit
- django
- tensorflow
- opencv-python
- mediapipe
- googletrans==4.0.0rc1
- arabic-reshaper
- python-bidi
- pillow
- language_tool_python

### 3. Download & Setup LanguageTool (for local grammar correction)

- Download LanguageTool from [https://languagetool.org/download/](https://languagetool.org/download/)
- Extract it and run the server:
  ```bash
  cd /path/to/LanguageTool-X.Y
  java -jar languagetool-server.jar --port 8081
  ```
- Make sure Java 17+ is installed (`java -version`).

### 4. Prepare the Model

- Place your trained `best_model.keras` file in the `lasl/` directory.
- If you don't have a model, you must train one using your own dataset and save it as `best_model.keras`.

### 5. Run the Streamlit App

```bash
cd lasl
streamlit run main.py
```

### 6. Run the Django Server

```bash
cd ..
python manage.py runserver
```

- Visit `http://localhost:8000/` for the main site.
- The Streamlit app will be embedded via an iframe.

---

## Usage

- Log in to the Django website.
- Navigate to the "Start your conversation" page.
- Select your camera if prompted.
- The app will automatically start recognizing signs and display the recognized sentence, grammar correction, and Arabic translation in real time.

---

## Customization

- **Backgrounds:** Change images in `handsign_app/static/main_resources/images/`.
- **Model:** Replace `lasl/best_model.keras` with your own trained model for different gestures or languages.
- **UI:** Edit `embedded_streamlit.html` for Django-side appearance, and `main.py` for Streamlit-side logic.

---

## Troubleshooting

- **Model loading errors:** Ensure your Keras/TensorFlow version matches the one used to save the model.
- **LanguageTool errors:** Make sure the server is running and Java 17+ is installed.
- **Camera not found:** Check permissions and that your webcam is connected.
- **Streamlit rerun issues:** Upgrade Streamlit to the latest version.

---

## License

This project is for academic and research purposes. For commercial use, please contact the authors.

---

## Acknowledgements

- [MediaPipe](https://mediapipe.dev/)
- [TensorFlow](https://www.tensorflow.org/)
- [Streamlit](https://streamlit.io/)
- [LanguageTool](https://languagetool.org/)
- [Google Translate](https://cloud.google.com/translate)
- [Django](https://www.djangoproject.com/)

---

## Contact

For questions, suggestions, or contributions, please open an issue or
