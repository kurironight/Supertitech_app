from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import forms as auth_forms
from .models import ProfilImage, QRmatrix, DocumentFile, PastExamFile
# ユーザ作成フォームを継承


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'class_name'}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'class_name'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password Again', 'class': 'class_name'}))


class PostForm(forms.Form):
    content = forms.CharField(max_length=400,
                              widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)


class ResPostForm(forms.Form):
    content = forms.CharField(max_length=400,
                              widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super(ResPostForm, self).__init__(*args, **kwargs)


class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


class QuarterSelectionForm(forms.Form):  # クオーターを利用して授業を検索するフォーム
    quarters = forms.MultipleChoiceField(
        label='Quarter',
        widget=forms.CheckboxSelectMultiple,
        choices=(
                ('1', '1Q'),
                ('2', '2Q'),
                ('3', '3Q'),
                ('4', '4Q'),
        ),
        required=False
    )
    grades = forms.MultipleChoiceField(
        label='grade',
        widget=forms.CheckboxSelectMultiple,
        choices=(
                ('1', '100'),
                ('2', '200'),
                ('3', '300'),
                ('4', '400'),
        ),
        required=False
    )
    time = forms.MultipleChoiceField(
        label='time',
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ('1', '1限'),
            ('2', '2限'),
            ('3', '3限'),
            ('4', '4限'),
            ('5', '5限'),
            ('6', '6限'),
        ),
        required=False
    )

    day = forms.MultipleChoiceField(
        label='day',
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ('1', '月曜日'),
            ('2', '火曜日'),
            ('3', '水曜日'),
            ('4', '木曜日'),
            ('5', '金曜日'),
            ('6', '土曜日'),
        ),
        required=False
    )
    name = forms.CharField(
        label='授業名',
        max_length=100,
        required=False
    )


class QuarterSelectformenu(forms.Form):  # menu用Qselectform
    data = [
        ('1', '1Q'),
        ('2', '2Q'),
        ('3', '3Q'),
        ('4', '4Q'),
    ]
    choice = forms.ChoiceField(label='Q',
                               choices=data,
                               initial=['1'])


class ProfilImageForm(forms.ModelForm):
    class Meta:
        model = ProfilImage
        fields = ('description', 'photo',)


class QRmatrixForm(forms.ModelForm):  # クオーターを利用して授業を検索するフォーム
    class Meta:
        model = QRmatrix
        fields = ('A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
                  'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
                  'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
                  'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
                  'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7',
                  'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7',
                  'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7',
                  'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7',
                  'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7',
                  'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7',
                  )
        widgets = {}
        for i in fields:
            widgets[i] = forms.TextInput(attrs={'size': 20})


class DocumentFileForm(forms.ModelForm):
    class Meta:
        model = DocumentFile
        fields = ('description', 'documentfile')
        widgets = {'description': forms.Textarea(
            attrs={'placeholder': 'ファイル名を入力してください'}), }


class PastExamFileForm(forms.ModelForm):
    class Meta:
        model = PastExamFile
        fields = ('description', 'pastexamfile')
        widgets = {'description': forms.Textarea(
            attrs={'placeholder': 'ファイル名を入力してください'}), }
