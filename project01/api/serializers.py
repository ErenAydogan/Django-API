from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        #fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(read_only=True, many=True)
    #Adding another field
    #len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        #fields = ['active', 'name', 'description']
        #exclude = ['id']



class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(read_only=True, many=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="watch-detail")


    class Meta:
        model = StreamPlatform
        fields = "__all__"



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error' : 'Passwords don\'t match!'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error' : 'This email has already been used!'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account


"""
    def get_len_name(self, object): #get_{field_name}
        return len(object.title)

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short!")

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different!")
        else:
            return data


    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
"""