from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators


def PaymentStatusList():
    try:
        collPaymentStatus = models.PaymentStatus.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collPaymentStatus:
            dataArray.append({
                "paymentStatusId": str(d.id),
                "paymentStatusName": d.paymentStatusName,
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

def PaymentStatusCreate():
    try:
        bodyJson = request.json
        userId = ObjectId(request.args["userId"])
        err = validators.PaymentStatus(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collPaymentStatus = models.PaymentStatus(
            paymentStatusName=bodyJson["paymentStatusName"], updatedBy=userId, createdBy=userId)
        collPaymentStatus.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "paymentStatusId": str(collPaymentStatus.id),
                "paymentStatusName": collPaymentStatus.paymentStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def PaymentStatusDetail():
    try:
        paymentStatusId = ObjectId(request.args["paymentStatusId"])
        collPaymentStatus = models.PaymentStatus.objects(
            id=paymentStatusId,
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "paymentStatusId": str(collPaymentStatus.id),
                "paymentStatusName": collPaymentStatus.paymentStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def PaymentStatusUpdate():
    try:
        bodyJson = request.json
        paymentStatusId = ObjectId(request.args["paymentStatusId"])
        userId = ObjectId(request.args["userId"])
        err = validators.Category(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collPaymentStatus = models.BlastStatus.objects(id=paymentStatusId, isActive=True, isDelete=False).update(
            paymentStatusName=bodyJson["paymentStatusName"], updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "paymentStatusId": str(collPaymentStatus.id),
                "paymentStatusName": collPaymentStatus.paymentStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def PaymentStatusDelete():
    try:
        paymentStatusId = ObjectId(request.args["paymentStatusId"])
        userId = ObjectId(request.args["userId"])
        collPaymentStatus = models.PaymentStatus.objects(
            id=paymentStatusId,
            isActive=True, isDelete=False).update(isActive=False, isDelete=True, updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "paymentStatusId": str(collPaymentStatus.id),
                "paymentStatusName": collPaymentStatus.paymentStatusName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
