from app import app
from app.controllers import user

app.route ("/user/create", methods = ["POST"])(user.UserCreate)
app.route ("/user/update", methods = ["PUT"])(user.UserUpdate)