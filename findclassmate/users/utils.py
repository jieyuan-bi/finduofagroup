import logging
from django.db.models import Q
from .models import *
from passlib.context import CryptContext

# Get an instance of a logger
logger = logging.getLogger(__name__)

#encrypt the password
def encryptPassword(password):
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )
    return pwd_context.encrypt(password)

#check if the password match the hashed one
#@return 
def checkPassword(account, password):
    role = UserModel.objects.get(name=account).role
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
    )
    hashed = UserModel.objects.get(name=account).password
    # logger.info('[Users] check_password' +hashed )
    validity = pwd_context.verify(password, hashed)
    return validity, role

#create super super user
def createAdmin():
    name='jieyuan'
    password='bijieyuan526'
    password = encryptPassword(password)
    UserModel.objects.create(name=name,password=password,role=2)
    return

#search user with query
#@return serialized users
def searchUser(query):
    users = UserModel.objects.filter(Q(name__icontains=query))
    result = []
    for user in users:
        data = {'name':user.name,'gender':user.gender,'phone':user.phone,'wechat':user.wechat,'email':user.email,'onecard':user.get_onecard(),
            'role':user.role,'create_time':user.create_time, 'major':user.major}
        result.append(data)
    return result
