import pymongo
import tkinter as tk
from tkinter import ttk
import pdfplumber
import re

def extract_resume_information(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

            resume_info = {
                "Name": extract_field(text, "Name:"),
                "Address": extract_field(text, "Address:"),
                "Email": extract_field(text, "Email:"),
                "Telephone Number": extract_field(text, "Phone:"),
                "Education": extract_field(text, "Education:"),
                "Experience": extract_field(text, "Experience:"),
                "Certifications": extract_field(text, "Certifications:"),
                "Skills": extract_field(text, "Skills:"),
                "Languages": extract_field(text, "Languages:"),
                "Other Studies": extract_field(text, "Other Studies:")
            }

            return resume_info

    except Exception as e:
        return {"Error": str(e)}

def extract_field(text, field_name):
    pattern = re.escape(field_name) + r'(.+?)(?=' + re.escape(field_name) + r'|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""

def fetch_and_display_data():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["resume_database"]
    collection = db["resumes"]
    
    for row in tree.get_children():
        tree.delete(row)
    
    for document in collection.find():
        tree.insert("", "end", values=list(document.values()))

root = tk.Tk()
root.title("Resume Database Viewer")

fetch_button = tk.Button(root, text="Fetch Data", command=fetch_and_display_data)
fetch_button.pack()

columns = ["Name", "Address", "Email", "Telephone Number", "Education", "Experience", "Certifications", "Skills", "Languages", "Other Studies"]
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack()

root.mainloop()
