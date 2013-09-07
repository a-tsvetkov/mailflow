from flask import render_template, redirect, session, g

from mailflow.front import app, db, models, lm
from forms import LoginForm, RegistrationForm

from flask.ext.login import login_user, logout_user, current_user, login_required


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def index():
    if g.user.is_authenticated():
        return redirect('/dashboard')

    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        session['remember_me'] = form.remember_me.data
        login_user(user, remember=session['remember_me'])
        return redirect('/dashboard')
    return render_template('index.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.User(email=form.email.data, password=form.password.data, active=True)
        db.session.add(user)
        db.session.commit()
        return redirect('/dashboard')
    return render_template('reg.html', form=form)


@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/index")
