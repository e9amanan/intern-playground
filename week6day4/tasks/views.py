from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework.decorators import action


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class=TaskSerializer

    permission_classes = [IsAuthenticated,IsOwner]

    

    def get_queryset(self):
        user=self.request.user
        return Task.objects.filter(owner=user)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


    @action(detail=True,methods=['post'])
    def mark_complete(self,request,pk=None):
        task=self.get_object()
        task.completed=True
        task.save()
        return Response({'status':'task marked as complete'})
