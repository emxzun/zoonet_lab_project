from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from applications.likedislike.models import LikeDislike
from applications.account.models import Profile
from applications.likedislike.serializers import LikeDislikeSerializer



class LikeCreateAPIView(APIView):
    serializer_class = LikeDislikeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        message = 'Like created successfully!'
        response = {
            'data': data,
            'message': message
        }
        return Response(response, status=status.HTTP_201_CREATED)

class SetDislikeAPIView(APIView):
    def post(self, request, user_id):
        serializer = LikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dislike = serializer.save(sender=request.user, recipient_id=user_id, is_dislike=True)
        subject = f'You have a new Dislike from {request.user.username}'
        message = f'You have a new Dislike from {request.user.username}!'
        recipient_list = [dislike.recipient.email]
        email = EmailMessage(subject, message, to=recipient_list)
        email.send()
        return Response({'status': 'success', 'message': 'You disliked this user'}, status=status.HTTP_201_CREATED)

            
class GetLikeDislikeAPIView(APIView): 
    '''Получение статуса Like/Dislike на профиле ID - recipient_id
        Формат ответа:
            "is_like": BooleanField,
            "is_dislike": BooleanField
                        
    '''

    @staticmethod
    def get(request, recipient_id):

        try:
            recipient = Profile.objects.get(user_id=recipient_id)
            sender = Profile.objects.get(user_id=request.user.id)
            like_dislake = LikeDislike.objects.filter(sender=sender, 
                                            recipient=recipient).values('is_like', 'is_dislike')
            return Response(like_dislake, status=status.HTTP_200_OK)
        except BaseException:
            return Response({'message': 'По данному запросу нет данных'},status=status.HTTP_204_NO_CONTENT)
    
        
            
            


     

            
                    
        
        