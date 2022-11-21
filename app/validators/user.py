from json_checker import Checker


def User(data):
    try:
        checker = Checker({
            "userName": str,
            "userEmail": str,
            "userPassword": str,
            "userPin": str,
            "userFirstName": str,
            "userLastName": str,
            "userPhoneNumber": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err
    
