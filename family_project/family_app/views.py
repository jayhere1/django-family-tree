from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer


class PersonListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all
        """
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Person
        """
        data = {
            "ID": request.data.get("ID"),
            "forename": request.data.get("forename"),
            "surname": request.data.get("surname"),
            "parent_id": request.data.get("parent_id"),
        }
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, person_id):
        """
        Helper method to get the object with given id
        """
        try:
            return Person.objects.get(ID=person_id)
        except Person.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, person_id, *args, **kwargs):
        """
        Retrieves the person with id
        """
        person_instance = self.get_object(person_id)
        if not person_instance:
            return Response({"res": f"Person with id {person_id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(person_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def patch(self, request, person_id, *args, **kwargs):
        """
        Updates the Person with given person if exists
        """
        person_instance = self.get_object(person_id)
        if not person_instance:
            return Response({"res": f"Person with id {person_id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "ID": request.data.get("ID"),
            "forename": request.data.get("forename"),
            "surname": request.data.get("surname"),
            "parent_id": request.data.get("parent_id"),
        }
        serializer = PersonSerializer(instance=person_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonChildrenApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, person_id, *args, **kwargs):
        """
        Retrieves the person with id
        """
        family_list = Person.objects.filter(parent_id__contains=[person_id])
        # return (person_instance)
        if not family_list:
            return Response({"res": f"No children found for {person_id}"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(family_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonSiblingsAPIView(APIView):
    def get_object(self, person_id):
        """
        Helper method to get the object with given id
        """
        try:
            return Person.objects.get(ID=person_id)
        except Person.DoesNotExist:
            return None

    def get(self, request, person_id, *args, **kwargs):
        """
        Retrieves the person with id
        """
        current_person = self.get_object(person_id)
        siblings_list = []
        for parent in current_person.parent_id:
            siblings_list = Person.objects.filter(parent_id__contains=[parent])
        if not siblings_list:
            return Response({"res": f"No siblings found for {person_id}"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(siblings_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonAncestorsAPIView(APIView):
    def get_object(self, person_id):
        """
        Helper method to get the object with given id
        """
        try:
            return Person.objects.get(ID=person_id)
        except Person.DoesNotExist:
            return None

    def get(self, request, person_id, *args, **kwargs):
        """
        Retrieves the person with id
        """
        current_person = self.get_object(person_id)
        parent_ids = current_person.parent_id
        ancestors_list = []
        ancestors_list = Person.objects.filter(ID__in=parent_ids)
        if not ancestors_list:
            return Response({"res": f"No ancestors found for {person_id}"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(ancestors_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonDescendantsAPIView(APIView):
    def get(self, request, person_id, *args, **kwargs):
        """
        Retrieves the person with id
        """
        family_list = Person.objects.filter(parent_id__contains=[person_id])
        # return (person_instance)
        if not family_list:
            return Response({"res": f"No descendants found for {person_id}"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(family_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
