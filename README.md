# Random Quote Generator — пошаговая инструкция по созданию приложения

## 1. Структура проекта

Создайте папку `quote_generator` и добавьте в неё:
- файл `main.py` — основной код приложения;
- файл `quotes.json` — для хранения цитат и истории;
- файл `.gitignore` — чтобы не отслеживать временные файлы;
- файл `README.md` — описание проекта.

## 2. Основной код (`main.py`)

```python
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
```

## 3. Файл `.gitignore`

```
__pycache__/
*.pyc
*.log
*.swp
*.bak
```
*(Если хотите хранить данные в Git — уберите `quotes.json` из .gitignore)*

## 4. Пример файла `quotes.json`

```json
{
  "quotes": [
    {
      "text": "Жизнь — это то, что происходит, когда ты занят другими планами.",
      "author": "Джон Леннон",
      "theme": "Жизнь"
    },
    {
      "text": "Величайшая слава не в том, чтобы никогда не падать, а в том, чтобы подниматься каждый раз.",
      "author": "Конфуций",
      "theme": "Мотивация"
    },
    {
      "text": "Знание — сила.",
      "author": "Фрэнсис Бэкон",
      "theme": "Знания"
    }
  ],
  "history": []
}
```

## 5. README.md (пример оформления)

```
# Random Quote Generator

**Автор:** Иван Иванов

## Описание программы

Random Quote Generator — приложение для генерации случайных цитат с графическим интерфейсом. Позволяет фильтровать цитаты по автору и теме, отображать историю сгенерированных цитат и сохранять её в файл JSON.

## Как использовать

1. Установите Python 3.x.
2. Скопируйте файлы проекта в одну папку.
3. Запустите main.py.
4. Введите автора или тему для фильтрации (по желанию) и нажмите «Сгенерировать цитату».
5. История отображается в списке ниже.
6. Данные сохраняются автоматически.

## Примеры использования

- Сгенерировать случайную цитату без фильтра.
- Отфильтровать цитаты по автору: «Конфуций».
- Отфильтровать по теме: «Мотивация».
```

## 6. Использование Git

1. Откройте терминал в папке проекта.
2. Инициализируйте репозиторий:
   ```
   git init
   ```
3. Добавьте файлы:
   ```
   git add .
   ```
4. Сделайте первый коммит:
   ```
   git commit -m "Initial commit"
   ```
5. (Опционально) Создайте репозиторий на GitHub/GitLab и залейте проект.
```
git remote add origin <ваш_репозиторий>
git push -u origin master
```
```
