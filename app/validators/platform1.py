from json_checker import Checker

def Platform(data):
    try:
        checker = Checker({
            "platformName": str,
            "platformCode": str,
            "platformPrice": float
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err