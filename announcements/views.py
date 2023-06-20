from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from .models import Announcement
from .serializers import AnnouncementSerializer



class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Announcement.objects.all().order_by('pk')
    serializer_class = AnnouncementSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    
    @action(methods=['get'], 
            detail=True, 
            permission_classes=[permissions.IsAuthenticated],
            )
    def get_user_announcments(self, request, pk=None):
        user_announcments = Announcement.objects.filter(user_pk=pk)
        
        return AnnouncementSerializer(user_announcments).data