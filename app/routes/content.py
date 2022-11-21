from app import app
from app.controllers import content

app.route ("/content/approve", methods = ["PUT"])(content.ContentApprove)
app.route ("/content/reject", methods = ["PUT"])(content.ContentReject)
app.route ("/content/revision", methods = ["PUT"])(content.ContentRevision)
app.route ("/content/list", methods = ["GET"])(content.ContentList)
app.route ("/content/create", methods = ["POST"])(content.ContentCreate)