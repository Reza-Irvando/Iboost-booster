from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def ContentList():
    try:
        collContent = models.Contents.objects(
            isActive=True, isDelete=False).all()
        dataArray = []
        for d in collContent:
            dataArray.append({
                "contentId" : str(d.id),
                "platformId": str(d.platformId.id),
                "contentMessage": d.contentMessage,
                "payloadMessage": d.payloadMessage,
                "duration": d.duration,
                "segmentId": str(d.segmentId.id),
                "targetEstimate": d.targetEstimate,
                "price": d.price
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

def ContentCreate():
    try:
        bodyJson = request.json
        userId = request.args["userId"]
        err = validators.Content(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error1",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        collPlatform = models.Platforms.objects(id=ObjectId(bodyJson["platformId"]), isActive=True, isDelete=False)
        if not collPlatform:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error2",
                Data="PlatformId not found"
            ), HTTPStatus.BAD_REQUEST.value
        collSegment = models.Segments.objects(id=ObjectId(bodyJson["segmentId"]), isActive=True, isDelete=False)
        if not collSegment:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error3",
                Data="SegmentId not found"
            ), HTTPStatus.BAD_REQUEST.value
        collContent = models.Contents(
            platformId=ObjectId(bodyJson["platformId"]), contentMessage=bodyJson["contentMessage"], payloadMessage=bodyJson["payloadMessage"], duration=bodyJson["duration"], segmentId=ObjectId(bodyJson["segmentId"]), targetEstimate=bodyJson["targetEstimate"], price=bodyJson["price"], paymentStatusId=ObjectId("6374889361b23022da7f9940"), blastStatusId=ObjectId("6374884961b23022da7f993b"), updatedBy=ObjectId(userId), createdBy=ObjectId(userId))
        collContent.save()
        return responses.Make(
            Status=200,
            Message="Success create Content",
            Data={
                "contentId": str(collContent.id),
                "platformId": str(collContent.platformId.id),
                "contentMessage": collContent.contentMessage,
                "payloadMessage": collContent.payloadMessage,
                "duration": collContent.duration,
                "segmentId": str(collContent.segmentId.id),
                "targetEstimate": collContent.targetEstimate,
                "price": collContent.price
            }
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error4",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def ContentApprove():
    try:
        contentId = request.args["contentId"]
        userId = request.args["userId"]
        collContent = models.Contents.objects(id=ObjectId(contentId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collContent:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Content not found"
            ), HTTPStatus.BAD_REQUEST.value
        collContent.update(blastStatusId=ObjectId("6374884f61b23022da7f993c"), updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Success",
            Data=f"Content with contentId {contentId} is Approved"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def ContentReject():
    try:
        contentId = request.args["contentId"]
        userId = request.args["userId"]
        collContent = models.Contents.objects(id=ObjectId(contentId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collContent:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Content not found"
            ), HTTPStatus.BAD_REQUEST.value
        collContent.update(blastStatusId=ObjectId("6374885461b23022da7f993d"), updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Success",
            Data=f"Content with contentId {contentId} is Rejected"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def ContentRevision():
    try:
        contentId = request.args["contentId"]
        userId = request.args["userId"]
        collContent = models.Contents.objects(id=ObjectId(contentId), isActive=True, isDelete=False, updatedBy=ObjectId(userId))
        if not collContent:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="Content not found"
            ), HTTPStatus.BAD_REQUEST.value
        collContent.update(blastStatusId=ObjectId("6374885d61b23022da7f993e"), updatedBy=ObjectId(userId))
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Success",
            Data=f"Content with contentId {contentId} is Revised"
        ),200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value