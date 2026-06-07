

from accounts.serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError


class AuthService:

    @staticmethod
    def register(data):
        import traceback
        try:
            serializer = RegisterSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            try:
                user = serializer.save()
            except IntegrityError:
                raise ValidationError({'email': 'An account with this email already exists.'})
            refresh = RefreshToken.for_user(user)
            return user, refresh
        except Exception as e:
            traceback.print_exc()
            raise