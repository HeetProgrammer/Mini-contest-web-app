from directory import db, app
from directory.models import User
app.app_context().push()
print("lol")
db.drop_all()
db.create_all()