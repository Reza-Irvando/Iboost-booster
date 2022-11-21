from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def BlastStatusList():
    try:
        collBlastStatus = models.BlastStatus.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collBlastStatus:
            dataArray.append({
                "blastStatusId": str(d.id),
                "blastStatusName": d.blastStatusName,
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

def BlastStatusCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.BlastStatus(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collBlastStatus = models.BlastStatus(
            blastStatusName=bodyJson["blastStatusName"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collBlastStatus.save()
        return responses.Make(
            Status=200,
            Message="Success Create Blast Status",
            Data={
                "blastStatusId": str(collBlastStatus.id),
                "blastStatusName": collBlastStatus.blastStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def BlastStatusDetail():
    try:
        blastStatusId = request.args["blastStatusId"]
        collBlastStatus = models.BlastStatus.objects(
            id=ObjectId(blastStatusId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "blastStatusId": str(collBlastStatus.id),
                "blastStatusName": collBlastStatus.blastStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def BlastStatusUpdate():
    try:
        bodyJson = request.json
        blastStatusId = request.args["blastStatusId"]
        userId = request.args["userId"]
        err = validators.Category(bodyJson)
        collBlastStatus = models.BlastStatus.objects(id=ObjectId(blastStatusId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collBlastStatus:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Blast Status not found"
            ), HTTPStatus.BAD_REQUEST.value
        collBlastStatus.update(blastStatusName=bodyJson["blastStatusName"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Blast Status",
            Data=f"Blast Status with blastStatusId {blastStatusId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def BlastStatusDelete():
    try:
        blastStatusId = request.args["blastStatusId"]
        userId = request.args["userId"]
        collBlastStatus = models.BlastStatus.objects(
            id=ObjectId(blastStatusId),
            isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collBlastStatus:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Blast Status not found"
            ), HTTPStatus.BAD_REQUEST.value
        collBlastStatus.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete Blast Status",
            Data=f"Blast Status with blastStatusId {blastStatusId} was deleted by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value