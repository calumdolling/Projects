import tkinter as tk
from tkinter import filedialog, messagebox
# import main
import pdf_man

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
        pdf_man.merge_pdf_files(pdf_files, "merged.pdf")
        pdf_man.pdf_to_audio("merged.pdf", f"{output_path}/{audio_filename}")
        messagebox.showinfo("Success", f"Audio file saved at {output_path}/{audio_filename}")

    root = tk.Tk()
    root.title("PDF to Audio Converter")
    root.configure(bg="#f0f0f0")

    frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
    frame.pack(padx=10, pady=10)

    button_style = {"bg": "#2196F3", "fg": "white", "font": ("Helvetica", 12), "relief": "flat", "bd": 0, "highlightthickness": 0}
    button_style["activebackground"] = "#1976D2"
    button_style["activeforeground"] = "white"

    add_pdf_button = tk.Button(frame, text="Add PDFs", command=add_pdfs, **button_style)
    add_pdf_button.grid(row=0, column=0, pady=5)
    add_pdf_button.configure(borderwidth=0, highlightthickness=0, padx=10, pady=5)
    add_pdf_button.configure(highlightbackground="#2196F3", highlightcolor="#2196F3", highlightthickness=1)
    add_pdf_button.configure(borderwidth=1, relief="solid", overrelief="solid")

    pdf_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=50, height=10, font=("Helvetica", 10))
    pdf_listbox.grid(row=1, column=0, columnspan=2, pady=5)

    output_path_button = tk.Button(frame, text="Output Path", command=select_output_path, **button_style)
    output_path_button.grid(row=2, column=0, pady=5)
    output_path_button.configure(borderwidth=0, highlightthickness=0, padx=10, pady=5)
    output_path_button.configure(highlightbackground="#2196F3", highlightcolor="#2196F3", highlightthickness=1)
    output_path_button.configure(borderwidth=1, relief="solid", overrelief="solid")

    output_path_entry = tk.Entry(frame, width=50, font=("Helvetica", 10))
    output_path_entry.grid(row=2, column=1, pady=5)

    audio_name_label = tk.Label(frame, text="Audio File Name (without .mp3):", bg="#f0f0f0", font=("Helvetica", 12))
    audio_name_label.grid(row=3, column=0, pady=5)

    audio_name_entry = tk.Entry(frame, width=50, font=("Helvetica", 10))
    audio_name_entry.grid(row=3, column=1, pady=5)

    convert_button = tk.Button(frame, text="Convert", command=convert, **button_style)
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)
    convert_button.configure(borderwidth=0, highlightthickness=0, padx=10, pady=5)
    convert_button.configure(highlightbackground="#2196F3", highlightcolor="#2196F3", highlightthickness=1)
    convert_button.configure(borderwidth=1, relief="solid", overrelief="solid")

    root.mainloop()