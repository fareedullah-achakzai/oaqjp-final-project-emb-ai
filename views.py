from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission

@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        enrollment = get_object_or_404(
            Enrollment,
            user=request.user,
            course=course
        )

        submission = Submission.objects.create(enrollment=enrollment)

        selected_choices = []

        for key in request.POST:
            if key.startswith('choice'):
                selected_choices.extend(request.POST.getlist(key))

        choices = Choice.objects.filter(id__in=selected_choices)
        submission.choices.set(choices)

        return redirect(
            'onlinecourse:show_exam_result',
            course_id=course.id,
            submission_id=submission.id
        )

    return redirect('onlinecourse:course_details', course_id=course.id)


@login_required
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)

    submission = get_object_or_404(
        Submission,
        pk=submission_id,
        enrollment__user=request.user,
        enrollment__course=course
    )

    questions = Question.objects.filter(course=course)
    selected_choices = submission.choices.all()

    selected_ids = [choice.id for choice in selected_choices]

    total_grade = sum(question.grade for question in questions)
    total_score = 0

    for question in questions:
        if question.is_get_score(selected_ids):
            total_score += question.grade

    percentage_score = (
        (total_score / total_grade) * 100
        if total_grade > 0 else 0
    )
    selected_ids = list(selected_choices.values_list('id', flat=True))

    context = { 'selected_ids': selected_ids,
        'course': course,
        'submission': submission,
        'grade': total_score,
        'total_grade': total_grade,
        'percentage_score': percentage_score,
        'choices': selected_choices,
    }

    return render(
        request,
        'onlinecourse/exam_result_bootstrap.html',
        context
    )
