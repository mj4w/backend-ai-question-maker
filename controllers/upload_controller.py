import os
from flask import Blueprint, request, jsonify
from config import Config
from services.pdf_service import PDFService
from services.openai_service import OpenAIService

upload_bp = Blueprint('upload', __name__)
openai_service = OpenAIService()

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filepath = os.path.join(Config.UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    extracted_text = PDFService.extract_text(filepath)

    if not extracted_text:
        return jsonify({'error': 'No text found in PDF'}), 400

    try:
        question = openai_service.generate_question(extracted_text)
        return jsonify({'question': question})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
