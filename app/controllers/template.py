from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def TemplateList():
    try:
        collTemplate = models.Templates.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collTemplate:
            dataArray.append({
                "templateId": str(d.id),
                "templateName": d.templateName,
                "templateContent": d.templateContent,
                "templateLength": d.templateLength,
                "categoryId": str(d.categoryId.id)
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

def TemplateCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Template(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message= "error1",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collTemplate = models.Templates(
            templateName=bodyJson["templateName"], 
            templateContent=bodyJson["templateContent"], 
            templateLength=bodyJson["templateLength"], 
            categoryId=ObjectId(bodyJson["categoryId"]), 
            updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collTemplate.save()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "templateId": str(collTemplate.id),
                "templateName": collTemplate.templateName,
                "templateContent": collTemplate.templateContent,
                "templateLength": collTemplate.templateLength,
                "categoryId": str(collTemplate.categoryId.id)
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="errorr2",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def TemplateDetail():
    try:
        templateId = request.args["templateId"]
        collTemplate = models.Templates.objects(
            id=ObjectId(templateId),
            isActive=True, isDelete=False).first()
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "templateId": str(collTemplate.id),
                "templateName": collTemplate.templateName,
                "templateContent": collTemplate.templateContent,
                "templateLength": collTemplate.templateLength,
                "categoryId": str(collTemplate.categoryId)
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def TemplateUpdate():
    try:
        bodyJson = request.json
        templateId = request.args["templateId"]
        userId = request.args["userId"]
        err = validators.Template(bodyJson)
        collTemplate = models.Templates.objects(id=ObjectId(templateId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collTemplate:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Template not found"
            ), HTTPStatus.BAD_REQUEST.value
        collTemplate.update(templateName=bodyJson["templateName"], templateContent=bodyJson["templateContent"], templateLength=bodyJson["templateLength"], categoryId=ObjectId(bodyJson["categoryId"]), updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly update template",
            Data=f"Template with templateId {templateId} was updated by {userId}"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def TemplateDelete():
    try:
        templateId = request.args["templateId"]
        userId = request.args["userId"]
        collTemplate = models.Templates.objects(
            id=ObjectId(templateId),
            isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collTemplate:
            return responses.Make(
                Status=HTTPStatus.OK.value,
                Message="error",
                Data="Template not found"
            ), HTTPStatus.BAD_REQUEST.value
        collTemplate.delete()
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Successfuly delete template",
            Data=f"Template with templateId {templateId} was deleted by {userId}"
        ), HTTPStatus.OK.value
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value