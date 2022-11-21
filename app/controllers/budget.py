from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def BudgetCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Budget(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collBudget = models.Budgets(
            budgetsAmount=bodyJson["budgetsAmount"], unitId=ObjectId("6374ab4cf861c9476669bad4"), updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collBudget.save()
        return responses.Make(
            Status=200,
            Message="Success Create Blast Status",
            Data={
                "budgetId": str(collBudget.id),
                "budgetsAmount": collBudget.budgetsAmount
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def BudgetUpdate():
    try:
        bodyJson = request.json
        budgetId = request.args["budgetId"]
        userId = request.args["userId"]
        err = validators.Budget(bodyJson)
        collBudget = models.Budgets.objects(id=ObjectId(budgetId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collBudget:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Budget not found"
            ), HTTPStatus.BAD_REQUEST.value
        collBudget.update(blastStatusName=bodyJson["blastStatusName"], updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update Budget",
            Data=f"Budget with budgetId {budgetId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
