from directory import app, db
from flask import render_template, redirect, url_for, flash, request
from directory.models import User, Problem
from directory.forms import RegisterForm, LoginForm, ProblemForm, SolveProblemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
    problems = Problem.query.all()
    return render_template("index.html", problems=problems)


@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account Created Successfully! You are logged in as {user_to_create.username} ", category="success")
        return redirect(url_for('home_page'))
    
    if form.errors:
        for error in form.errors.values():
            flash(f"There was an error: {error}", category="danger")

    return render_template('register.html', form=form)



@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user:
            if attempted_user.check_password_correction(form.password.data):
                login_user(attempted_user)
                flash(f"Success! You are logged in as {attempted_user.username} ", category="success")
                return redirect(url_for('home_page'))
    
    for error in form.errors:
        if error:
            flash(error, category='danger')
    return render_template('login.html', form=form)



@login_required
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category="info")
    return redirect(url_for('home_page'))



@app.route('/addproblem', methods=["GET", "POST"])

def add_problem():
    if not current_user.is_authenticated or not current_user.is_admin:
        flash("You are not authorized to add problems!", category="danger")
        return redirect(url_for('home_page')
                        )
    else:
        form = ProblemForm()
        if form.validate_on_submit():
            problem_to_add = Problem(title=form.title.data, description=form.description.data, sample_input=form.sample_input.data, sample_output=form.sample_output.data)
            db.session.add(problem_to_add)
            db.session.commit()
            flash("Problem created successfully!", category="info")
            return redirect(url_for('home_page'))
    
        if form.errors:
            for error in form.errors.values():
                flash(f"There was an error: {error}", category="danger")
    
        return render_template('add_problem.html', form=form)
    

@app.route("/problems/<int:problem_id>", methods=["GET", "POST"])
@login_required
def view_problem(problem_id):
    problem = Problem.query.get(problem_id)
    if not problem in current_user.solved_problems:
        form = SolveProblemForm()
        if form.validate_on_submit() and form.validate_user_output(form.user_output):
                if form.user_output.data.strip():
                    if form.user_output.data == problem.sample_output:
                        flash(f"Congratulations!You solved the problem correctly", category="success")
                    else:
                        flash(f"Sorry!You solved the problem incorrectly. Better luck next time!", category="danger")
                
            
                elif form.code_file.data:
                    flash("Thanks for submitting file", category="info")

                current_user.solved_problems.append(problem)
                db.session.commit()
                return redirect(url_for('home_page'))
        
        if not form.validate_user_output(form.user_output):
            flash("Please fill atleast one field", category="danger")
        
        if form.code_file.data:
            if not form.code_file.data.filename.endswith(".py") and form.code_file.data:
                flash("The file should be a python code file", category="danger")
       
    

       
    
    else:
        flash(f"You have already solved this problem", category="info")
        return redirect(url_for('home_page'))
    

    return render_template("problem.html", problem=problem, form=form)











