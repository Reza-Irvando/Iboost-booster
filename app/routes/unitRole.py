from app import app
from app.controllers import unitRole

app.route ("/unitRole/create", methods = ["POST"])(unitRole.UnitRoleCreate)
app.route ("/unitRole/update", methods = ["PUT"])(unitRole.UnitRoleUpdate)