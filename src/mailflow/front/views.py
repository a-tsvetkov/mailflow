from mailflow.front import app

@app.route('/')
@app.route('/index')
def index():
    return "Mailflow landing page"