# chatbot/gpt_chat.py

import random

def ask_gpt(message):
    message = message.lower()

    # Emergency check
    if any(word in message for word in ["emergency", "severe pain", "bleeding", "chest pain", "can't breathe"]):
        return "⚠️ This may be an emergency. Please call emergency services or go to the nearest hospital immediately."

    # Greeting
    if "my name is" in message or "i am" in message:
        name = message.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {name}! How can I assist you with your health today?"

    # Symptom-based smart replies
    if "fever" in message:
        return "🌡️ Fever may indicate an infection. Stay hydrated, rest, and monitor your temperature regularly."
    elif "headache" in message:
        return "🤕 A headache can be due to stress, screen time, dehydration or sleep issues. Try resting and drinking water."
    elif "cough" in message:
        return "😷 A persistent cough could mean a viral infection. Stay warm, drink warm fluids, and use a cough suppressant if needed."
    elif "fatigue" in message or "tired" in message:
        return "💤 Fatigue might come from lack of sleep, poor nutrition or viral illness. Take rest and maintain good hydration."
    elif "sore throat" in message:
        return "🗣️ A sore throat may result from viral infections. Gargle with warm salt water and avoid cold foods."
    elif "nausea" in message:
        return "🤢 Nausea may indicate indigestion or stomach infection. Try drinking ginger tea or ORS solution."
    elif "rash" in message:
        return "🩹 Skin rashes may be allergic or viral. Keep the area clean and apply a soothing cream like calamine."
    elif "diarrhea" in message:
        return "🚽 Diarrhea could be due to a stomach bug. Stay hydrated with ORS, avoid dairy, and eat bland foods."

    # General random health tips
    tips = [
        "💧 Stay hydrated — drink at least 8 glasses of water daily.",
        "🥦 Eat a balanced diet rich in fruits and vegetables.",
        "🏃 Regular exercise boosts immunity and reduces stress.",
        "🛌 Get 7–8 hours of sleep every night.",
        "🧼 Wash hands regularly to avoid infections.",
        "🚭 Avoid smoking and limit alcohol consumption.",
        "🧘 Practice mindfulness or yoga to reduce anxiety.",
        "🩺 Schedule annual health checkups even if you feel fine."
    ]

    # Doctor recommendation if unsure
    doctor_phrases = [
        "If you're unsure, it's always best to consult a medical professional.",
        "For a proper diagnosis, please see your doctor.",
        "I recommend booking a check-up if symptoms persist.",
    ]

    # Fallback response with tips
    return f"{random.choice(doctor_phrases)} Here's a tip: {random.choice(tips)}"
