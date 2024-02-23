
from rest_framework import serializers
            
from .models import User





class UserSerializers(serializers.ModelSerializer):
            Confirm_Password = serializers.CharField(write_only=True)
            class Meta:
                    model = User
                                # fields = '__all__'
                    fields = ['id','Username','Profile_Photo','First_Name','Last_Name','Email','Mobile_Number','Role','DOB','Address','Password','Confirm_Password']
                    extra_kwargs = {
                        'Password': {'write_only': True},  # Making Password field write-only
                        'Confirm_Password': {'write_only': True},  
                    }
            def create(self, validated_data):
                    validated_data.pop('Confirm_Password', None)  # Remove Confirm_Password from validated_data
                    return super().create(validated_data)



