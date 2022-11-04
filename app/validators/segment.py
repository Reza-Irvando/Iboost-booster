from json_checker import Checker


def Segment(data):
    try:
        checker = Checker({
            "segmentName": "str",
            "segmentAge": "object",
            "segmentClass": "array",
            "segmentGender": "array",
            "segmentInterest": "array",
            "segmentLocation": "array"
            })
        checker.validate(data)
        return False
    except Exception as err:
        return err