from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def UserList():
    try:
        collUser = models.Users.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collUser:
            dataArray.append({
                "userId": str(d.id),
                "userName": d.userName,
                "userPassword": d.userPassword,
                "userEmail": d.userEmail,
                "userFirstName": d.userFirstName,
                "userLastName": d.userLastName,
                "userPhoneNumber": d.userPhoneNumber
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

def UserCreate():
    try:
        bodyJson = request.json
        err = validators.User(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collUser = models.Users(userName=bodyJson["userName"], userEmail=bodyJson["userEmail"], userPassword=bodyJson["userPassword"], userPin=bodyJson["userPin"], userFirstName=bodyJson["userFirstName"], userLastName=bodyJson["userLastName"], userPhoneNumber=bodyJson["userPhoneNumber"])
        collUser.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "userId": str(collUser.id),
                "userName": collUser.userName,
                "userEmail": collUser.userEmail,
                "userPassword": collUser.userPassword,
                "userPin": collUser.userPin,
                "userFirstName": collUser.userFirstName,
                "userLastName": collUser.userLastName,
                "userPhoneNumber": collUser.userPhoneNumber
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="errorr",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def UserUpdate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.User(bodyJson)
        collUser = models.Users.objects(id=ObjectId(userId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collUser:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="User not found"
            ), HTTPStatus.BAD_REQUEST.value
        collUser.update(userName=bodyJson["userName"], userEmail=bodyJson["userEmail"], userPassword=bodyJson["userPassword"], userPin=bodyJson["userPin"], userFirstName=bodyJson["userFirstName"], userLastName=bodyJson["userLastName"], userPhoneNumber=bodyJson["userPhoneNumber"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update user",
            Data=f"User data was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value