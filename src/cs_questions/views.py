"""
Control authentication and new users registrations.
"""

from django.contrib.auth.models import User
from django import http
from codeschool.shortcuts import render_context, get_object_or_404
from cs_activities import models as activity_models
from cs_auth import models as auth_models
from cs_questions import models

users = User.objects


def question_io(request, id):
    grade = None
    activity = get_object_or_404(models.CodeIoActivity, pk=id)
    answer_key = activity.answer_key
    question = activity.question.codeioquestion
    feedback = None

    if request.method == 'POST':
        source_code = request.POST['source']
        response = activity_models.TextualResponse(
                group=auth_models.SingleUserGroup.from_user(request.user),
                activity=activity,
                text=source_code)
        response.save()
        feedback = answer_key.grade(response)
        feedback.save()
        grade = int(feedback.grade * 100)

    return render_context(
            request, 'cs_questions/question_io.jinja2',
            feedback=feedback,
            grade=grade,
            question=question,
            placeholder_text=answer_key.placeholder,
            can_download=request.user == activity.course.teacher,
    )


def question_io_download(request, pk):
    activity = get_object_or_404(models.CodeIoActivity, pk=pk)
    question = activity.question.codeioquestion
    if request.user != activity.course.teacher:
        return http.HttpResponseForbidden()
    return http.HttpResponse(question.as_markio(),
                             content_type='text/markdown')


def index(request):
    return render_context(
            request, 'base.jinja2',
            content='<p>Em construção</p>')
