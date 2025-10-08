Movie Survey Form - Flask Web Application
Overview
This is a simple Flask web application that collects movie preferences from users through a survey form. Users enter details like their name, favorite movie, rating, genre, and whether they would recommend the movie. All submissions are displayed in a summary page. The project demonstrates basic CRUD operations, form handling, Bootstrap integration, Jinja2 templating, and essential validation for a small full-stack application.

Features
Movie survey form with multiple fields (name, favorite movie, rating, genre, recommendation)

Client-side and server-side form validation

Responsive design using Bootstrap 5

Displays all submitted survey responses

Clean project layout for easy understanding and modification

Ready to run locally, deployable to Render or Heroku

Project Structure
text
movie-survey/
│
├── app.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── survey.html
│   └── responses.html
Technologies Used
Python 3.x

Flask

HTML5 & CSS3

Bootstrap 5

Jinja2 (for templates)

Minimal JavaScript

Setup Instructions
1. Clone this repository
bash
git clone https://github.com/<your-username>/movie-survey.git
cd movie-survey
2. Create and activate a virtual environment (optional but recommended)
bash
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the application
bash
python app.py


Usage
Fill in the survey form with your movie preferences.

Submit the form — you’ll be redirected to the summary page showing all submissions made during this session.

All responses are stored in memory (will reset if the app restarts). For persistent storage, integrate with a database like SQLite.

Customizing
Modify form fields in survey.html and backend handling in app.py as needed.

Change style by editing static/style.css or Bootstrap configuration.

Screenshots
(Add screenshots showing the survey form, and the summary page with sample submissions.)

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.
