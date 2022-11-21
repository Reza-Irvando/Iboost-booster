from json_checker import Checker

def Budget(data):
    try:
        checker = Checker({
            "budgetsAmount": float
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err