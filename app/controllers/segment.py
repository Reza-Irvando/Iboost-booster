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
        userId = request.args["userId"]
        err = validators.Segment(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collSegment = models.Segments(segmentName=bodyJson["segmentName"], segmentAge=bodyJson["segmentAge"], segmentClass=bodyJson["segmentClass"], segmentGender=bodyJson["segmentGender"], segmentInterest=bodyJson["segmentInterest"], segmentLocation=bodyJson["segmentLocation"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collSegment.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "segmentId": str(collSegment.id),
                "segmentName": collSegment.segmentName,
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
            Message="errorr",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def SegmentDetail():
    try:
        segmentId = request.args["segmentId"]
        collSegment = models.Segments.objects(
            id=ObjectId(segmentId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "segmentId": str(collSegment.id),
                "segmentName": collSegment.segmentName,
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
        segmentId = request.args["segmentId"]
        userId = request.args["userId"]
        err = validators.Segment(bodyJson)
        collSegment = models.Segments.objects(id=ObjectId(segmentId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collSegment:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Segment not found"
            ), HTTPStatus.BAD_REQUEST.value
        collSegment.update(segmentName=bodyJson["segmentName"], segmentAge=bodyJson["segmentAge"], segmentClass=bodyJson["segmentClass"], segmentGender=bodyJson["segmentGender"], segmentInterest=bodyJson["segmentInterest"], segmentLocation=bodyJson["segmentLocation"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update segment",
            Data=f"Segment with segmentId {segmentId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def SegmentDelete():
    try:
        segmentId = request.args["segmentId"]
        userId = request.args["userId"]
        collSegment = models.Segments.objects(
            id=ObjectId(segmentId),
            isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collSegment:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data="Segment not found"
            ), HTTPStatus.BAD_REQUEST.value
        collSegment.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete segment",
            Data=f"Segment with segmentId {segmentId} was deleted by {userId}"
        ), HTTPStatus.OK.value
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value