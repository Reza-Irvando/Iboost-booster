from json_checker import Checker

def Unit(data):
    try:
        checker = Checker({
            "unitName": str,
            "unitEmail": str,
            "unitAddress": str,
            "unitPhone": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err