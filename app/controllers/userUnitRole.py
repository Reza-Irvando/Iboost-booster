from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def UserUnitRoleCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.UserUnitRole(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collUserUnitRole = models.UserUnitRoles(
            userId=ObjectId(userId), unitRoleId=ObjectId(bodyJson["unitRoleId"]), updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collUserUnitRole.save()
        return responses.Make(
            Status=200,
            Message="Success create User Unit Role",
            Data={
                "userUnitRoleId": str(collUserUnitRole.id),
                "userId": str(collUserUnitRole.userId.id),
                "unitRoleId": str(collUserUnitRole.unitRoleId.id),
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def UserUnitRoleUpdate():
    try:
        bodyJson = request.json
        userUnitRoleId = request.args["roleId"]
        userId = request.args["userId"]
        err = validators.UnitRole(bodyJson)
        collUserUnitRole = models.Roles.objects(id=ObjectId(userUnitRoleId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collUserUnitRole:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="User Unit Role not found"
            ), HTTPStatus.BAD_REQUEST.value
        collUserUnitRole.update(unitRoleId=bodyJson["unitRoleId"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update User Unit Role",
            Data=f"User Unit Role with unitRoleId {userUnitRoleId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value