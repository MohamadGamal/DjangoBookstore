# from django.conf import settings
# from django.contrib.auth.hashers import check_password
# from .models import User


# class MyBackend(object):
#     def authenticate(self, request, username=None, password=None):
#         # login_valid = (settings.ADMIN_LOGIN == username)
#         # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
#         # if login_valid and pwd_valid:
#         try:
#                 print(username)
#                 user = User.objects.get(username=username)
              
#         except Exception:
#                 return None
#         return user

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
