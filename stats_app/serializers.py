from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Country, Competition, Season, Group, Battle, Freestyler

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        
        fields = ('id', 'username', 'password', 'email',)

        # These fields are displayed but not editable and have to be a part of 'fields' tuple
        read_only_fields = ('is_active', 'is_staff', 'is_superuser',)

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {'password': {'write_only': True}}

class TokenSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Token
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Country
        fields = "__all__"

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Competition
        fields = "__all__"

class SeasonSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Season
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Group
        fields = "__all__"

class FreestylerSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Freestyler
        fields = "__all__"

class BattleSerializer(serializers.ModelSerializer):

    # judge = UserSerializer(read_only=True)
    # freestyler_1 = FreestylerSerializer(read_only=True)
    # freestyler_2 = FreestylerSerializer(read_only=True)
    # winner_replica = FreestylerSerializer(read_only=True)
    # competition =  CompetitionSerializer(read_only=True)
    # season = SeasonSerializer(read_only=True)
    # group = GroupSerializer(read_only=True)
    

    def to_representation(self, instance):

        self.fields['judge'] = UserSerializer(read_only=True)
        self.fields["freestyler_1"] = FreestylerSerializer(read_only=True)
        self.fields["freestyler_2"] = FreestylerSerializer(read_only=True)
        self.fields["winner_replica"] = FreestylerSerializer(read_only=True)
        self.fields["competition"] =  CompetitionSerializer(read_only=True)
        self.fields["season"] = SeasonSerializer(read_only=True)
        self.fields["group"] = GroupSerializer(read_only=True)

        return super().to_representation(instance)
    

    class Meta(object):
        model = Battle
        fields = "__all__"