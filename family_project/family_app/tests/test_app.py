from django.test import TestCase, Client
from family_app.models import Person
from family_app.serializers import PersonSerializer
from rest_framework.decorators import api_view
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status


client = Client()


class GetAllPuppiesTest(TestCase):
    """Test module for GET all puppies API"""

    def setUp(self):

        Person.objects.create(ID=1, forename="John", surname="Smith", parent_id=[2])

    @api_view(["GET", "POST"])
    def get_persons(request):
        # get all puppies
        if request.method == "GET":
            person1 = Person.objects.all()
            serializer = PersonSerializer(person1, many=True)
            return Response(serializer.data)
        # insert a new record for a Person
        elif request.method == "POST":
            return Response({})

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse("get_persons"))
        # get data from db
        person1 = Person.objects.all()
        serializer = PersonSerializer(person1, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
