import tkinter as tk
from tkinter import ttk, messagebox
import json
import random

QUOTES_FILE = 'quotes.json'

def load_quotes():
    try:
        with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'quotes': [], 'history': []}

def save_quotes(data):
    with open(QUOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_quote():
    quotes = quote_data['quotes']
    filtered = quotes.copy()

    author = entry_author.get().strip()
    theme = entry_theme.get().strip()

    if author:
        filtered = [q for q in filtered if q['author'].lower() == author.lower()]
    if theme:
        filtered = [q for q in filtered if q['theme'].lower() == theme.lower()]

    if not filtered:
        messagebox.showinfo("Нет цитат", "Нет цитат по заданным фильтрам.")
        return

    quote = random.choice(filtered)
    label_quote.config(text=f"{quote['text']}\n— {quote['author']}")
    quote_data['history'].append(quote)
    save_quotes(quote_data)
    refresh_history()

def refresh_history():
    history_list.delete(0, tk.END)
    for quote in quote_data['history'][::-1]:
        history_list.insert(tk.END, f"{quote['text']} ({quote['author']})")

quote_data = load_quotes()

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("600x500")

frame_input = ttk.Frame(root)
frame_input.pack(padx=10, pady=10, fill='x')

ttk.Label(frame_input, text="Фильтр по автору:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_author = ttk.Entry(frame_input)
entry_author.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="Фильтр по теме:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_theme = ttk.Entry(frame_input)
entry_theme.grid(row=1, column=1, padx=5, pady=5)

btn_generate = ttk.Button(frame_input, text="Сгенерировать цитату", command=generate_quote)
btn_generate.grid(row=2, column=0, columnspan=2, pady=10)

label_quote = ttk.Label(root, text="", font=("Arial", 12), wraplength=500)
label_quote.pack(padx=10, pady=10)

frame_history = ttk.Frame(root)
frame_history.pack(padx=10, pady=10, fill='both', expand=True)

ttk.Label(frame_history, text="История сгенерированных цитат:").pack(anchor='w')
history_list = tk.Listbox(frame_history, height=10)
history_list.pack(side='left', fill='both', expand=True)
scrollbar = ttk.Scrollbar(frame_history, orient="vertical", command=history_list.yview)
scrollbar.pack(side='right', fill='y')
history_list.config(yscrollcommand=scrollbar.set)

refresh_history()
root.mainloop()
