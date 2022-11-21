from json_checker import Checker

def Category(data):
    try:
        checker = Checker({
            "categoryName": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err