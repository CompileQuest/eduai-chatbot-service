from flask import jsonify

from app.services.intent_detection.resources import load_models


def detect_intent(message):
    if not message.text or message.text.strip() == "":
        return {"error": "You must provide a text"},400
    models = load_models()
    # Ensure that 'models' is the actual dictionary returned by load_models()
    model = models["intent_detection"]

    # Get the predicted probabilities from the model
    intent_probs = model.predict_proba([message.text]).tolist()[0]

    # Find the maximum confidence and its index
    max_prob_value = max(intent_probs)
    max_prob_index = intent_probs.index(max_prob_value)

    # Use the index to get the corresponding intent label
    intent_name = message.intent_labels[max_prob_index]

    return {
        "result": {
            "text": message.text,
            "intent": {
                "name": intent_name,
                "confidence": max_prob_value,
            }
        }
    }
