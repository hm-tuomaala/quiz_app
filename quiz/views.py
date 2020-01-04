from django.shortcuts import render
from quiz.forms import SubmitForm
from clogin.models import Keys
from django.http import HttpResponse


def submit(request, key):
    valid_key = False
    valid_name = ''
    score = 0
    num = 0

    for k in Keys.objects.all():
        if key == k.key and not k.submitted:
            valid_key = True
            valid_name = k.name
    if valid_key:
        quiz_form = SubmitForm()
        context = {
            'form' : quiz_form,
            'name' : valid_name
        }
        if request.method == 'POST':
            quiz_form = SubmitForm(request.POST)
            if quiz_form.is_valid():
                #Calculate the answers
                for i in quiz_form.cleaned_data:
                    print(quiz_form.cleaned_data[i], i[3])
                    score += int(quiz_form.cleaned_data[i])
                    num = int(i[3])
                for k in Keys.objects.all():
                    if k.key == key:
                        k.score = score
                        k.submitted = True
                        k.save()
                context = {
                    'score' : score,
                    'name' : valid_name,
                    'num' : num
                }
                #return HttpResponse('<h1>Postattu - valid</h1>')
                return render(request, 'quiz/answers.html', context)
            else:
                print(quiz_form.errors)
                return HttpResponse('<h1>Postattu - invalid</h1>')
        else:
            return render(request, 'quiz/quiz.html', context)
    else:
        return HttpResponse('<h1>Invalid code</h1>')


def board(request):
    position = 1
    sub_num = 0
    context = {
        'names' : []
    }
    for i in Keys.objects.values():
        if i['submitted']:
            context['names'].append([i['score'], i['name'], 0])
            context['names'].sort(reverse=True)
            sub_num += 1

    for n in context['names']:
        n[2] = position
        position += 1

    if sub_num == 0:
        context = {
            'names' : [[0, 0, 0]]
        }
    print(context)

    return render(request, 'quiz/board.html', context)
    # return HttpResponse('<h1>This is leaderboard</h1>')
