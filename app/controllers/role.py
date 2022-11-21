from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def RoleCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Role(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collUnit = models.Units.objects(id=ObjectId(bodyJson["unitId"]), isActive=True, isDelete=False)
        if not collUnit:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="UnitId not found"
            ), HTTPStatus.BAD_REQUEST.value
        collRole = models.Roles(
            roleName=bodyJson["roleName"], unitId=bodyJson["unitId"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collRole.save()
        return responses.Make(
            Status=200,
            Message="Success create Payment Status",
            Data={
                "roleId": str(collRole.id),
                "roleName": collRole.roleName,
                "unitId":str(collRole.unitId.id)
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def RoleUpdate():
    try:
        bodyJson = request.json
        roleId = request.args["roleId"]
        userId = request.args["userId"]
        err = validators.Role(bodyJson)
        collRole = models.Roles.objects(id=ObjectId(roleId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collRole:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Role not found"
            ), HTTPStatus.BAD_REQUEST.value
        collRole.update(roleName=bodyJson["roleName"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Role",
            Data=f"Role with roleId {roleId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value