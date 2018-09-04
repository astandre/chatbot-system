from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email')


class SocialNetworkInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworks
        fields = ('id_account', 'social_network')


class SocialNetworksSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SocialNetworks
        fields = ('id_account', 'user_name', 'social_network', 'user')

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        try:
            user = Users.objects.get(email=users_data["email"])
        except Users.DoesNotExist:
            print("(User) isn't in the database yet.")
            print("Adding (User)", users_data['first_name'], " ", users_data['last_name'], "  to DB")
            user = Users(first_name=users_data['first_name'], last_name=users_data['last_name'],
                         email=users_data['email'])
            user.save()
        else:
            print(user, " (User) is in the database.")
        finally:
            user = Users.objects.get(email=users_data["email"])
        SocialNetworks.objects.create(user=user, **validated_data)
        return user


class InputSerializer(serializers.ModelSerializer):
    social_network = SocialNetworkInputSerializer()

    class Meta:
        model = Inputs
        fields = ('created_at', 'text', 'location', 'raw_input', 'social_network')

    def create(self, validated_data):
        user_data = validated_data['social_network']
        sn_user = SocialNetworks.objects.get(id_account=user_data['id_account'],
                                             social_network=user_data['social_network'])
        input_name = Inputs(text=validated_data['text'], location=validated_data['location'],
                            created_at=validated_data['created_at'],
                            raw_input=validated_data['raw_input'], social_network=sn_user)
        input_name.save()

        return input_name
