from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from applications.likedislike.models import LikeDislike
from applications.account.models import Profile
from applications.likedislike.serializers import LikeSerializer, DislikeSerializer



class LikeCreateAPIView(APIView):
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        sender = serializer.validated_data['sender']
        recipient = serializer.validated_data['recipient']
        existing_like = LikeDislike.objects.filter(sender=sender, recipient=recipient, is_like=True).exists()
        if existing_like:
            message = 'You have already sent a like to this recipient'
            response = {
                'message': message
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        data = serializer.data
        message = 'Like created successfully!'
        response = {
            'data': data,
            'message': message
        }
        return Response(response, status=status.HTTP_201_CREATED)

class SetDislikeAPIView(APIView):
    serializers_class = DislikeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializers_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        sender = serializer.validated_data['sender']
        recipient = serializer.validated_data['recipient']
        existing_like = LikeDislike.objects.filter(sender=sender, recipient=recipient, is_like=True).exists()
        if existing_like:
            message = 'you have already disliked this person'
            response = {
                'message': message
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        data = serializer.data
        message = 'dislike created successfully'
        response = {
            'data': data,
            'message': message
        }
        return Response(response, status=status.HTTP_201_CREATED)


            

    
        
            
            


     

            
                    
        
        