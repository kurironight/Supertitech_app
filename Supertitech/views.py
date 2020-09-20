from django.http import HttpResponse
import csv
from io import TextIOWrapper
from .forQR import scrapingLogin
from .QRfromuser import QRLogin, extractQR
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PastExamFileForm, DocumentFileForm, SignUpForm, LoginForm, \
    QuarterSelectionForm, QuarterSelectformenu, PostForm, ResPostForm, \
    ProfilImageForm, QRmatrixForm
from django.contrib.auth import login
from .models import DocumentFile, Star, Subject,\
    Reputation, Res, ProfilImage, PastExamFile, QRmatrix


def csvtest(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        testlist = []
        for line in csv_file:
            testlist.append(line[3])

        a = testcsv.objects.first()
        return HttpResponse(a.a[1])


def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            youbilist = line[3].split('  ')
            for youbi in youbilist:
                if len(youbi) < 4:
                    pass
                elif not (youbi[1].isdigit() and youbi[3].isdigit()):
                    pass
                else:
                    timelist = []
                    if((float(youbi[1])+1)//2 == float(youbi[3])//2):
                        timelist.append(float(youbi[3])//2)
                    else:
                        timelist.append((float(youbi[1])+1)//2)
                        timelist.append(float(youbi[3])//2)
                    for time in timelist:
                        subject = Subject()
                        subject.title = line[1]
                        subject.teacher = line[2]
                        # 曜日を数値に変換して代入する
                        if(line[3][0] == "  "):
                            subject.data3 = 0
                        else:
                            if(youbi[0] == '月'):
                                subject.youbi = 1
                            elif(youbi[0] == '火'):
                                subject.youbi = 2
                            elif(youbi[0] == '水'):
                                subject.youbi = 3
                            elif(youbi[0] == '木'):
                                subject.youbi = 4
                            else:
                                subject.youbi = 5
                        subject.time = time
                        subject.classroom = youbi[5:len(youbi)-1]
                        subject.Q = line[6]
                        subject.code = line[4]
                        subject.credit = line[5]
                        subject.content = line[7]
                        subject.grade = line[4][5]
                        subject.save()

        return render(request, 'Supertitech/upload.html')
    else:
        return render(request, 'Supertitech/upload.html')


def profile(request):
    if request.method == 'POST':
        form = ProfilImageForm(request.POST, request.FILES)
        if form.is_valid():
            ProfilImage.objects.filter(owner=request.user).delete()
            image = form.save()
            image.owner = request.user
            image.save()

            return redirect('test')
    else:
        form = ProfilImageForm()
        obj = ProfilImage.objects.filter(owner=request.user)

    return render(request, 'Supertitech/profile.html', {
        'form': form,
        'obj': obj
    })


@login_required
def QRmatrixsite(request):
    if request.method == 'POST':
        form = QRmatrixForm(request.POST)
        if form.is_valid():
            QRmatrix.objects.filter(owner=request.user).delete()
            QR = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            QR.owner = request.user  # Set the user object here
            QR.save()  # Now you can send it to DB

        return render(request, 'Supertitech/QRmatrix.html', {
            'QR_form': form,
        })
    else:
        try:
            data = QRmatrix.objects.get(owner=request.user)
            form = QRmatrixForm(instance=data)  # フォームの中に最初からデータが入っているように見せるため
        except:
            form = QRmatrixForm()

        return render(request, 'Supertitech/QRmatrix.html', {
            'QR_form': form,
        })


@login_required
def goportalbeta(request):

    data = QRmatrix.objects.get(owner=request.user)
    form = QRmatrixForm(instance=data)
    matrix = extractQR(data)
    QRLogin(matrix)
    return render(request, 'Supertitech/QRmatrix.html', {
        'message': 'success',
        'QR_form': form,
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'Supertitech/r_success.html')
    else:
        form = SignUpForm()
    return render(request, 'Supertitech/signup.html', {'form': form})


@login_required
def menu(request):
    # publicは、searchリンクに曜日および時間の情報を伝えるため、ダミーで作ったユーザー
    public = User.objects.filter(username='public').first()
    if request.method == 'POST':
        quarterselection = QuarterSelectformenu(request.POST)
        qota = request.POST['choice']
        schedule = [['1限', 0, 0, 0, 0, 0], [
            '2限', 0, 0, 0, 0, 0], [
            '3限', 0, 0, 0, 0, 0], [
            '4限', 0, 0, 0, 0, 0], [
            '5限', 0, 0, 0, 0, 0]]
        for i in range(0, 5):  # [1:1時限,2:2時限,...,5:5時限]
            for j in range(1, 6):  # [1:月曜,2:火曜,...,5:金曜]
                if Subject.objects.filter(
                        user=request.user).filter(time=i + 1).filter(youbi=j).filter(Q=qota).exists():  # when user enroll the subject exists,
                    z = Subject.objects.filter(
                        user=request.user).filter(time=i + 1).filter(youbi=j).filter(Q=qota).first()
                    schedule[i][j] = z
                elif Subject.objects.filter(
                        user=public).filter(time=i + 1).filter(youbi=j).filter(Q=qota).exists():  # when the subject exists on that time,
                    empty = Subject.objects.filter(
                        user=public).filter(time=i + 1).filter(youbi=j).filter(Q=qota).first()
                    schedule[i][j] = empty
                else:
                    schedule[i][j] = 'まだpublicに登録してない'
    else:
        quarterselection = QuarterSelectformenu()
        schedule = [['1限', 0, 0, 0, 0, 0], ['2限', 0, 0, 0, 0, 0], [
            '3限', 0, 0, 0, 0, 0], ['4限', 0, 0, 0, 0, 0], ['5限', 0, 0, 0, 0, 0]]
        for i in range(0, 5):  # [1:1時限,2:2時限,...,5:5時限]
            for j in range(1, 6):  # [1:月曜,2:火曜,...,5:金曜]
                if Subject.objects.filter(
                        user=request.user).filter(time=i + 1).filter(youbi=j).filter(Q=1).exists():  # when user enroll the subject exists,
                    z = Subject.objects.filter(
                        user=request.user).filter(time=i + 1).filter(youbi=j).filter(Q=1).first()
                    schedule[i][j] = z
                elif Subject.objects.filter(
                        user=public).filter(time=i + 1).filter(youbi=j).filter(Q=1).exists():  # when the subject exists on that time,
                    empty = Subject.objects.filter(
                        user=public).filter(time=i + 1).filter(youbi=j).filter(Q=1).first()
                    schedule[i][j] = empty
                else:
                    schedule[i][j] = 'まだpublicに登録してない'

    params = {
        'user': request.user,
        'quarter_form': quarterselection,
        'times': schedule,
    }
    return render(request, 'Supertitech/menu.html', params)

# 授業を時間割に登録する


def add(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    get_subject = Subject.objects.filter(title=subject.title)
    flag = True
    for item in get_subject:
        flag = flag and Subject.objects.filter(time=item.time) \
            .filter(youbi=item.youbi).exists()

    if flag == 0:
        message = 'すでに登録済みよ'
    else:
        message = '登録するわ'
        for item in get_subject:
            item.user.add(request.user)  # manytomanyの場合はaddがsave代わり
    params = {
        'title': 'Add',
        'message': message,
        'item': subject,
    }
    return render(request, 'Supertitech/add.html', params)

# 登録した時間割を削除する


def subdelete(request, subject_id):
    public = User.objects.filter(username='public').first()
    get_subject = Subject.objects.get(id=subject_id)
    subjectlist = Subject.objects.filter(title=get_subject.title)
    for item in subjectlist:
        item.user.remove(request.user)

    qota = get_subject.Q
    quarterselection = QuarterSelectformenu()
    schedule = [['1限', 0, 0, 0, 0, 0], ['2限', 0, 0, 0, 0, 0], [
        '3限', 0, 0, 0, 0, 0], ['4限', 0, 0, 0, 0, 0], ['5限', 0, 0, 0, 0, 0]]
    for i in range(0, 5):  # [1:1時限,2:2時限,...,5:5時限]
        for j in range(1, 6):  # [1:月曜,2:火曜,...,5:金曜]
            if Subject.objects.filter(
                    user=request.user).filter(time=i + 1).filter(youbi=j).filter(Q=qota).exists():  # when user enroll the subject exists,
                z = Subject.objects.filter(
                    user=request.user).filter(time=i + 1).filter(youbi=j).filter(Q=qota).first()
                schedule[i][j] = z
            elif Subject.objects.filter(
                    user=public).filter(time=i + 1).filter(youbi=j).filter(Q=qota).exists():  # when the subject exists on that time,
                empty = Subject.objects.filter(
                    user=public).filter(time=i + 1).filter(youbi=j).filter(Q=qota).first()
                schedule[i][j] = empty
            else:
                schedule[i][j] = 'まだpublicに登録してない'

    #image = ProfilImage.objects.get(owner=request.user)
    params = {
        'user': request.user,
        'quarter_form': quarterselection,
        'times': schedule,
    }
    return render(request, 'Supertitech/menu.html', params)

# 授業評価ページ


def reputation(request, subject_id):
    request_subject = Subject.objects.get(id=subject_id)
    print(request_subject.title)
    get_subject = Subject.objects.filter(title=request_subject.title).first()
    # POST送信時の処理
    if request.method == 'POST':
        if 'reviewbutton' in request.POST:
            if Reputation.objects.filter(owner=request.user, subject=get_subject).exists():
                return render(request, 'Supertitech/alreadypost.html')
            else:
                # 送信内容の取得
                content = request.POST['content']
            # Reputationを作成して保存
                rep = Reputation()
                rep.subject = get_subject
                rep.content = content
                rep.owner = request.user
                rep.save()
        elif 'resbutton' in request.POST:
            content = request.POST['content']
            res = Res()
            res.owner = request.user
            res.subject = get_subject
            res.content = content
            res.save()

        elif 'docupload' in request.POST:
            docform = DocumentFileForm(request.POST, request.FILES)
            if docform.is_valid():
                obj = docform.save(commit=False)
                obj.owner = request.user
                obj.subject = get_subject
                obj.save()
            else:
                pass

        elif 'examupload' in request.POST:
            examform = PastExamFileForm(request.POST, request.FILES)
            if examform.is_valid():
                obj = examform.save(commit=False)
                obj.owner = request.user
                obj.subject = get_subject
                obj.save()
            else:
                pass

    # 共通処理
    examform = PastExamFileForm()
    docform = DocumentFileForm()
    reputations = Reputation.objects.filter(subject=get_subject)
    form = PostForm(request.user)
    ResForm = ResPostForm(request.user)
    Reslist = Res.objects.filter(subject=get_subject)
    documentlist = DocumentFile.objects.filter(subject=get_subject)
    pastexamlist = PastExamFile.objects.filter(subject=get_subject)
    pinres = Res.objects.filter(
        subject=get_subject).filter(pinuser=request.user)
    params = {
        'pinres': pinres,
        'examform': examform,
        'docform': docform,
        'subject': get_subject,
        'responses': Reslist,
        'contents': reputations,
        'form': form,
        'resform': ResForm,
        'subject_id': subject_id,
        'documentlist': documentlist,
        'pastexamlist': pastexamlist,
    }
    return render(request, 'Supertitech/reputation.html', params)

# ピン止めをクリックしたとき


def pincheck(request, res_id):
    get_res = Res.objects.get(id=res_id)
    get_subject = get_res.subject
    pinres = Res.objects.filter(
        subject=get_subject).filter(pinuser=request.user)
    pinuserlist = get_res.pinuser.all()
    if request.user in pinuserlist:
        get_res.pinuser.remove(request.user)
    else:
        get_res.pinuser.add(request.user)

    examform = PastExamFileForm()
    docform = DocumentFileForm()
    reputations = Reputation.objects.filter(subject=get_subject)
    form = PostForm(request.user)
    ResForm = ResPostForm(request.user)
    Reslist = Res.objects.filter(subject=get_subject)
    documentlist = DocumentFile.objects.filter(subject=get_subject)
    pastexamlist = PastExamFile.objects.filter(subject=get_subject)
    params = {
        'pinres': pinres,
        'examform': examform,
        'docform': docform,
        'subject': get_subject,
        'responses': Reslist,
        'contents': reputations,
        'form': form,
        'resform': ResForm,
        'subject_id': get_subject.id,
        'documentlist': documentlist,
        'pastexamlist': pastexamlist,
    }
    return render(request, 'Supertitech/reputation.html', params)

# 過去問を消去するとき


def examdelete(request, exam_id):
    get_exam = PastExamFile.objects.get(id=exam_id)
    get_subject = get_exam.subject
    get_exam.delete()

    pinres = Res.objects.filter(
        subject=get_subject).filter(pinuser=request.user)
    reputations = Reputation.objects.filter(subject=get_subject)
    form = PostForm(request.user)
    Reslist = Res.objects.filter(subject=get_subject)
    ResForm = ResPostForm(request.user)
    docform = DocumentFileForm()
    examform = PastExamFileForm()
    documentlist = DocumentFile.objects.filter(subject=get_subject)
    pastexamlist = PastExamFile.objects.filter(subject=get_subject)
    params = {
        'pinres': pinres,
        'examform': examform,
        'docform': docform,
        'subject': get_subject,
        'responses': Reslist,
        'contents': reputations,
        'form': form,
        'resform': ResForm,
        'subject_id': get_subject.id,
        'documentlist': documentlist,
        'pastexamlist': pastexamlist,
    }
    return render(request, 'Supertitech/reputation.html', params)

# 資料を削除するとき


def docdelete(request, document_id):
    get_document = DocumentFile.objects.get(id=document_id)
    get_subject = get_document.subject
    get_document.delete()

    pinres = Res.objects.filter(
        subject=get_subject).filter(pinuser=request.user)
    reputations = Reputation.objects.filter(subject=get_subject)
    form = PostForm(request.user)
    Reslist = Res.objects.filter(subject=get_subject)
    ResForm = ResPostForm(request.user)
    docform = DocumentFileForm()
    examform = PastExamFileForm()
    documentlist = DocumentFile.objects.filter(subject=get_subject)
    pastexamlist = PastExamFile.objects.filter(subject=get_subject)
    params = {
        'pinres': pinres,
        'examform': examform,
        'docform': docform,
        'subject': get_subject,
        'responses': Reslist,
        'contents': reputations,
        'form': form,
        'resform': ResForm,
        'subject_id': get_subject.id,
        'documentlist': documentlist,
        'pastexamlist': pastexamlist,
    }
    return render(request, 'Supertitech/reputation.html', params)

# いいねボタンを押したとき


@login_required
def good(request, repu_id):
    get_reputation = Reputation.objects.get(id=repu_id)
    get_subject = get_reputation.subject
    if Star.objects.filter(owner=request.user).filter(repu=get_reputation).exists():
        pass
    else:
        star = Star()
        star.owner = request.user
        star.repu = get_reputation
        star.save()
        get_reputation.good_count += 1
        get_reputation.save()

    pinres = Res.objects.filter(
        subject=get_subject).filter(pinuser=request.user)
    reputations = Reputation.objects.filter(subject=get_reputation.subject)
    form = PostForm(request.user)
    Reslist = Res.objects.filter(subject=get_reputation.subject)
    ResForm = ResPostForm(request.user)
    docform = DocumentFileForm()
    examform = PastExamFileForm()
    documentlist = DocumentFile.objects.filter(subject=get_subject)
    pastexamlist = PastExamFile.objects.filter(subject=get_subject)
    params = {
        'pinres': pinres,
        'examform': examform,
        'docform': docform,
        'subject': get_subject,
        'contents': reputations,
        'responses': Reslist,
        'form': form,
        'resform': ResForm,
        'subject_id': get_reputation.subject.id,
        'documentlist': documentlist,
        'pastexamlist': pastexamlist,
    }
    return render(request, 'Supertitech/reputation.html', params)

# 自分のレビューを削除するとき


@login_required
def repudelete(request, delete_id):
    get_reputation = Reputation.objects.get(id=delete_id)
    starlist = Star.objects.filter(repu=get_reputation)
    for item in starlist:
        item.delete()

    get_subject = Subject.objects.get(id=get_reputation.subject.id)
    pinres = Res.objects.filter(
        subject=get_subject).filter(pinuser=request.user)
    get_reputation.delete()
    reputations = Reputation.objects.filter(subject=get_subject)
    form = PostForm(request.user)
    Reslist = Res.objects.filter(subject=get_subject)
    ResForm = ResPostForm(request.user)
    docform = DocumentFileForm()
    examform = PastExamFileForm()
    documentlist = DocumentFile.objects.filter(subject=get_subject)
    pastexamlist = PastExamFile.objects.filter(subject=get_subject)
    params = {
        'pinres': pinres,
        'examform': examform,
        'docform': docform,
        'subject': get_subject,
        'responses': Reslist,
        'contents': reputations,
        'form': form,
        'resform': ResForm,
        'subject_id': get_subject.id,
        'documentlist': documentlist,
        'pastexamlist': pastexamlist,
    }
    return render(request, 'Supertitech/reputation.html', params)


def resdelete(request, delete_id):
    get_res = Res.objects.get(id=delete_id)
    get_subject = Subject.objects.get(id=get_res.subject.id)
    get_res.delete()

    pinres = Res.objects.filter(
        subject=get_subject).filter(pinuser=request.user)
    reputations = Reputation.objects.filter(subject=get_subject)
    form = PostForm(request.user)
    Reslist = Res.objects.filter(subject=get_subject)
    ResForm = ResPostForm(request.user)
    docform = DocumentFileForm()
    examform = PastExamFileForm()
    documentlist = DocumentFile.objects.filter(subject=get_subject)
    pastexamlist = PastExamFile.objects.filter(subject=get_subject)
    params = {
        'pinres': pinres,
        'examform': examform,
        'docform': docform,
        'subject': get_subject,
        'responses': Reslist,
        'contents': reputations,
        'form': form,
        'resform': ResForm,
        'subject_id': get_subject.id,
        'documentlist': documentlist,
        'pastexamlist': pastexamlist,
    }
    return render(request, 'Supertitech/reputation.html', params)


class loginView(LoginView):
    form_class = LoginForm
    template_name = "Supertitech/login.html"


def search(request):
    public = User.objects.filter(username='public').first()
    if request.method == 'POST':
        quarterselection = QuarterSelectionForm(request.POST)
        # あとでユーザーがまだ選択していない科目を出力できるようにしたい
        # チェックしたQをリストにまとめる
        moji = request.POST['name']  # 検索欄に入力されたデータをぶち込む
        Qlist = []
        Gradelist = []
        timelist = []
        daylist = []
        for item in request.POST.getlist('quarters'):
            Qlist.append(item)
        for item in request.POST.getlist('grades'):
            Gradelist.append(item)
        for item in request.POST.getlist('time'):
            timelist.append(item)
        for item in request.POST.getlist('day'):
            daylist.append(item)

        if Qlist == []:
            data = Subject.objects.all()
        else:
            data = Subject.objects.filter(~Q(user=public)).filter(Q__in=Qlist)

        if Gradelist != []:
            data = data.filter(grade__in=Gradelist)

        if timelist != []:
            data = data.filter(time__in=timelist)

        if daylist != []:
            data = data.filter(youbi__in=daylist)

        if moji != []:
            data = data.filter(title__icontains=moji)

        data = data.order_by('Q', 'youbi', 'time', 'grade')

        params = {
            'user': request.user,
            'title': 'Search',
            'message': '',
            'quarter_form': quarterselection,
            'data': data,
        }
        return render(request, 'Supertitech/search.html', params)

    else:
        data = Subject.objects.all().filter(~Q(user=public)).order_by('Q')
        quarterselection = QuarterSelectionForm()
        params = {
            'user': request.user,
            'title': 'Search',
            'message': data,
            'quarter_form': quarterselection,
            'data': data,
        }
        return render(request, 'Supertitech/search.html', params)


def search_time(request, search_Q, search_youbi, search_time):  # 時間割からのリンク用
    public = User.objects.filter(username='public').first()
    quarterselection = QuarterSelectionForm()
    data = Subject.objects.filter(~Q(user=public)).filter(  # publicを入れないようにしてaddが認識されないようにする
        Q=search_Q).filter(
        youbi=search_youbi).filter(
        time=search_time)
    params = {
        'user': request.user,
        'title': 'search',
        'message': 'search',
        'quarter_form': quarterselection,
        'data': data,
    }
    return render(request, 'Supertitech/search.html', params)


def check(request, check_id):  # idを取得しているkどうかの確認用関数だから消しても良い
    subject = Subject.objects.get(id=check_id)
    message = subject.id
    params = {
        'title': 'check',
        'message': message,
        'item': subject,
    }
    return render(request, 'Supertitech/check.html', params)
