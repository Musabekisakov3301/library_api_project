from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title','subtitle','content','author','isbn','price',)
    
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError( 
                {
                    'status': False,
                    'message': 'The title of the book must be composed of a letter'
                }
            )
        
        # check title and author from database existance
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                  {
                    'status': False,
                    'message': "Kitabdin atin ham author rin birdey bolgan bolsa jukley almaysiz"
                }
            )
        
        return data
    
    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError(
                {
                   'status': False,
                   'message': "Bahasi qate terilgen"
                }
            )