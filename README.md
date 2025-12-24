# 💬 Chat App

A real-time chat application built using **Django** that allows users to communicate instantly through messages.

## 🚀 Features

- Real-time messaging
- One-to-one chat
- Responsive design
- Secure data handling

## 🛠️ Tech Stack

**Backend:**
- Django
- Django Channels (for WebSockets)

**Frontend:**
- HTML
- CSS
- JavaScript

**Database:**
- SQLite (default Django database)
- (Can be replaced with PostgreSQL or MySQL)

**Other Tools:**
- WebSockets
- Git & GitHub

## 📸 Screenshots



## 📦 Installation

Use the following code to run the project locally:

```bash
git clone https://github.com/SusanCodes-GH/Chat_App.git
cd Chat_App
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
