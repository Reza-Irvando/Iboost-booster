from json_checker import Checker

def PaymentStatus(data):
    try:
        checker = Checker({
            "paymentStatusName": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err