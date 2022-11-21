from app import app
from app.controllers import userUnitRole

app.route ("/userUnitRole/create", methods = ["POST"])(userUnitRole.UserUnitRoleCreate)
app.route ("/userUnitRole/update", methods = ["PUT"])(userUnitRole.UserUnitRoleUpdate)