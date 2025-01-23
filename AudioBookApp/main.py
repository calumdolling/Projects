"""AudioBookApp
    
    This script will convert a PDF file to an audio file.
    
    Example: python main.py sample.pdf sample.mp3
    

    Args:
        pdf_path (str): Path to the PDF file
        audio_path (str): Path to save the audio file 
        
    
    """

import PyPDF2
from gtts import gTTS
import argparse

def pdf_to_audio(pdf_path, audio_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        
        # Extract text from each page
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    
    # Convert text to speech
    tts = gTTS(text)
    tts.save(audio_path)
    
def get_args():
    parser = argparse.ArgumentParser(description="Convert a PDF file to an audio file.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file")
    parser.add_argument("audio_path", type=str, help="Path to save the audio file")
    return parser.parse_args()

def check_args(args):
    if not args.pdf_path.endswith('.pdf'):
        raise ValueError("PDF file must have a .pdf extension")
    if not args.audio_path.endswith('.mp3'):
        raise ValueError("Audio file must have a .mp3 extension")
    if not args.pdf_path:
        raise ValueError("PDF file path is required")
    if not args.audio_path:
        raise ValueError("Audio file path is required")


def main():
    args = get_args()
    check_args(args)
    pdf_to_audio(args.pdf_path, args.audio_path)
    print(f"Audio file saved at {args.audio_path}")

if __name__ == "__main__":
    main()