
from http.client import HTTPException
import uuid
import torch
from app.models.feedback import Feedback
from app.models.user import User
from app.services.sentiment_analysis.schemes import label_mapping
from app.services.sentiment_analysis.resources import load_models
from flask import jsonify
from app.utils.db import db
from app.models.feedback import Feedback
from flask import jsonify

def save_feedback(user_id, text, predicted_label, user_name):
    try:
        if not user_id or not text or not predicted_label or not user_name:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if the user already exists
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            # Create the user if they don't exist
            user = User(user_id=user_id, username=user_name)
            db.session.add(user)

        # Update username in case it changed (even if duplicates are allowed)
        if user.username != user_name:
            user.username = user_name

        # Check if feedback already exists for the user
        existing_feedback = Feedback.query.filter_by(user_id=user_id).first()

        if existing_feedback:
            # Update existing feedback
            existing_feedback.feedback_text = text
            existing_feedback.feedback_type = predicted_label
        else:
            # Create new feedback
            new_feedback = Feedback(feedback_id=str(uuid.uuid4()), user_id=user_id, feedback_text=text, feedback_type=predicted_label)
            db.session.add(new_feedback)

        # Commit all changes at once
        db.session.commit()

        return jsonify({"message": "Feedback saved successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def analyze_sentiment(data):
    try:
        # Get the text from the request body
        print(data)
        user_id = data.get("user_id")
        user_name = data.get("user_name")
        text =data.get("text")
        models = load_models()
        tokenizer = models["tokenizer"]
        model = models["model"]
        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt")

        # Perform inference
        with torch.no_grad():
            logits = model(**inputs).logits

        # Get the predicted class ID
        predicted_class_id = logits.argmax().item()

        # Map the predicted class ID to the sentiment label
        predicted_label = label_mapping[predicted_class_id]
        save_feedback(user_id,text,predicted_label,user_name)
        # Return the sentiment result
        return {"text": text, "sentiment": predicted_label}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


