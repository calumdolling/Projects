 # -*- coding: utf-8 -*-

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
import tkinter as tk
from tkinter import filedialog, messagebox

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
        merge_pdf_files(args.pdf_paths, "merged.pdf")
        args.pdf_path = "merged.pdf"
    if args.gui:
        gui_mode()
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

def merge_pdf_files(pdf_files, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    

def gui_mode():
    def add_pdfs():
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in files:
            pdf_listbox.insert(tk.END, file)

    def select_output_path():
        path = filedialog.askdirectory()
        output_path_entry.delete(0, tk.END)
        output_path_entry.insert(0, path)

    def convert():
        pdf_files = pdf_listbox.get(0, tk.END)
        output_path = output_path_entry.get()
        audio_filename = audio_name_entry.get() + ".mp3"
        if not pdf_files:
            messagebox.showerror("Error", "Please add at least one PDF file.")
            return
        if not output_path:
            messagebox.showerror("Error", "Please select an output path.")
            return
        if not audio_filename:
            messagebox.showerror("Error", "Please enter a name for the audio file.")
            return
        merge_pdf_files(pdf_files, "merged.pdf")
        pdf_to_audio("merged.pdf", f"{output_path}/{audio_filename}")
        messagebox.showinfo("Success", f"Audio file saved at {output_path}/{audio_filename}")

    root = tk.Tk()
    root.title("PDF to Audio Converter")
    root.configure(bg="#f0f0f0")

    frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
    frame.pack(padx=10, pady=10)

    button_style = {"bg": "#4CAF50", "fg": "white", "font": ("Helvetica", 12), "relief": "flat", "bd": 0, "highlightthickness": 0}

    add_pdf_button = tk.Button(frame, text="Add PDFs", command=add_pdfs, **button_style)
    add_pdf_button.grid(row=0, column=0, pady=5)

    pdf_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=50, height=10, font=("Helvetica", 10))
    pdf_listbox.grid(row=1, column=0, columnspan=2, pady=5)

    output_path_button = tk.Button(frame, text="Output Path", command=select_output_path, **button_style)
    output_path_button.grid(row=2, column=0, pady=5)

    output_path_entry = tk.Entry(frame, width=50, font=("Helvetica", 10))
    output_path_entry.grid(row=2, column=1, pady=5)

    audio_name_label = tk.Label(frame, text="Audio File Name (without .mp3):", bg="#f0f0f0", font=("Helvetica", 12))
    audio_name_label.grid(row=3, column=0, pady=5)

    audio_name_entry = tk.Entry(frame, width=50, font=("Helvetica", 10))
    audio_name_entry.grid(row=3, column=1, pady=5)

    convert_button = tk.Button(frame, text="Convert", command=convert, **button_style)
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

def main():
    args = get_args()
    check_args(args)
    pdf_to_audio(args.pdf_path, args.audio_path)
    print(f"Audio file saved at {args.audio_path}")

if __name__ == "__main__":
    main()