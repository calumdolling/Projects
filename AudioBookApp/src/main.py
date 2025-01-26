 # -*- coding: utf-8 -*-

"""AudioBookApp
    
    This script will convert a PDF file to an audio file.
    
    Example: python main.py sample.pdf sample.mp3
    

    Args:
        pdf_path (str): Path to the PDF file
        audio_path (str): Path to save the audio file
        interactive (bool): Interactive mode
        gui (bool): Launch the GUI
        merge (bool): Merge multiple PDF files into one before converting to audio
        
    Returns:
        None
    """
    
import argparse
import gui_mode
import pdf_man

    
def get_args():
    parser = argparse.ArgumentParser(description="Convert a PDF file to an audio file.")
    parser.add_argument("-p", "--pdf_paths", type=str, nargs='+', help="Paths to the PDF files")
    parser.add_argument("-a", "--audio_path", type=str, help="Path to save the audio file")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("-m", "--merge", action="store_true", help="Merge multiple PDF files into one before converting to audio")
    parser.add_argument("-g", "--gui", action="store_true", help="Launch the GUI")
    return parser.parse_args()

def check_args(args):
    if args.interactive:
        args.pdf_path, args.audio_path = interactive_mode()
    if args.merge:
        pdf_man.merge_pdf_files(args.pdf_paths, "merged.pdf")
        args.pdf_path = "merged.pdf"
    if args.gui:
        gui_mode.main()
    if not args.pdf_path.endswith('.pdf'):
        raise ValueError("PDF file must have a .pdf extension")
    if not args.audio_path.endswith('.mp3'):
        raise ValueError("Audio file must have a .mp3 extension")
    if not args.pdf_path:
        raise ValueError("PDF file path is required")
    if not args.audio_path:
        raise ValueError("Audio file path is required")

def interactive_mode():
    num_files = int(input("How many PDF files would you like to convert? "))
    pdf_paths = []
    for i in range(num_files):
        pdf_path = input(f"Enter the path to PDF file {i+1}: ")
        pdf_paths.append(pdf_path)
    audio_path = input("Enter the path to save the audio file (with .mp3 extension): ")
    return pdf_paths, audio_path

def main():
    args = get_args()
    check_args(args)
    pdf_man.pdf_to_audio(args.pdf_path, args.audio_path)
    print(f"Audio file saved at {args.audio_path}")

if __name__ == "__main__":
    main()