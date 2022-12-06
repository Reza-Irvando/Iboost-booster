from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def PlatformList():
    try:
        collPlatform = models.Platforms.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collPlatform:
            dataArray.append({
                "platformId": str(d.id),
                "platformName": d.platformName,
                "platformCode": d.platformCode,
                "platformPrice": d.platformPrice,
            })
        return responses.Make(
            Status=200,
            Message="Success",
            Data=dataArray
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PlatformCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Platform(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collPlatform = models.Platforms(
            platformName=bodyJson["platformName"], platformCode=bodyJson["platformCode"], platformPrice=bodyJson["platformPrice"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collPlatform.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "platformId": str(collPlatform.id),
                "platformName": collPlatform.platformName,
                "platformCode": collPlatform.platformCode,
                "platformPrice": collPlatform.platformPrice
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PlatformDetail():
    try:
        platformId = request.args["platformId"]
        collPlatform = models.Platforms.objects(
            id=ObjectId(platformId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "platformId": str(collPlatform.id),
                "platformName": collPlatform.platformName,
                "platformCode": collPlatform.platformCode,
                "platformPrice": collPlatform.platformPrice
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PlatformUpdate():
    try:
        platformId = request.args["platformId"]
        userId = request.args["userId"]
        bodyJson = request.json
        err = validators.Platform(bodyJson)
        collPlatform = models.Platforms.objects(id=ObjectId(platformId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collPlatform:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Platform not found"
            ), HTTPStatus.BAD_REQUEST.value

        collPlatform.update(platformName=bodyJson["platformName"], platformCode=bodyJson["platformCode"], platformPrice=bodyJson["platformPrice"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update platform",
            Data=f"Platform with platformId {platformId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PlatformDelete():
    try:
        platformId = request.args["platformId"]
        userId = request.args["userId"]
        collPlatform = models.Platforms.objects(
            id=ObjectId(platformId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collPlatform:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data="Platform not found"
            ), HTTPStatus.BAD_REQUEST.value
        collPlatform.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete platform",
            Data=f"Platform with platformId {platformId} was deleted by {userId}"
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value