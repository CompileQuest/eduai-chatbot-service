import os
from dotenv import load_dotenv

# Load environment variables from a .env file if you’re using one
load_dotenv()

# Hugging Face token
HF_TOKEN = os.getenv("HF_TOKEN", None)
setfit_model_id = os.getenv("setfit_model_id", "HussienAhmad/SFT_GradProject")
SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_SQLALCHEMY_DATABASE_URI')
print(SQLALCHEMY_DATABASE_URI)