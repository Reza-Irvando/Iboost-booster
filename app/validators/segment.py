from json_checker import Checker


def Segment(data):
    try:
        checker = Checker({
            "segmentName": str,
            "segmentAge": {
                "min age": str,
                "max age": str
            },
            "segmentClass": [str],
            "segmentGender": [str],
            "segmentInterest": [str],
            "segmentLocation": [str]
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err