import numpy as np
from tensorflow.keras.models import load_model
from googletrans import Translator
import language_tool_python

actions = np.array([
    'a', 'n', 'o', 'name', 'what', 'r', 'your', 'help', 'please', 'professor', 'hello', 'thank you'
])
model = load_model('best_model.keras')
translator = Translator()
lt_tool = language_tool_python.LanguageToolPublicAPI('en-US')
custom_corrections = {
    "Name Nora": "My name is Nora",
    "Name Ahmed": "My name is Ahmed",
    "What your name": "What is your name?",
}

def predict_from_keypoints(keypoints_list):
    last_prediction = None
    sentence = []
    grammar_result = ""
    arabic_translation = ""

    if len(keypoints_list) == 10:
        keypoints_np = np.array(keypoints_list)
        prediction = model.predict(keypoints_np[np.newaxis, :, :])
        if np.amax(prediction) > 0.9:
            pred = actions[np.argmax(prediction)]
            if last_prediction != pred:
                sentence.append(pred)
                last_prediction = pred

    if sentence:
        sentence[0] = sentence[0].capitalize()
        text = ' '.join(sentence)
        grammar_result = lt_tool.correct(text)
        if grammar_result in custom_corrections:
            grammar_result = custom_corrections[grammar_result]
        try:
            arabic_translation = translator.translate(grammar_result, src='en', dest='ar').text
        except Exception as e:
            arabic_translation = f"Translation error: {e}"

    return {
        "sentence": ' '.join(sentence),
        "grammar_result": grammar_result,
        "arabic_translation": arabic_translation
    }