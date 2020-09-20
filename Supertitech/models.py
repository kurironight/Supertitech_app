from django.db import models
from django.contrib.auth.models import User


class Timeschedule(models.Model):  # 仮の時間割　あとで修正予定
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.message[:10])


class Subject(models.Model):
    title = models.TextField(max_length=50)
    Q = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    youbi = models.IntegerField(default=0)
    code = models.TextField(max_length=30)
    user = models.ManyToManyField(User, blank=True)
    content = models.TextField(max_length=200, default="説明なし")
    teacher = models.TextField(max_length=20, default="不明")
    credit = models.IntegerField(default="1")
    classroom = models.TextField(max_length=20, default="不明")
    grade = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)


class Reputation(models.Model):
    subject = models.ForeignKey(Subject, on_delete='CASCADE')
    content = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete='CASCADE')
    good_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)


class PastExamFile(models.Model):
    pastexamfile = models.FileField('過去問ファイル')
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete='CASCADE', default=1)
    subject = models.ForeignKey(
        Subject, on_delete='CASCADE', default=1)  # pk=1

    def __str__(self):
        return self.pastexamfile.url


class DocumentFile(models.Model):
    documentfile = models.FileField('資料ファイル')
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete='CASCADE', default=1)
    subject = models.ForeignKey(
        Subject, on_delete='CASCADE', default=1)  # pk=1

    def __str__(self):
        return self.documentfile.url


class Res(models.Model):
    owner = models.ForeignKey(User, on_delete='CASCADE', related_name='Res')
    subject = models.ForeignKey(Subject, on_delete='CASCADE')
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    pinuser = models.ManyToManyField(User, blank=True)


class ProfilImage(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(
        upload_to='profilimages/', default='media/profileimages/bigmac_l.png')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ManyToManyField(User, blank=True)


class QRmatrix(models.Model):
    # blank とnullを入れることにより、require=falseとなる
    gakuseki = models.CharField(max_length=20, blank=True, null=True)
    PW = models.CharField(max_length=20, blank=True, null=True)

    A1 = models.CharField(max_length=1, blank=True, null=True)
    A2 = models.CharField(max_length=1, blank=True, null=True)
    A3 = models.CharField(max_length=1, blank=True, null=True)
    A4 = models.CharField(max_length=1, blank=True, null=True)
    A5 = models.CharField(max_length=1, blank=True, null=True)
    A6 = models.CharField(max_length=1, blank=True, null=True)
    A7 = models.CharField(max_length=1, blank=True, null=True)

    B1 = models.CharField(max_length=1, blank=True, null=True)
    B2 = models.CharField(max_length=1, blank=True, null=True)
    B3 = models.CharField(max_length=1, blank=True, null=True)
    B4 = models.CharField(max_length=1, blank=True, null=True)
    B5 = models.CharField(max_length=1, blank=True, null=True)
    B6 = models.CharField(max_length=1, blank=True, null=True)
    B7 = models.CharField(max_length=1, blank=True, null=True)

    C1 = models.CharField(max_length=1, blank=True, null=True)
    C2 = models.CharField(max_length=1, blank=True, null=True)
    C3 = models.CharField(max_length=1, blank=True, null=True)
    C4 = models.CharField(max_length=1, blank=True, null=True)
    C5 = models.CharField(max_length=1, blank=True, null=True)
    C6 = models.CharField(max_length=1, blank=True, null=True)
    C7 = models.CharField(max_length=1, blank=True, null=True)

    D1 = models.CharField(max_length=1, blank=True, null=True)
    D2 = models.CharField(max_length=1, blank=True, null=True)
    D3 = models.CharField(max_length=1, blank=True, null=True)
    D4 = models.CharField(max_length=1, blank=True, null=True)
    D5 = models.CharField(max_length=1, blank=True, null=True)
    D6 = models.CharField(max_length=1, blank=True, null=True)
    D7 = models.CharField(max_length=1, blank=True, null=True)

    E1 = models.CharField(max_length=1, blank=True, null=True)
    E2 = models.CharField(max_length=1, blank=True, null=True)
    E3 = models.CharField(max_length=1, blank=True, null=True)
    E4 = models.CharField(max_length=1, blank=True, null=True)
    E5 = models.CharField(max_length=1, blank=True, null=True)
    E6 = models.CharField(max_length=1, blank=True, null=True)
    E7 = models.CharField(max_length=1, blank=True, null=True)

    F1 = models.CharField(max_length=1, blank=True, null=True)
    F2 = models.CharField(max_length=1, blank=True, null=True)
    F3 = models.CharField(max_length=1, blank=True, null=True)
    F4 = models.CharField(max_length=1, blank=True, null=True)
    F5 = models.CharField(max_length=1, blank=True, null=True)
    F6 = models.CharField(max_length=1, blank=True, null=True)
    F7 = models.CharField(max_length=1, blank=True, null=True)

    G1 = models.CharField(max_length=1, blank=True, null=True)
    G2 = models.CharField(max_length=1, blank=True, null=True)
    G3 = models.CharField(max_length=1, blank=True, null=True)
    G4 = models.CharField(max_length=1, blank=True, null=True)
    G5 = models.CharField(max_length=1, blank=True, null=True)
    G6 = models.CharField(max_length=1, blank=True, null=True)
    G7 = models.CharField(max_length=1, blank=True, null=True)

    H1 = models.CharField(max_length=1, blank=True, null=True)
    H2 = models.CharField(max_length=1, blank=True, null=True)
    H3 = models.CharField(max_length=1, blank=True, null=True)
    H4 = models.CharField(max_length=1, blank=True, null=True)
    H5 = models.CharField(max_length=1, blank=True, null=True)
    H6 = models.CharField(max_length=1, blank=True, null=True)
    H7 = models.CharField(max_length=1, blank=True, null=True)

    I1 = models.CharField(max_length=1, blank=True, null=True)
    I2 = models.CharField(max_length=1, blank=True, null=True)
    I3 = models.CharField(max_length=1, blank=True, null=True)
    I4 = models.CharField(max_length=1, blank=True, null=True)
    I5 = models.CharField(max_length=1, blank=True, null=True)
    I6 = models.CharField(max_length=1, blank=True, null=True)
    I7 = models.CharField(max_length=1, blank=True, null=True)

    J1 = models.CharField(max_length=1, blank=True, null=True)
    J2 = models.CharField(max_length=1, blank=True, null=True)
    J3 = models.CharField(max_length=1, blank=True, null=True)
    J4 = models.CharField(max_length=1, blank=True, null=True)
    J5 = models.CharField(max_length=1, blank=True, null=True)
    J6 = models.CharField(max_length=1, blank=True, null=True)
    J7 = models.CharField(max_length=1, blank=True, null=True)

    owner = models.ForeignKey(
        User, on_delete='CASCADE')

    def __str__(self):
        return str(self.owner)


class testdata(models.Model):
    data1 = models.TextField(max_length=100)
    data2 = models.TextField(max_length=100)
    data3 = models.TextField(max_length=100)
    data4 = models.TextField(max_length=100)
    data5 = models.TextField(max_length=100)
    data6 = models.TextField(max_length=100)


class Star(models.Model):
    owner = models.ForeignKey(User, on_delete='CASCADE')
    repu = models.ForeignKey(Reputation, on_delete='CASCADE')
