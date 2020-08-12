from Supertitech.models import Subject
from django.contrib.auth.models import User

# このcodeは、https://www.sejuku.net/blog/26477　からadd subjectを作るための仮置き場
public = User.objects.filter(username='public').first()
for i in range(4):
    Qu = i+1
    for j in range(5):
        yo = j+1
        for s in range(5):
            ti = s+1
            c = Subject(title='add', Q=Qu, time=ti, youbi=yo, code='add')
            c.save()
            c.user.add(public)
            c.save()
