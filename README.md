Mini Contest Web App

A Flask web application that allows users to create an account and solve coding problems. Admins can add problems with title, description, sample input. Users have to give correct output either in a textbox
or add a python code file. This app also keeps track of the scores of the users and displays them on a leaderboard


#Features:

**User Authentication**
   * User registration with secure password hashing
   * Login & Logout functionality with session management
   * Flask-Login integration

**Problem Management**
Admins can add coding problems with:
  * Title
  * Description
  * Sample Input
  * Sample Output

**Problem Solving**
Users can attempt problems by:
  *Writing output directly in a text box
  *Uploading a Python file (only `.py` files are allowed)
  *The app checks correctness and flashes messages accordingly
  *Solved problems are stored per user

**Leaderboard**
Displays all users ranked by score
  *Admins are excluded from the leaderboard


**User-Friendly Interface**

  * Clean and responsive templates with Jinja2
  * Flash messages for better user experience

#Getting Started:
1. Clone the Repository

```Bash
git clone https://github.com/HeetProgrammer/Mini-contest-web-app.git
cd Mini-contest-web-app
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Run the 'run.py' file

```bash
python run.py
```

4. Visit `http://127.0.0.1:5000/` in your browser.
6. There are 2 pre-made admin accounts.
   Account 1
     -Username: Admin1
     -Email Address: admin1@gmail.com
     -Password: 12345678
   Account 2
     -Username: Admin2
     -Email Address: admin2@gmail.com
     -Password: 12345678

7. Log into any of these and you can create problems which other users can solve!

