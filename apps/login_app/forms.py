from models import User, Club

class ClubList (forms.ModelForm):

    model = User
    fields = ('club')
