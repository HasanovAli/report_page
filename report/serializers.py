from rest_framework import serializers
from report.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'user', 'date', 'distance', 'duration']



