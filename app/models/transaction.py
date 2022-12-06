from mongoengine import connect
from mongoengine import *
from datetime import datetime
from app import configs
from .managament import UnitRoles

connect(alias='content', db=configs.mongoDbContent, host=configs.mongoHost, port=configs.mongoPort)
connect(alias='transaction', db=configs.mongoDbTransaction, host=configs.mongoHost, port=configs.mongoPort)

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

class Units(Document):
    unitParent = ReferenceField("self", null=True)
    unitName = StringField(required=True, unique=True)
    unitEmail = StringField(required=True, unique=True)
    unitAddress = StringField(required=True)
    unitPhone = StringField(required=True, unique=True)
    # unitContractAmount = DecimalField(null= True, min_value=0, precision=2)
    # unitContractStart = DateField(null= True)
    # unitContractEnd = DateField(null= True)
    # personResponsibleName = StringField(null=True)
    # personResponsibleContact = StringField(null=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'management'}
    
class Budgets(Document):
    unitId = ReferenceField(Units, required=True)
    budgetsAmount = DecimalField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'transaction'}

class UserUnitRoles(Document):
    userId = ReferenceField(Users, required=True)
    unitRoleId = ReferenceField(UnitRoles, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'management'}

class Mutations(Document):
    fromUserUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    toUserUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    mutationAmount = DecimalField(required=True)
    mutationNote = StringField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'transaction'}

class Wallets(Document):
    walletDC = StringField(required=True)
    walletAmount = DecimalField(required=True)
    userUnitRoleId = ReferenceField(UserUnitRoles)
    mutationId = ReferenceField(Mutations, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'transaction'}

class PaymentStatus(Document):
    paymentStatusName = StringField(required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'master'}

class BlastStatus(Document):
    blastStatusName = StringField(required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'master'}

class Platforms(Document):
    platformName = StringField(required=True, unique=True)
    platformCode = StringField(required=True, unique=True)
    platformPrice = DecimalField(required=True, min_value=0, precision=2)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'master'}

class Segments(Document):
    segmentName = StringField(required=True, unique=True)
    segmentAge = DictField(required=True)
    segmentClass = ListField(required=True)
    segmentGender = ListField(required=True)
    segmentInterest = ListField(required=True)
    segmentLocation = ListField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'content'}

class MutationPaymentStatus(Document):
    mutationId = ReferenceField(Mutations, required=True)
    paymentStatusId = ReferenceField(PaymentStatus, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'transaction'}

class Contents(Document):
    platformId = ReferenceField(Platforms, required=True)
    paymentStatusId = ReferenceField(PaymentStatus, required=True)
    blastStatusId = ReferenceField(BlastStatus, required=True)
    contentMessage = DictField(required=True)
    payloadMessage = DictField(required=True)
    duration = IntField(required=True)
    segmentId = ReferenceField(Segments, required=True)
    targetEstimate = IntField(required=True)
    price = DecimalField(required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta  = {'db_alias': 'content'}