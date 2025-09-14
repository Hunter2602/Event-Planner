
# Event Planner

A Django-based event management application that allows users to register, book, and manage events.
It comes with an admin interface, event booking system, and user authentication, using SQLite as the default database.

🚀 Features

User registration and authentication

Event creation and management

Event booking system (users can book events and their details are stored)

Django Admin support for managing users and events

Media & static file handling

📂 Project Structure
eventplanner/
│── manage.py                # Django management script
│── db.sqlite3                # SQLite database file
│── eventplanner/             # Project settings and configuration
│── <your_apps>/              # Django apps (events, users, etc.)
│── static/                   # Static files (CSS, JS, images)
│── media/                    # Uploaded media files

🛠️ Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/eventplanner.git
cd eventplanner

2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply database migrations
python manage.py migrate

5. Create superuser (admin access)
python manage.py createsuperuser

6. Run development server
python manage.py runserver


Open in browser 👉 http://127.0.0.1:8000/

⚙️ Requirements

Python 3.9+

Django 4.x

SQLite3 (default, can switch to PostgreSQL/MySQL)

📸 Demo Media

The project includes a sample image (woman-9398011_1280.webp) inside the media folder for demonstration/testing.

🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss the proposed changes.

📄 License

This project is licensed under the MIT License.

Do you want me to also generate a requirements.txt file for this project so it runs out of the box?

