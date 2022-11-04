from mongoengine import connect
from mongoengine import *
from datetime import datetime
from app import configs

connect(alias='content', db=configs.mongoDbContent, host=configs.mongoHost, port=configs.mongoPort)
connect(alias='management', db=configs.mongoDbManagement, host=configs.mongoHost, port=configs.mongoPort)

class Users(Document):
    userName = StringField(max_length=25, required=True, unique=True)
    userEmail = EmailField(required=True, unique=True)
    userPassword = StringField(required=True)
    userPin = StringField(required=True)
    userFirstName = StringField(max_length=25)
    userLastName = StringField(max_length=25)
    userPhoneNumber = StringField(max_length=15, required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField("self", null=True)
    createdBy = ReferenceField("self", null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'management'}
    
class Segments(Document):
    segmentName = StringField(required=True, unique=True)
    segmentAge = StringField(required=True, unique=True)
    segmentClass = StringField(required=True, unique=True)
    segmentGender = StringField(required=True, unique=True)
    segmentInterest = StringField(required=True, unique=True)
    segmentLocation = StringField(required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'content'}