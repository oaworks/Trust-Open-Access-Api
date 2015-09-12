from publishers.models import Publisher
from publishers.serializers import PublisherSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PublishersList(generics.ListCreateAPIView):
	queryset = Publisher.objects.all()
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	serializer_class = PublisherSerializer

class PublisherDetail(generics.ListCreateAPIView):
	serializer_class = PublisherSerializer
	def get_object(self, pk):
		try:
			return Publisher.objects.filter(pk__istartswith=pk)
		except Publisher.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		publisher = self.get_object(pk)
		serializer = PublisherSerializer(publisher, many=True)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		publisher = self.get_object(pk)
		serializer = PublisherSerializer(publisher, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		publisher = self.get_object(pk)
		publisher.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)