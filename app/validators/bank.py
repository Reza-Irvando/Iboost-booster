from json_checker import Checker

def Bank(data):
    try:
        checker = Checker({
            "bankName": str,
            "bankCode": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err