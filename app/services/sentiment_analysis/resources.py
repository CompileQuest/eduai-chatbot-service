from setfit import SetFitModel

from functools import lru_cache
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Cache only the model loading
@lru_cache(maxsize=1)
def load_sentiment_analysis_model():
    
    
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
    return {"tokenizer" : tokenizer, "model":model}

def load_models():
    # Just load the model with a separate cache for the model itself
    models= load_sentiment_analysis_model()
    
    return models
