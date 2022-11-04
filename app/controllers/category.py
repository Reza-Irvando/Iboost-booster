from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators


def CategoryList():
    try:
        collCategory = models.Categories.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collCategory:
            dataArray.append({
                "categoryId": str(d.id),
                "categoryName": d.categoryName,
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

def CategoryCreate():
    try:
        bodyJson = request.json
        userId = ObjectId(request.args["userId"])
        err = validators.Category(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collCategory = models.Categories(
            categoryName=bodyJson["categoryName"], updatedBy=userId, createdBy=userId)
        collCategory.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collCategory.id),
                "categoryName": collCategory.categoryName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def CategoryDetail():
    try:
        categoryId = ObjectId(request.args["categoryId"])
        collCategory = models.Categories.objects(
            id=categoryId,
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collCategory.id),
                "categoryName": collCategory.categoryName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def CategoryUpdate():
    try:
        bodyJson = request.json
        categoryId = ObjectId(request.args["categoryId"])
        userId = ObjectId(request.args["userId"])
        err = validators.Category(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collCategory = models.Categories.objects(id=categoryId, isActive=True, isDelete=False).update(
            categoryName=bodyJson["categoryName"], updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collCategory.id),
                "categoryName": collCategory.categoryName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value


def CategoryDelete():
    try:
        categoryId = ObjectId(request.args["categoryId"])
        userId = ObjectId(request.args["userId"])
        collCategory = models.Categories.objects(
            id=categoryId,
            isActive=True, isDelete=False).update(isActive=False, isDelete=True, updatedBy=userId)
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "categoryId": str(collCategory.id),
                "categoryName": collCategory.categoryName
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
