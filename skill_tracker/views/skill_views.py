from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.skill import Skill
from ..serializers import SkillSerializer

# Create your views here.


class SkillsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SkillSerializer

    def get(self, request):
        """Index request"""
        # Get all the skills:
        # skills = Skill.objects.all()
        # Filter the skills by owner, so you can only see your owned skills
        skills = Skill.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = SkillSerializer(skills, many=True).data
        return Response({'skills': data})

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['skill']['owner'] = request.user.id
        # Serialize/create skill
        skill = SkillSerializer(data=request.data['skill'])
        # If the skill data is valid according to our serializer...
        if skill.is_valid():
            # Save the created skill & send a response
            skill.save()
            return Response({'skill': skill.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(skill.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the skill to show
        skill = get_object_or_404(Skill, pk=pk)
        # Only want to show owned skills?
        if request.user != skill.owner:
            raise PermissionDenied('Unauthorized, you do not own this skill')

        # Run the data through the serializer so it's formatted
        data = SkillSerializer(skill).data
        return Response({'skill': data})

    def delete(self, request, pk):
        """Delete request"""
        # Locate skill to delete
        skill = get_object_or_404(Skill, pk=pk)
        # Check the skill's owner against the user making this request
        if request.user != skill.owner:
            raise PermissionDenied('Unauthorized, you do not own this skill')
        # Only delete if the user owns the  skill
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Skill
        # get_object_or_404 returns a object representation of our Skill
        skill = get_object_or_404(Skill, pk=pk)
        # Check the skill's owner against the user making this request
        if request.user != skill.owner:
            raise PermissionDenied('Unauthorized, you do not own this skill')

        # Ensure the owner field is set to the current user's ID
        request.data['skill']['owner'] = request.user.id
        # Validate updates with serializer
        data = SkillSerializer(skill, data=request.data['skill'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
