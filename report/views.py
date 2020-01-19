from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .models import Entry
from .forms import EntryAddForm
from .serializers import EntrySerializer


class EntryView(APIView):

    def get(self, request, entry_id=None):

        if entry_id:
            entries = Entry.objects.filter(user=request.user, id=entry_id)
        else:
            entries = Entry.objects.filter(user=request.user)

        serializer = EntrySerializer(entries, many=True)
        return Response({'entries': serializer.data})

    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, entry_id):
        entry = Entry.objects.filter(user=request.user, id=entry_id)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)