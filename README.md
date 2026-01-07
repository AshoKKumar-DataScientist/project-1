# Cricbuzz Live Cricket Analytics | Streamlit + MySQL

This web app shows:
- Live cricket matches from Cricbuzz API
- Player analytics & leaderboards
- SQL query execution
- CRUD operations

## How to run

### 1. Install modules
pip install -r requirements.txt

### 2. Setup database
create database cricketdb;

### 3. Add .env
DB_HOST=localhost
DB_USER=root
DB_PASS=yourpassword
DB_NAME=cricketdb

### 4. Run app
streamlit run app.py
