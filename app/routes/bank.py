from app import app
from app.controllers import bank

app.route("/master/bank/list",   methods=["GET"])(bank.BankList)
app.route("/master/bank/create",   methods=["POST"])(bank.BankCreate)
app.route("/master/bank/detail",   methods=["GET"])(bank.BankDetail)
app.route("/master/bank/update",   methods=["PUT"])(bank.BankUpdate)
app.route("/master/bank/delete",   methods=["DELETE"])(bank.BankDelete)