from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from services.auth_service import AuthService
from accounts.serializers import UserReadSerializer
from utils.response_helper import APIResponse


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            user, refresh = AuthService.register(request.data)
        except APIException:
            import traceback
            traceback.print_exc()
            raise
        except Exception:
            raise APIException('Registration failed. Please try again.')

        return APIResponse.created(
            message='Account created successfully',
            data={
                **UserReadSerializer(user).data,
                'tokens': {
                    'access' : str(refresh.access_token),
                    'refresh': str(refresh),
                }
            }
        )