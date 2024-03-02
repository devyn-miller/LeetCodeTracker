from app import app, db
from app.models import models
from app.routes import auth, main

app.register_blueprint(auth.auth)
app.register_blueprint(main.main)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

