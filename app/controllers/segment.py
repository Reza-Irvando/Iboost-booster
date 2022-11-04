from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators


def SegmentList():
    try:
        collSegment = models.Segments.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collSegment:
            dataArray.append({
                "segmentId": str(d.id),
                "segmentName": d.segmentName,
                "segmentAge": d.segmentAge,
                "segmentClass": d.segmentClass,
                "segmentGender": d.segmentGender,
                "segmentInterest": d.segmentInterest,
                "segmentLocation": d.segmentLocation
            })
        return responses.Make(
            Status=200,
            Message="success",
            Data=dataArray
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def SegmentCreate():
    try:
        bodyJson = request.json
        userId = ObjectId(request.args["userId"])
        err = validators.Segment(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collSegment = models.Segments(
            segmentName=bodyJson["categoryName"], segmentAge=bodyJson["segmentAge"], segmentClass=bodyJson["segmentClass"], segmentGender=bodyJson["segmentGender"], segmentLocation=bodyJson["segmentInterest"], updatedBy=userId, createdBy=userId)
        collSegment.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collSegment.id),
                "categoryName": collSegment.segmentName,
                "segmentAge": collSegment.segmentAge,
                "segmentClass": collSegment.segmentClass,
                "segmentGender": collSegment.segmentGender,
                "segmentInterest": collSegment.segmentInterest,
                "segmentLocation": collSegment.segmentLocation
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def SegmentDetail():
    try:
        segmentId = ObjectId(request.args["segmentId"])
        collSegment = models.Segments.objects(
            id=segmentId,
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collSegment.id),
                "categoryName": collSegment.segmentName,
                "segmentAge": collSegment.segmentAge,
                "segmentClass": collSegment.segmentClass,
                "segmentGender": collSegment.segmentGender,
                "segmentInterest": collSegment.segmentInterest,
                "segmentLocation": collSegment.segmentLocation
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def SegmentUpdate():
    try:
        bodyJson = request.json
        segmentId = ObjectId(request.args["segmentId"])
        userId = ObjectId(request.args["userId"])
        err = validators.Segment(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collSegment = models.Segments.objects(id=segmentId, isActive=True, isDelete=False).update(
            segmentName=bodyJson["categoryName"], segmentAge=bodyJson["segmentAge"], segmentClass=bodyJson["segmentClass"], segmentGender=bodyJson["segmentGender"], segmentLocation=bodyJson["segmentInterest"], updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collSegment.id),
                "categoryName": collSegment.segmentName,
                "segmentAge": collSegment.segmentAge,
                "segmentClass": collSegment.segmentClass,
                "segmentGender": collSegment.segmentGender,
                "segmentInterest": collSegment.segmentInterest,
                "segmentLocation": collSegment.segmentLocation
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def SegmentDelete():
    try:
        segmentId = ObjectId(request.args["segmentId"])
        userId = ObjectId(request.args["userId"])
        collSegment = models.Segments.objects(
            id=segmentId,
            isActive=True, isDelete=False).update(isActive=False, isDelete=True, updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collSegment.id),
                "categoryName": collSegment.segmentName,
                "segmentAge": collSegment.segmentAge,
                "segmentClass": collSegment.segmentClass,
                "segmentGender": collSegment.segmentGender,
                "segmentInterest": collSegment.segmentInterest,
                "segmentLocation": collSegment.segmentLocation
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
