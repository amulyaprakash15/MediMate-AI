from flask import Flask, render_template, request, jsonify
import pickle
from chatbot.gpt_chat import ask_gpt

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model/disease_model.pkl', 'rb'))

# List of symptoms (must match training data order)
symptom_list = ['fever', 'headache', 'cough', 'sore throat', 'body pain', 'nausea', 'fatigue', 'rash']

# Basic prescription dictionary
disease_prescriptions = {
    "Flu": {
        "prescription": "Rest, stay hydrated, take paracetamol if needed.",
        "diet": "Warm fluids, fruits rich in vitamin C.",
        "urgency": "Low"
    },
    "Dengue": {
        "prescription": "Drink lots of fluids, avoid painkillers like ibuprofen.",
        "diet": "Papaya leaf juice, coconut water.",
        "urgency": "High"
    },
    "Cold": {
        "prescription": "Rest, take decongestants and stay warm.",
        "diet": "Soups, warm fluids, ginger tea.",
        "urgency": "Low"
    }
}

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Disease detection route
@app.route('/detect', methods=['POST'])
def detect():
    try:
        input_text = request.form['symptoms'].lower()
        print("User input:", input_text)

        selected_symptoms = [1 if s in input_text else 0 for s in symptom_list]
        print("Binary vector:", selected_symptoms)

        prediction = model.predict([selected_symptoms])[0]
        print("Predicted disease:", prediction)

        details = disease_prescriptions.get(prediction, {
            "prescription": "Consult a doctor.",
            "diet": "Eat healthy, stay hydrated.",
            "urgency": "Moderate"
        })

        return jsonify({
            "disease": prediction,
            **details
        })
    except Exception as e:
        print("❌ Error in /detect:", e)
        return jsonify({"error": "Internal server error"}), 500

# GPT chatbot response route
@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.form['message']
        reply = ask_gpt(message)
        return jsonify({"reply": reply})
    except Exception as e:
        print("❌ Error in /chat:", e)
        return jsonify({"reply": "Sorry, something went wrong. Please try again."})

if __name__ == '__main__':
    app.run(debug=True)
symptom_list = [
    'fever', 'headache', 'cough', 'sore throat', 'body pain', 'nausea',
    'fatigue', 'rash', 'chills', 'vomiting', 'diarrhea', 'joint pain'
]
