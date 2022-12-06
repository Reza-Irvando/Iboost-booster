from json_checker import Checker


def Template(data):
    try:
        checker = Checker({
            "templateName": str, 
            "templateContent": str, 
            "templateLength": int, 
            "categoryId": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err