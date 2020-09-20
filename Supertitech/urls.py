from django.urls import path
from . import views
from supertitech_app import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.menu, name='menu'),
    path('signup', views.signup, name='signup'),
    path('login', views.loginView.as_view(), name="login"),
    path('search', views.search, name="search"),
    path('add/<int:subject_id>', views.add, name="add"),
    path('check/<int:check_id>', views.check, name="check"),
    path('search_time/<int:search_Q>/<int:search_youbi>/<int:search_time>',
         views.search_time, name="search_time"),
    path('repu/<int:subject_id>', views.reputation, name="repu"),
    path('good/<int:repu_id>', views.good, name="good"),
    path('delete/<int:delete_id>', views.repudelete, name="delete"),
    path('resdelete/<int:delete_id>', views.resdelete, name="resdelete"),
    #path('res/<int:subject_id>', views.bulletinPost, name="res"),
    path('change_profile_image', views.change_profile_image,
         name='change_profile_image'),
    path('QRmatrix', views.QRmatrixsite, name='QRmatrix'),
    path('toportal(beta)', views.goportalbeta, name='toportal(beta)'),
    path('upload', views.upload, name='upload'),
    #path('examupload/<int:subject_id>', views.examupload, name='examupload'),
    #path('documentupload/<int:subject_id>', views.documentupload, name='documentupload'),
    path('subdelete/<int:subject_id>', views.subdelete, name='subdelete'),
    path('examdelete/<int:exam_id>', views.examdelete, name='examdelete'),
    path('docdelete/<int:document_id>', views.docdelete, name='docdelete'),
    path('pincheck/<int:res_id>', views.pincheck, name='pincheck'),
    #path('csvtest', views.csvtest, name='csvtest'),
    #path('aaa', views.aaa, name='aaa'),
]
