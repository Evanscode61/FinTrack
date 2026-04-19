from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from services.auth_service import AuthService
from utils.response_helper import APIResponse


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = AuthService.register(request.data)
        return APIResponse.created(
            message='Account created successfully',
            data={
                'user_uuid'   : user.uuid,
                'email'     : user.email,
                'first_name': user.first_name,
                'last_name' : user.last_name,
                'phone_number' : user.phone_number,
                'created_at': user.created_at.strftime('%Y-%m-%dT%H:%M:%SZ'),
            }
        )
