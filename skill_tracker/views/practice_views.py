from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.practice import Practice
from ..serializers import PracticeSerializer

# Create your views here.


class PracticesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PracticeSerializer

    def get(self, request):
        """Index request"""
        # Get all the practices:
        practices = Practice.objects.all()
        # Filter the practices by owner, so you can only see your owned practices
        # practices = Practice.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = PracticeSerializer(practices, many=True).data
        return Response({'practices': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['practice']['owner'] = request.user.id
        # Serialize/create practice
        practice = PracticeSerializer(data=request.data['practice'])
        # If the practice data is valid according to our serializer...
        if practice.is_valid():
            # Save the created practice & send a response
            practice.save()
            return Response({'practice': practice.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(practice.errors, status=status.HTTP_400_BAD_REQUEST)


class MyPracticesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PracticeSerializer

    def get(self, request):
        """Index request"""
        # Filter the practices by owner, so you can only see your owned practices
        practices = Practice.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = PracticeSerializer(practices, many=True).data
        return Response({'practices': data})

class PracticeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the practice to show
        practice = get_object_or_404(Practice, pk=pk)
        # Only want to show owned practices?
        if request.user != practice.owner:
            raise PermissionDenied('Unauthorized, you do not own this practice')

        # Run the data through the serializer so it's formatted
        data = PracticeSerializer(practice).data
        return Response({'practice': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate practice to delete
        practice = get_object_or_404(Practice, pk=pk)
        # Check the practice's owner against the user making this request
        if request.user != practice.owner:
            raise PermissionDenied('Unauthorized, you do not own this practice')
        # Only delete if the user owns the  practice
        practice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Practice
        # get_object_or_404 returns a object representation of our Practice
        practice = get_object_or_404(Practice, pk=pk)
        # Check the practice's owner against the user making this request
        if request.user != practice.owner:
            raise PermissionDenied('Unauthorized, you do not own this practice')

        # Ensure the owner field is set to the current user's ID
        request.data['practice']['owner'] = request.user.id
        # Validate updates with serializer
        data = PracticeSerializer(practice, data=request.data['practice'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
