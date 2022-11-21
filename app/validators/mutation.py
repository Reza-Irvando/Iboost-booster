from json_checker import Checker

def Mutation(data):
    try:
        checker = Checker({
            "fromUserUnitRoleId": str,
            "toUserUnitRoleId": str,
            "mutationAmount":float,
            "mutationNote": str,
            "mutationDC":str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err