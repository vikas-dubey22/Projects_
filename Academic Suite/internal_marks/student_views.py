from django.shortcuts import render,redirect
from marks_app.models import Student_Notification,student,Student_Feedback,Staff,Student_leave,Subject,Attendance,Attendance_Report,Student_Result
from django.contrib import messages
from django.core.files.storage import default_storage
from django.template.loader import render_to_string

def STUDENT_HOME(request):
    return render(request, 'student/home.html')


def STUD_DASH(request):
    return render(request, 'student/dashboard.html')

def STUDENT_NOTIFICATIONS(request):
    stud = student.objects.filter(admin = request.user.id)
    for i in stud:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification':notification,
        }
    return render(request, 'student/notification.html',context)


def STUDENT_NOTIFICATION_MARK_DONE(request, status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('stud_notification')


def STUDENT_FEED(request):
    student_id = student.objects.get(admin = request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id = student_id)
    context = {
        'feedback_history':feedback_history,
    }
    return render(request, 'student/student_feedback.html',context)


def STUDENT_FEED_SAVE(request):
     if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        stud = student.objects.get(admin=request.user.id)
        feedback = Student_Feedback(
            student_id=stud,
            feedback=feedback_text,
            feedback_reply="",  # You might want to handle this field as well
        )
        feedback.save()
        messages.success(request,'successfully sent')
     return redirect('student_feedback')

def STUDENT_APPLY_FOR_LEAVE(request):
    stud = student.objects.get(admin = request.user.id)
    stud_leave_history = Student_leave.objects.filter(student_id = stud)
    context = {
        'stud_leave_history':stud_leave_history,
    }
    return render(request,'student/apply_leave.html',context)


def STUDENTLEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_reason = request.POST.get('leave_reason')

        student_id = student.objects.get(admin = request.user.id)
        stud_leave = Student_leave(
            student_id = student_id,
            data = leave_date,
            message = leave_reason,
        )
        stud_leave.save()
        messages.success(request,'Successfully Applied For Leave!')
        return redirect('student_apply_leave')
    

def STUDENT_SEE_ATTENDANCE(request):
    stud = student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course=stud.course_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None  # Initialize with an empty queryset

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            attendance_report = Attendance_Report.objects.filter(student_id=stud, attendance_id__subject_id=subject_id)

    context = {
        'subjects': subjects,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report,
    }
    return render(request, 'student/view_attendance.html', context)


# views.py

def VIEW_RES(request):
    stud = student.objects.get(admin=request.user.id)
    result = Student_Result.objects.filter(student_id=stud)
    mark = None

    total_subjects = 0
    total_grade_points = 0

    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark
        i.mark = assignment_mark + exam_mark

        # Assuming a grading scale where grades are assigned based on marks
        if i.mark >= 90:
            grade_point = 10.0
        elif 80 <= i.mark < 90:
            grade_point = 9.0
        elif 70 <= i.mark < 80:
            grade_point = 8.0
        elif 60 <= i.mark < 70:
            grade_point = 7.0
        elif 50 <= i.mark < 60:
            grade_point = 6.0
        else:
            grade_point = 0.0  # Assuming 0.0 for failing grades

        total_subjects += 1
        total_grade_points += grade_point

        # Save the calculated grade_point to the Student_Result model
        i.grade_point = grade_point
        i.save()

    if total_subjects > 0:
        cgpa = total_grade_points / total_subjects
    else:
        cgpa = 0.0  # Default CGPA if there are no subjects

    stud.cgpa = cgpa
    stud.save()
    context = {
        'result': result,
        'mark': mark,
        'cgpa': cgpa,
    }
    return render(request, 'student/view_result.html', context)

