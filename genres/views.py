from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from app.permisions import GlobalDefaultPermission
from genres.serializers import GenreSerializers


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    # esse método faz básicamente a mesma coisa abaixo lista tudo que tem no BD e
    # cadastra nova coisa no BD


"""@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201,) """


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    # faz a mesma coisa do código abaixo, detalha, atualiza e exclui


"""@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
      data = {'id': genre.id, 'name': genre.name}
      return JsonResponse(data)
    elif request.method == 'PUT':
         data = json.loads(request.body.decode('utf-8'))
         genre.name = data['name']
         genre.save()
         return JsonResponse({'id': genre.id, 'name': genre.name})
    elif request.method == 'DELETE':
         genre.delete()
         return JsonResponse({'message':'Genero excluido com sucesso!!!'}, status=204)"""
