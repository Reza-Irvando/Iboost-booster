from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def BankList():
    try:
        collBank = models.Banks.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collBank:
            dataArray.append({
                "bankId": str(d.id),
                "bankName": d.bankName,
                "bankCode": d.bankCode
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

def BankCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Bank(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collBank = models.Banks(
            bankName=bodyJson["bankName"], bankCode=bodyJson["bankCode"], updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collBank.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "bankId": str(collBank.id),
                "bankName": collBank.bankName,
                "bankCode": collBank.bankCode
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def BankDetail():
    try:
        bankId = request.args["bankId"]
        collBank = models.Banks.objects(
            id=ObjectId(bankId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "bankId": str(collBank.id),
                "bankName": collBank.bankName,
                "bankCode": collBank.bankCode
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def BankUpdate():
    try:
        bodyJson = request.json
        bankId = request.args["bankId"]
        userId = request.args["userId"]
        err = validators.Bank(bodyJson)
        collBank = models.Banks.objects(id=ObjectId(bankId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collBank:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Bank not found"
            ), HTTPStatus.BAD_REQUEST.value
        collBank.update(bankName=bodyJson["bankName"], bankCode=bodyJson["bankCode"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Bank",
            Data=f"Bank with bankId {bankId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def BankDelete():
    try:
        bankId = request.args["bankId"]
        userId = request.args["userId"]
        collBank = models.Banks.objects(
            id=ObjectId(bankId),
            isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collBank:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data="Bank not found"
            ), HTTPStatus.BAD_REQUEST.value
        collBank.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete Bank",
            Data=f"Bank with bankId {bankId} was deleted by {userId}"
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value