from django.contrib import admin
from .models import Star, Timeschedule, Subject, Reputation, Res, ProfilImage, PastExamFile, DocumentFile, QRmatrix, testdata

# Register your models here.
admin.site.register(Timeschedule)
admin.site.register(Subject)
admin.site.register(Reputation)
admin.site.register(DocumentFile)
admin.site.register(PastExamFile)
admin.site.register(Res)
admin.site.register(ProfilImage)
admin.site.register(QRmatrix)
admin.site.register(testdata)
admin.site.register(Star)
