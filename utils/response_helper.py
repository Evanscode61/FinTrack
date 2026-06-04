from rest_framework import status
from rest_framework.response import Response


class APIResponse:

    @staticmethod
    def success(message, data=None, http_status=status.HTTP_200_OK):
        return Response({
            'status' : 'success',
            'message': message,
            'data'   : data or {},
        }, status=http_status)

    @staticmethod
    def created(message, data=None):
        return Response({
            'status' : 'success',
            'message': message,
            'data'   : data or {},
        }, status=status.HTTP_201_CREATED)

    @staticmethod
    def deleted(message):
        return Response({
            'status' : 'success',
            'message': message,
            'data'   : {},
        }, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def bad_request(message, errors=None):
        return Response({
            'status' : 'error',
            'message': message,
            'errors' : errors or {},
        }, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def unauthorized(message='Authentication required'):
        return Response({
            'status' : 'error',
            'message': message,
            'errors' : {},
        }, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def forbidden(message='You do not have permission to perform this action'):
        return Response({
            'status' : 'error',
            'message': message,
            'errors' : {},
        }, status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def not_found(message='Resource not found'):
        return Response({
            'status' : 'error',
            'message': message,
            'errors' : {},
        }, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def conflict(message, errors=None):
        return Response({
            'status' : 'error',
            'message': message,
            'errors' : errors or {},
        }, status=status.HTTP_409_CONFLICT)

    @staticmethod
    def unprocessable(message, errors=None):
        return Response({
            'status' : 'error',
            'message': message,
            'errors' : errors or {},
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @staticmethod
    def server_error(message='An unexpected error occurred. Please try again later'):
        return Response({
            'status' : 'error',
            'message': message,
            'errors' : {},
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)