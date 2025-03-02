from setfit import SetFitModel
import os
from functools import lru_cache
from app.config import HF_TOKEN, setfit_model_id
# Cache only the model loading
@lru_cache(maxsize=1)
def load_intent_detection_model():
    
    
    return SetFitModel.from_pretrained(setfit_model_id, token=HF_TOKEN)

def load_models():
    # Just load the model with a separate cache for the model itself
    model = load_intent_detection_model()
    models = {"intent_detection": model}
    return models
