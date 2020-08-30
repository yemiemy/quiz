from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, UserAnswer, UserQuizScore, Story
# Create your views here.


def quiz(request):

    # Get all Questions
    story_qs = Story.objects.all()
    quiz_qs = Question.objects.all()
    score = 0

    try:
        if request.method == 'POST':
            count = 0
            for question in quiz_qs:
                count+=1
                try:
                    reply = request.POST[f'{count}']
                    print(reply)
                except:
                    reply = None
                UserAnswer.objects.create(
                    question=question, 
                    response=reply
                    )
                # check if the user reply is the correct answer.
                if reply == question.answer:
                    score +=5
            # print(score)
            percent_score = int((score/25) * 100)
            # print(percent_score)

            
            user_score = UserQuizScore.objects.create(
                score = score,
                is_attempted = True
            )
            user_score.save()
            # print("Object" + str(user_score))
            # print("if " + str(user_score.score))
            # print("Percentage " + str(percent_score))
            if percent_score >=75:
                messages.success(request, f'Congratulations! You got {percent_score}% out of 100%. You passed this Test.')
            elif percent_score <75:
                messages.warning(request, f'Oops! You got {percent_score}% out of 100%. Unfortunately, you need over 75% to pass this test.')
            
            request.session['result'] = percent_score

            return redirect('/result')
    except:
        pass



    context = {
        'quiz':quiz_qs, 
        'quiz_is_attempted': False,
        'story':story_qs
        
    }
    return render(request, "quizz.html", context)

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, "result.html", context)
