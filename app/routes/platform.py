from app import app
from app.controllers import platform

app.route("/master/platform/list",   methods=["GET"])(platform.PlatformList)
app.route("/master/platform/create",   methods=["POST"])(platform.PlatformCreate)
app.route("/master/platform/detail",   methods=["GET"])(platform.PlatformDetail)
app.route("/master/platform/update",   methods=["PUT"])(platform.PlatformUpdate)
app.route("/master/platform/delete",   methods=["DELETE"])(platform.PlatformDelete)