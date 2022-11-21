from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def MutationList():
    try:
        collMutation = models.Mutations.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collMutation:
            dataArray.append({
                "mutationId": str(d.id),
                "fromUserUnitRoleId": str(d.fromUserUnitRoleId.id),
                "toUserUnitRoleId": str(d.UserUnitRoleId.id),
                "mutationAmount":d.mutationAmount,
                "mutationNote": d.mutationNote
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

def MutationCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Mutation(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collMutation = models.Mutations(
            fromUserUnitRoleId=ObjectId(bodyJson["fromUserUnitRoleId"]), toUserUnitRoleId=ObjectId(bodyJson["toUserUnitRoleId"]), mutationAmount=bodyJson["mutationAmount"], mutationNote=bodyJson["mutationNote"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collMutation.save()
        return responses.Make(
            Status=200,
            Message="Success create Payment Status",
            Data={
                "mutationId": str(collMutation.id),
                "fromUserUnitRoleId": str(collMutation.fromUserUnitRoleId.id),
                "toUserUnitRoleId": str(collMutation.toUserUnitRoleId.id),
                "mutationAmount": collMutation.mutationAmount,
                "mutationNote": collMutation.mutationNote
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def MutationDetail():
    try:
        mutationId = request.args["mutationId"]
        collMutation = models.Mutations.objects(
            id=ObjectId(mutationId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "mutationId": str(collMutation.id),
                "fromUserUnitRoleId": str(collMutation.fromUserUnitRoleId.id),
                "toUserUnitRoleId": str(collMutation.toUserUnitRoleId.id),
                "mutationAmount": collMutation.mutationAmount,
                "mutationNote": collMutation.mutationNote
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def MutationUpdate():
    try:
        bodyJson = request.json
        mutationId = request.args["mutationId"]
        userId = request.args["userId"]
        err = validators.Mutation(bodyJson)
        collMutation = models.Mutations.objects(id=ObjectId(mutationId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collMutation:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Mutation not found"
            ), HTTPStatus.BAD_REQUEST.value
        collMutation.update(fromUserUnitRoleId=ObjectId(bodyJson["fromUserUnitRoleId"]), toUserUnitRoleId=ObjectId(bodyJson["toUserUnitRoleId"]), mutationAmount=bodyJson["mutationAmount"], mutationNote=bodyJson["mutationNote"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Mutation",
            Data=f"Mutation with mutationId {mutationId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def MutationDelete():
    try:
        mutationId = request.args["mutationId"]
        userId = request.args["userId"]
        collMutation = models.Mutations.objects(
            id=ObjectId(mutationId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collMutation:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data="Mutation not found"
            ), HTTPStatus.BAD_REQUEST.value
        collMutation.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete Mutation",
            Data=f"Mutation with mutationId {mutationId} was deleted by {userId}"
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value