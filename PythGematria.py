# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog, messagebox
from tkhtmlview import HTMLLabel

# Comprehensive Greek gematria dictionary
greek_gematria = {
    'α': 1, 'Α': 1, 'β': 2, 'Β': 2, 'γ': 3, 'Γ': 3, 'δ': 4, 'Δ': 4, 'ε': 5, 'Ε': 5,
    'ϝ': 6, 'Ϝ': 6, 'ζ': 7, 'Ζ': 7, 'η': 8, 'Η': 8, 'θ': 9, 'Θ': 9, 'ι': 10, 'Ι': 10,
    'κ': 20, 'Κ': 20, 'λ': 30, 'Λ': 30, 'μ': 40, 'Μ': 40, 'ν': 50, 'Ν': 50, 'ξ': 60, 'Ξ': 60,
    'ο': 70, 'Ο': 70, 'π': 80, 'Π': 80, 'ϙ': 90, 'Ϙ': 90, 'ρ': 100, 'Ρ': 100, 'σ': 200, 'Σ': 200,
    'τ': 300, 'Τ': 300, 'υ': 400, 'Υ': 400, 'φ': 500, 'Φ': 500, 'χ': 600, 'Χ': 600, 
    'ψ': 700, 'Ψ': 700, 'ω': 800, 'Ω': 800, 'Ͳ': 900, 'Ͳ': 900
}

def calculate_gematria(word):
    return sum(greek_gematria.get(char, 0) for char in word)

def load_words_and_definitions(words_filepath, definitions_filepath):
    try:
        with open(words_filepath, 'r', encoding='utf-8') as words_file, open(definitions_filepath, 'r', encoding='utf-8') as defs_file:
            words = []
            definitions = {}
            for word_line, def_line in zip(words_file, defs_file):
                word = word_line.strip().split()[0]
                definition = def_line.strip()
                words.append(word)
                definitions[word] = definition
        return words, definitions
    except Exception as e:
        messagebox.showerror("Error", f"Error reading text files: {e}")
        return None, None

def find_words_by_value(words, value):
    compatible_words = []
    for word in words:
        if calculate_gematria(word) == value:
            compatible_words.append(word)
    return compatible_words

def find_compatible_numbers_and_words(words, input_word):
    value = calculate_gematria(input_word)
    compatible_words = find_words_by_value(words, value)
    return value, compatible_words

class GematriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Greek Gematria Calculator")
        
        self.words = []
        self.definitions = {}
        self.create_widgets()
        
    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load Words and Definitions", command=self.load_words_and_definitions)
        self.load_button.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        
        self.search_by_number_label = tk.Label(self.root, text="Search by Number:")
        self.search_by_number_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.search_by_number_entry = tk.Entry(self.root)
        self.search_by_number_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.search_by_number_button = tk.Button(self.root, text="Search", command=self.search_by_number)
        self.search_by_number_button.grid(row=1, column=2, padx=10, pady=10)
        
        self.search_by_word_label = tk.Label(self.root, text="Search by Word:")
        self.search_by_word_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.search_by_word_entry = tk.Entry(self.root)
        self.search_by_word_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.search_by_word_button = tk.Button(self.root, text="Search", command=self.search_by_word)
        self.search_by_word_button.grid(row=2, column=2, padx=10, pady=10)
        
        self.results_label = tk.Label(self.root, text="Results:")
        self.results_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        
        self.definitions_label = tk.Label(self.root, text="Definitions:")
        self.definitions_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.definitions_html = HTMLLabel(self.root, html="")
        self.definitions_html.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")
        
    def load_words_and_definitions(self):
        words_filepath = filedialog.askopenfilename(title="Open Words File", filetypes=(("Text Files", "*.txt"),))
        definitions_filepath = filedialog.askopenfilename(title="Open Definitions File", filetypes=(("Text Files", "*.txt"),))
        if words_filepath and definitions_filepath:
            self.words, self.definitions = load_words_and_definitions(words_filepath, definitions_filepath)
            if self.words is not None and self.definitions is not None:
                messagebox.showinfo("Success", "Words and definitions loaded successfully.")
            else:
                messagebox.showerror("Error", "Failed to load words and definitions.")
    
    def search_by_number(self):
        number = self.search_by_number_entry.get()
        if not number.isdigit():
            messagebox.showerror("Error", "Please enter a valid number.")
            return
        number = int(number)
        result_words = find_words_by_value(self.words, number)
        self.display_results(f"Words with gematria value {number}:", result_words)
    
    def search_by_word(self):
        word = self.search_by_word_entry.get()
        if not word:
            messagebox.showerror("Error", "Please enter a valid word.")
            return
        value, compatible_words = find_compatible_numbers_and_words(self.words, word)
        results_message = f"Gematria value of '{word}': {value}\nWords with the same gematria value:"
        self.display_results(results_message, compatible_words)
        self.display_definitions(compatible_words)
    
    def display_results(self, message, words):
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"{message}\n{', '.join(words)}")
    
    def display_definitions(self, words):
        html_content = "<html><body>"
        for word in words:
            definition = self.definitions.get(word, 'No definition found')
            html_content += f"<p><b>{word}:</b> {definition}</p>"
        html_content += "</body></html>"
        self.definitions_html.set_html(html_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = GematriaApp(root)
    root.mainloop()
