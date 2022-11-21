from app import app
from app.controllers import unit

app.route ("/unit/create", methods = ["POST"])(unit.UnitCreate)
app.route ("/unit/update", methods = ["PUT"])(unit.UnitUpdate)
app.route ("/unit/ParentGet", methods = ["PUT"])(unit.UnitParentGet)