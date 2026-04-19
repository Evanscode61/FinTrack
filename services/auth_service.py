from accounts.serializers import RegisterSerializer

class AuthService:

    @staticmethod
    def register(data):
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return user



