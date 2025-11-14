from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ConversationSerialize, MessageSerializer
from .models import Conversation, Message
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerialize
    permission_classes = [permissions.IsAuthenticated]
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)