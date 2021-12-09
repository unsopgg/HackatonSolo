from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Chapter
from .permissions import IsChapterUploader
from .serializers import ChapterSerializer

class ChapterView(generics.RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class ChapterCreateView(generics.CreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated, ]

class ChapterUpdateView(generics.UpdateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated, IsChapterUploader, ]

class ChapterDeleteView(generics.DestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated, IsChapterUploader, ]
