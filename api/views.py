from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PerevalAddedSerializer
from .models import PerevalAdded

class SubmitDataView(APIView):
    def post(self, request):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            try:
                obj = serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Отправлено успешно',
                    'id': obj.id
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    'status': 500,
                    'message': str(e),
                    'id': None
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({
                'status': 400,
                'message': 'Ошибка валидации',
                'errors': serializer.errors,
                'id': None
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            pereval = PerevalAdded.objects.get(pk=pk)
            serializer = PerevalAddedSerializer(pereval)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PerevalAdded.DoesNotExist:
            return Response({'message':f'Запись {pk} не найдена',
                             "status": 404},
                            status=status.HTTP_404_NOT_FOUND)
