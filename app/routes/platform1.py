from app import app
from app.controllers import platform1

app.route("/master/platform/list",   methods=["GET"])(platform1.PlatformList)
app.route("/master/platform/create",   methods=["POST"])(platform1.PlatformCreate)
app.route("/master/platform/detail",   methods=["GET"])(platform1.PlatformDetail)
app.route("/master/platform/update",   methods=["PUT"])(platform1.PlatformUpdate)
app.route("/master/platform/delete",   methods=["DELETE"])(platform1.PlatformDelete)