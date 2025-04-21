

import os
from dotenv import load_dotenv
from openai import OpenAI
import tkinter as tk
from tkinter import scrolledtext

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("No API_KEY found. Please set it in your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)

# Function to call completion
def submit_prompt():
    prompt = prompt_entry.get()
    if not prompt:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        return
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=prompt
        )
        output = response.output_text
    except Exception as e:
        output = f"Error: {e}"
    # Display in output box
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, output)

# Setup GUI
root = tk.Tk()
root.title("OpenAI Completion GUI")
root.geometry("600x400")

# Prompt label and entry
tk.Label(root, text="Enter prompt:").pack(pady=(10, 0))
prompt_entry = tk.Entry(root, width=80)
prompt_entry.pack(pady=(0, 10))

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_prompt)
submit_btn.pack()

# Output label and box
tk.Label(root, text="Output:").pack(pady=(10, 0))
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
output_box.pack(pady=(0, 10))

root.mainloop()


