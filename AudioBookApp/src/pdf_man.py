import PyPDF2
from gtts import gTTS

def pdf_to_audio(pdf_path, audio_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # page = reader.pages[0] 
        text = ""
        
        # Extract text from each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    
    # Convert text to speech
    tts = gTTS(text)
    tts.save(audio_path)
    
def merge_pdf_files(pdf_files, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()