from app import app
from app.controllers import template

app.route ("/content/template/list", methods = ["GET"])(template.TemplateList)
app.route ("/content/template/create", methods = ["POST"])(template.TemplateCreate)
app.route ("/content/template/detail", methods = ["GET"])(template.TemplateDetail)
app.route ("/content/template/update", methods = ["PUT"])(template.TemplateUpdate)
app.route ("/content/template/delete", methods = ["DELETE"])(template.TemplateDelete)