from json_checker import Checker

def UnitRole(data):
    try:
        checker = Checker({
            "roleId" : str,
            "unitId": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err