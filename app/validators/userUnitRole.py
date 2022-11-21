from json_checker import Checker

def UserUnitRole(data):
    try:
        checker = Checker({
            "unitRoleId":str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err