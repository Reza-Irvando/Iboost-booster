from json_checker import Checker

def Access(data):
    try:
        checker = Checker({
            "accessName": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err