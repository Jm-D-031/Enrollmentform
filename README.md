# Enrollment – Django Student Profile View

An enrollment dashboard with public student profiles (white / black / orange). Use the "Login as admin" button to access the protected admin area.
Pick a class, see every student, click one to open their profile:
Personal info, Background info, Academic, Enrollment.

## Requirements
- Python 3.10 or newer  (https://www.python.org/downloads – on Windows tick "Add Python to PATH")

## Step-by-step setup

1. Extract `enrollment_django.zip`.
2. Open a terminal inside the extracted `enrollment_django` folder.
   - Windows: open the folder, click the address bar, type `cmd`, press Enter.
   - Mac/Linux: open Terminal, type `cd ` and drag the folder into it, press Enter.
3. Create a virtual environment:
   - Windows:   `python -m venv venv`
   - Mac/Linux: `python3 -m venv venv`
4. Activate it:
   - Windows:   `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install Django:            `pip install -r requirements.txt`
6. Prepare the database tables: `python manage.py makemigrations students`
7. Create the database:       `python manage.py migrate`
8. Add sample students:       `python manage.py seed_students`
9. Create your admin account: `python manage.py createsuperuser`
   (type a username and password; email can be left blank)
10. Start the server:         `python manage.py runserver`
11. Open http://127.0.0.1:8000 in your browser to view student profiles.
12. Use the "Login as admin" button to sign in with the account from step 9.

Stop the server with Ctrl+C. Next time, repeat steps 2, 4 and 10 only.

## Adding and editing students
Go to http://127.0.0.1:8000/admin/ (or click "Login as admin" on the dashboard).
- Add classes under **Classes**.
- Add students under **Students**. Grades and documents are entered on the same page.
- Changes appear on the dashboard right away.

## Project map
| Path                                   | Purpose                                  |
|----------------------------------------|------------------------------------------|
| students/models.py                     | Database tables (Class, Student, Grade, Document) |
| students/views.py                      | Loads the class, list and selected student |
| students/templates/students/           | The page layout (HTML)                   |
| students/static/students/styles.css    | Colors and look (edit `:root` to recolor) |
| students/admin.py                      | The admin forms                          |
| config/settings.py                     | Project settings                         |

## Before putting it online
Change `SECRET_KEY`, set `DEBUG = False`, and add your domain to `ALLOWED_HOSTS` in `config/settings.py`.
