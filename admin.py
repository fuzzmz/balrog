from auslib.web.base import app, db

db.setDburi('sqlite:////tmp/bhearsum.db')
db.createTables()
app.config['SECRET_KEY'] = 'abc123'
app.config['DEBUG'] = True
app.run()