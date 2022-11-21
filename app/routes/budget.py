from app import app
from app.controllers import budget

app.route ("/budget/create", methods = ["POST"])(budget.BudgetCreate)
app.route ("/budget/update", methods = ["PUT"])(budget.BudgetUpdate)