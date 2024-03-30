from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )
    resumo = serializers.CharField()

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


    #esse metodo precisa ter get_ como prefixo para poder implementar o campo de serliazerMethodField, pois esse é um campo calculado
    def get_rate(self, obj):        
        reviews = obj.reviews.filter()
        if reviews:
            i = 0
            media = 0
            for rate in reviews:
                media += rate.stars
                i = i+1
            return media / i
        return None
    

    #Validação de campos sempre começam com validate_[nome do campo]
    #pode ter mais de uma validação por campo, pois retorna uma lista de validações
    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1950.')
        return value
    

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior do que 500 caracteres.')
        return value