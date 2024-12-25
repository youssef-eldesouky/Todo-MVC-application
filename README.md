# Todo MVC Application

A simple, clean Todo application built with Flask and SQLite. This application allows users to create, manage, and track their tasks with a straightforward interface.

## 🚀 Technologies Used

- Python 3.x
- Flask (Web Framework)
- SQLite (Database)
- HTML/CSS
- Bootstrap (Styling)

## 📋 Features

- Create new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Reset all tasks
- Persistent storage using SQLite
- Clean and responsive user interface

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/youssef-eldesouky/Todo-MVC-application.git
cd Todo-MVC-application
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
```bash
# For Windows
venv\Scripts\activate
```

4. Install dependencies
```bash
pip install flask
```

5. Initialize the database
```bash
python setup.py
```

## 💻 Usage

1. Start the application
```bash
python app.py
```

2. Open your web browser and navigate to ```http://localhost:5000```

## 📁 Project Structure

todo_mvc/
│
├── app.py              # Main Flask application
├── models.py           # Database models and operations
├── setup.py           # Database initialization script
├── tasks.db           # SQLite database
│
└── templates/
    └── index.html     # Main template file


## 📝 License
This project is open source and available under the MIT License.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests to contribute to this project.

## ⭐ Show your support
Give a ⭐️ if this project helped you! ```
