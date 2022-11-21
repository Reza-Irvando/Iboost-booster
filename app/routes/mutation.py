from app import app
from app.controllers import mutation

app.route ("/mutation/list", methods = ["GET"])(mutation.MutationList)
app.route ("/mutation/create", methods = ["POST"])(mutation.MutationCreate)
app.route ("/mutation/detail", methods = ["GET"])(mutation.MutationDetail)
app.route ("/mutation/update", methods = ["PUT"])(mutation.MutationUpdate)
app.route ("/mutation/delete", methods = ["DELETE"])(mutation.MutationDelete)