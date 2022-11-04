from app import app
from app.controllers import category

app.route ("/master/category/list", methods = ["GET"])(category.CategoryList)
app.route ("/master/category/create", methods = ["POST"])(category.CategoryCreate)
app.route ("/master/category/detail", methods = ["GET"])(category.CategoryDetail)
app.route ("/master/category/update", methods = ["PUT"])(category.CategoryUpdate)
app.route ("/master/category/delete", methods = ["DELETE"])(category.CategoryDelete)