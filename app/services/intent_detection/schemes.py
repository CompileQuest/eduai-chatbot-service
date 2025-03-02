from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    text: str
    intent_labels = ['greet-hi',
                     'greet-who_are_you',
                     'greet-good_bye',
                     'general-questions',
                     'recommendations',
                     'website-information',
                     'feedback'
                    ]
    