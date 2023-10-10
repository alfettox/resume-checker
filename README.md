# Resume Checker

## Overview

The Resume Checker is a Python application that allows you to extract and view resume information from PDF files and store it in a MongoDB database. The graphical user interface (GUI) built with Tkinter provides an easy way to interact with the database.

## Features

- Extract resume information from PDF files.
- Store extracted information in a MongoDB database.
- View stored resume data in a user-friendly interface.

## Requirements

- Python 3.x
- Tkinter
- pdfplumber
- pymongo
- MongoDB (running locally or on a remote server)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/resume-checker.git
   cd resume-checker
Install dependencies:

### shell
Copy code
pip install pdfplumber pymongo
Make sure MongoDB is running and accessible at mongodb://localhost:27017/. Update the MongoDB connection details in the code if necessary.

Run the application:

### shell
Copy code
python main.py
Click the "Fetch Data" button to retrieve resume information from the MongoDB database.

Use the GUI to interact with the database and view stored resume data.

## Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository on GitHub.

Clone your forked repository locally:

```
git clone https://github.com/alfettox/resume-checker.git
cd resume-checker
Create a new branch for your feature or bug fix:

git checkout -b feature/your-feature-name
Make your changes and commit them:


git commit -m "Add your commit message here"
Push your changes to your GitHub fork:

git push origin feature/your-feature-name
Create a pull request on the main repository's GitHub page.
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.