from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializers
from actors.serializers import ActorSerializers


class MovieModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

        """if reviews:
            sum_reviews = 0
            for review in reviews:
                sum_reviews += review.starts

            reviews_count = reviews.count()

            return round(sum_reviews / reviews_count,1)
        return None"""
        # quiser escrever validação para cada campo especifico tem como
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo não pode passar de 200 caractere')
        return value


class MovieListDetailSerializers(serializers.ModelSerializer):

    actors = ActorSerializers(many=True)
    genre = GenreSerializers()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):

        # reviews = obj.reviews.all()

        rate = obj.reviews.aggregate(Avg('starts'))['starts__avg']

        if rate:

            return round(rate, 1)

        return None
