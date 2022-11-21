from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def UnitCreate():
    try:
        userId = request.args["userId"]
        bodyJson = request.json
        err = validators.Unit(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collUnit = models.Units(
            unitName=bodyJson["unitName"], unitEmail=bodyJson["unitEmail"], unitAddress=bodyJson["unitAddress"], unitPhone=bodyJson["unitPhone"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collUnit.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "unitId": str(collUnit.id),
                "unitName": collUnit.unitName,
                "unitEmail": collUnit.unitEmail,
                "unitAddress": collUnit.unitAddress,
                "unitPhone":collUnit.unitPhone
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def UnitParentGet():
    try:
        unitId = request.args["unitId"]
        userId = request.args["userId"]
        collUnit = models.Units.objects(id=ObjectId(unitId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collUnit:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Unit not found"
            ), HTTPStatus.BAD_REQUEST.value

        collUnit.update(unitParent=ObjectId(unitId), updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly get Unit Parent",
            Data=f"Unit Parent with unitId {unitId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def UnitUpdate():
    try:
        unitId = request.args["unitId"]
        userId = request.args["userId"]
        bodyJson = request.json
        err = validators.Unit(bodyJson)
        collUnit = models.Units.objects(id=ObjectId(unitId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collUnit:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Unit not found"
            ), HTTPStatus.BAD_REQUEST.value

        collUnit.update(unitName=bodyJson["unitName"], unitEmail=bodyJson["unitEmail"], unitAddress=bodyJson["unitAddress"], unitPhone=bodyJson["unitPhone"], unitParent=ObjectId(unitId), updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Unit",
            Data=f"Unit with unitId {unitId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value