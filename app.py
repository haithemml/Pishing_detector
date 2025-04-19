from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import pickle

# Charger le modèle TensorFlow et le scaler
model = tf.keras.models.load_model("phishing_bert_model", custom_objects={"KerasLayer": tf.keras.layers.Layer})
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        email_content = request.form['email_content']
        num_values = [
            float(request.form.get("num_words", 0)),
            float(request.form.get("num_unique_words", 0)),
            float(request.form.get("num_stopwords", 0)),
            float(request.form.get("num_links", 0)),
            float(request.form.get("num_unique_domains", 0)),
            float(request.form.get("num_email_addresses", 0)),
            float(request.form.get("num_spelling_errors", 0)),
            float(request.form.get("num_urgent_keywords", 0))
        ]

        X_num = scaler.transform([num_values])
        X_text = [email_content]

        result = model.predict({"text": X_text, "numerical": X_num})[0][0]
        prediction = "Phishing" if result > 0.5 else "Legitime"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
