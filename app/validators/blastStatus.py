from json_checker import Checker

def BlastStatus(data):
    try:
        checker = Checker({
            "blastStatusName": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err