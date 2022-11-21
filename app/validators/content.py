from json_checker import Checker

def Content(data):
    try:
        checker = Checker({
            "platformId": str,
            "contentMessage": {
                "contentMessage 1":str,
                "contentMessage 2":str
            },
            "payloadMessage": {
                "payloadMessage 1":str,
                "payloadMessage 2":str
            },
            "duration": int,
            "segmentId": str,
            "targetEstimate": int,
            "price": float
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err