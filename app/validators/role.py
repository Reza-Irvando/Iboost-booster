from json_checker import Checker

def Role(data):
    try:
        checker = Checker({
            "roleName" : str,
            "unitId": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err