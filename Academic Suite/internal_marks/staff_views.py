from django.shortcuts import render,redirect
from marks_app.models import Staff, Staff_Notification, Staff_Leave, Staff_Feedback,Subject,Session_Year,Course,student, Attendance, Attendance_Report, Student_Result
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage


@login_required(login_url='/')
def HOME(request):
    return render(request,'staff/staff_home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        notification = Staff_Notification.objects.filter(staff_id = staff_id)
        context = {
            'notification':notification,
        }
    return render(request,'staff/notifications.html',context)

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_Leave.objects.filter(staff_id = staff_id)

        context = {
            'staff_leave_history':staff_leave_history,
        }
    return render(request, 'Staff/staff_apply_leave.html',context)


@login_required(login_url='/')
def STAFF_SAVE(request):
    if request.method=="POST":
        leave_date = request.POST.get('leave_date')
        leave_reason = request.POST.get('leave_reason')
        staff = Staff.objects.get(admin = request.user.id)
        
        leave = Staff_Leave(
            staff_id = staff,
            data = leave_date,
            message = leave_reason,
        )
        leave.save()
        messages.success(request,'Applied For Leave')
        return redirect('staff_apply_leave')
    
@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin= request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id = staff_id)
    context = {
        'staff_id':staff_id,
        'feedback_history':feedback_history,
    }
    return render(request,'Staff/staff_feedback.html',context)

@login_required(login_url='/')
def STAFF_SAVE_FEEDBACK(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        staff = Staff.objects.get(admin=request.user.id)
        attached_file = request.FILES.get('attached_file')

        feedback = Staff_Feedback(
            staff_id=staff,
            feedback=feedback_text,
            feedback_reply="",  # You might want to handle this field as well
        )

        if attached_file:
            # Save the attached file
            file_name = f"feedback_attachment_{staff.id}_{attached_file.name}"
            file_path = default_storage.save(file_name, attached_file)
            feedback.attachment = file_path
        feedback.save()
        messages.success(request,'successfully')

    return redirect('staff_feedback')

@login_required(login_url='/')
def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    # Fetch subjects associated with the staff member
    subject = Subject.objects.filter(staff=staff_id)

    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    
    get_subject = None
    get_session_year = None
    stud = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id = session_year_id)
            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                stud_id = i.course.id
                stud = student.objects.filter(course_id = stud_id)
    context = { 
        'subject': subject,
        'session_year': session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action, 
        'stud':stud,
    }

    return render(request, 'staff/take_attendance.html', context)


@login_required(login_url='/')
def STAFF_STORE_ATTENDANCE(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        stu_id = request.POST.getlist('stu_id')

        # Check if 'Select Session Year' is selected
        if session_year_id == 'Select Session Year':
            messages.error(request, 'Please select a valid session year.')
            return redirect('take_attendance')

        try:
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            attendance = Attendance(
                subject_id=get_subject,
                attendance_data=attendance_date,
                session_year_id=get_session_year,
            )
            attendance.save()

            for stu_id in stu_id:
                i_st = int(stu_id)
                p_studs_qs = student.objects.filter(id=i_st)

                if p_studs_qs.exists():
                    p_studs = p_studs_qs.get()
                    attendance_report = Attendance_Report(
                        student_id=p_studs,
                        attendance_id=attendance,
                    )
                    attendance_report.save()
                else:
                    print(f"No student found with id {i_st}")

            messages.success(request, 'Attendance saved successfully!')
        except Subject.DoesNotExist:
            messages.error(request, 'Selected subject does not exist.')
        except Session_Year.DoesNotExist:
            messages.error(request, 'Selected session year does not exist.')

    return redirect('take_attendance')


@login_required(login_url='/')
def STAFF_GET_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    
    subject = Subject.objects.filter(staff_id = staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')
            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id = session_year_id)
            
            attendance = Attendance.objects.filter(subject_id = get_subject,attendance_data= attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id = attendance_id)
    context = {
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'attendance_report':attendance_report,
    }
    return render(request,'staff/view_attendance.html',context)

@login_required(login_url='/')
def STAFF_ADD_MARKS(request):
    staff = Staff.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(staff_id=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    stud = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_Year.objects.get(id=session_year_id)
            # Instead of reassigning subjects, use the existing subjects variable
            for i in subjects:
                student_id = i.course.id
                stud = student.objects.filter(course_id=student_id)  # Assuming your student model is named 'student'

    context = {
        'subjects': subjects,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session,
        'stud': stud,
    }
    return render(request, 'staff/add_result.html', context)

@login_required(login_url='/')
def STAFF_SAVE_RES(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        exam_mark = request.POST.get('exam_mark')

        # Check if assignment_mark and exam_mark are valid numbers
        if not assignment_mark.isdigit() or not exam_mark.isdigit():
            messages.error(request, 'Invalid marks. Please enter valid numbers.')
            return redirect('staff_add_result')

        get_student = student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exists = Student_Result.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exists:
            result =  Student_Result.objects.get(subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = exam_mark
            result.save()
            messages.success(request, 'Updated Successfully')
            return redirect('staff_add_result')
        else:
            result = Student_Result(
                student_id=get_student,
                subject_id=get_subject,
                exam_mark=exam_mark,
                assignment_mark=assignment_mark, 
            )
            result.save()
            messages.success(request, 'Added Successfully')
            return redirect('staff_add_result')
