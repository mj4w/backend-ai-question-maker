from dotenv import dotenv_values

class Config:
    UPLOAD_FOLDER = 'uploads'
    SECRETS = dotenv_values('.env')
    OPENAI_API_KEY = SECRETS.get('GPT_KEY', None)