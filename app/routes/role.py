from app import app
from app.controllers import role

app.route ("/role/create", methods = ["POST"])(role.RoleCreate)
app.route ("/role/update", methods = ["PUT"])(role.RoleUpdate)