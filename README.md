
# Getting Started

To use this program, you will need Python 3.x and Django installed on your system. Clone this repository to your local machine and navigate to the project directory in your terminal.

- Run the following commands to set up the virtual environment and install dependencies:
```python
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
- Once the dependencies are installed, run the following commands to set up the database and start the server:
```python
python manage.py migrate
python manage.py runserver
```
You are able to access the application by navigating to http://localhost:8000 in your web browser.

- To view documentation simply open:
```markdown
docs
└───build
    └───html
        └───index.html
```
