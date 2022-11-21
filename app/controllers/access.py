from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def CategoryList():
    try:
        collAccess = models.Access.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collAccess:
            dataArray.append({
                "accessId": str(d.id),
                "accessName": d.accessName,
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

def AccessCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Access(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collAccess = models.Access(
            accessName=bodyJson["accessName"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collAccess.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "accessId": str(collAccess.id),
                "accessName": collAccess.accessName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def AccessDetail():
    try:
        accessId = request.args["accessId"]
        collAccess = models.Access.objects(
            id=ObjectId(accessId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "accessId": str(collAccess.id),
                "accessName": collAccess.accessName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def AccessUpdate():
    try:
        bodyJson = request.json
        accessId = request.args["accessId"]
        userId = request.args["userId"]
        err = validators.Access(bodyJson)
        collAccess = models.Access.objects(id=ObjectId(accessId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collAccess:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Access not found"
            ), HTTPStatus.BAD_REQUEST.value
        collAccess.update(accessName=bodyJson["accessName"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Access",
            Data=f"Access with accessId {accessId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def AccessDelete():
    try:
        accessId = request.args["accessId"]
        userId = request.args["userId"]
        collAccess = models.Access.objects(
            id=ObjectId(accessId),
            isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collAccess:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data="Access not found"
            ), HTTPStatus.BAD_REQUEST.value
        collAccess.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete Access",
            Data=f"Access with accessId {accessId} was deleted by {userId}"
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value