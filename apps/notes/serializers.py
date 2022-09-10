from rest_framework import serializers
from apps.notes.models import Note

class NoteSerializer(serializers.ModelSerializer):

   class Meta:
      model = Note
      read_only_fiels = (
         "id",
         "created_at",
         "created_by",
      )
      fields = (
         "id",
         "created_at",
         "created_by",
         "content"
      )
