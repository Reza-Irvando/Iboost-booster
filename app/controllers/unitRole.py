from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def UnitRoleCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.UnitRole(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collUnitRole = models.UnitRoles(
            roleId=ObjectId(bodyJson["roleId"]), unitId=ObjectId(bodyJson["unitId"]), updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collUnitRole.save()
        return responses.Make(
            Status=200,
            Message="Success create Unit Role",
            Data={
                "unitRoleId": str(collUnitRole.id),
                "roleId": str(collUnitRole.roleId.id),
                "unitId": str(collUnitRole.unitId.id),
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def UnitRoleUpdate():
    try:
        bodyJson = request.json
        unitRoleId = request.args["roleId"]
        userId = request.args["userId"]
        err = validators.UnitRole(bodyJson)
        collUnitRole = models.Roles.objects(id=ObjectId(unitRoleId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collUnitRole:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Unit Role not found"
            ), HTTPStatus.BAD_REQUEST.value
        collUnitRole.update(roleId=bodyJson["roleId"], unitId=bodyJson["unitId"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Role",
            Data=f"Unit Role with unitRoleId {unitRoleId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value