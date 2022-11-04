from app import app
from app.controllers import paymentStatus

app.route ("/master/paymentStatus/list", methods = ["GET"])(paymentStatus.PaymentStatusList)
app.route ("/master/paymentStatus/create", methods = ["POST"])(paymentStatus.PaymentStatusCreate)
app.route ("/master/paymentStatus/detail", methods = ["GET"])(paymentStatus.PaymentStatusDetail)
app.route ("/master/paymentStatus/update", methods = ["PUT"])(paymentStatus.PaymentStatusUpdate)
app.route ("/master/paymentStatus/delete", methods = ["DELETE"])(paymentStatus.PaymentStatusDelete)