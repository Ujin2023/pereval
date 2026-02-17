from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PerevalAddedSerializer, PerevalUPDSerializer
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

    def patch(self, request, pk):
        try:
            instance = PerevalAdded.objects.get(pk=pk)
        except PerevalAdded.DoesNotExist:
            return Response({
                "state":0,
                "message":f"Запись с номером id {pk} не найдена."
            }, status=status.HTTP_400_BAD_REQUEST)

        if instance.status != 'new':
            return Response({
                "state":0,
                'message':f"Нельзя редактировать запись в статусе {instance.status}"
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = PerevalUPDSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'state': 1,
                'message': "Запись успешно обновлена"
            })
        else:
            return Response({
                'state': 0,
                'message': serializer.errors
            })