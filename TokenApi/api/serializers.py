from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        
        return token

    def validate(self, attrs):
        
        data = super().validate(attrs)        
        
        data.update({
            'user' : {
                'id' : self.user.id,
                'username' : self.user.username,
                'email' : self.user.email
            }
        })
        
        return data
