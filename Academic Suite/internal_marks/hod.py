from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from marks_app.models import Course, Session_Year, CustomUser, student, Staff, Subject, Staff_Notification, Staff_Leave, Staff_Feedback, Student_Notification, Student_Feedback, Student_leave, Attendance,Attendance_Report, Student_Result
from django.db import IntegrityError
from django.utils import timezone
from django.db.models import Subquery, OuterRef, Max
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@login_required(login_url='/')
def home(request):
    student_count = student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_gender_male = student.objects.filter(gender = 'Male').count()
    student_gender_female = student.objects.filter(gender = 'Female').count()
    
       

    context = {
        'student_count': student.objects.all().count(),
        'staff_count': Staff.objects.all().count(),
        'course_count': Course.objects.all().count(),
        'subject_count': Subject.objects.all().count(),
        'student_gender_male': student.objects.filter(gender='Male').count(),
        'student_gender_female': student.objects.filter(gender='Female').count(),
        
    }

    return render(request, 'hod/home.html', context)


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            Student = student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            Student.save()
            messages.success(request, "Student Successfully Saved !")
            return redirect('add_student')

    context = {
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'Hod/add_student.html', context)


@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')

        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, "Course Successfully Added !")
        return redirect("add_course")
    return render(request, 'Hod/add_course.html')


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student_ob = student.objects.all()
    context = {
        'student_ob': student_ob,
    }
    return render(request, 'Hod/view_student.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student_ob = student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    context = {
        'student_ob': student_ob,
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'Hod/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student_ob = student.objects.get(admin=student_id)
        student_ob.address = address
        student_ob.gender = gender

        course = Course.objects.get(id=course_id)
        student_ob.course_id = course

        session_year = Session_Year.objects.get(id=session_year_id)
        student_ob.session_year_id = session_year

        student_ob.save()

        messages.success(request, 'Successfully Updated !')

        return redirect('view_student')
    return render(request, 'Hod/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    student_ob = CustomUser.objects.get(id=admin)
    student_ob.delete()
    messages.success(request, 'Deleted Successfully!')
    return redirect('view_student')


@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'Hod/view_course.html', context)


@login_required(login_url='/')
def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'Hod/edit_course.html', context)


@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Successfully Updated !')
        return redirect('view_course')

    return render(request, 'Hod/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request, id):
    try:
        course = Course.objects.get(id=id)
        course.delete()
        messages.success(request, 'Course deleted successfully!')
    except IntegrityError as e:
        messages.error(request, f'IntegrityError: {e}')
    except Course.DoesNotExist:
        messages.error(request, 'Course not found.')

    return redirect('view_course')


@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('add_staff')
        else:
            user = CustomUser(first_name=first_name, last_name=last_name, email=email, username=username,
                              profile_pic=profile_pic, user_type=2)
            user.set_password(password)
            user.save()
            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, 'Data Saved Successfully')
            return redirect('add_staff')

    return render(request, 'Hod/add_staff.html')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }
    return render(request, 'Hod/view_staff.html', context)


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }
    return render(request, 'Hod/edit_staff.html', context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address
        staff.save()
        messages.success(request, 'Successfully Updated')
        return redirect('view_staff')
    return render(request, 'Hod/edit_staff.html')


@login_required(login_url='/')
def DELETE_STAFF(request, admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'SuccessFully Deleted')
    return redirect('view_staff')

@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff=staff,
        )
        subject.save()
        messages.success(request, 'Successfully Saved')
        return redirect('add_subject')
    context = {
        'course': course,
        'staff': staff,
    }
    return render(request, 'Hod/add_subject.html', context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject,
    }
    return render(request, 'Hod/view_subject.html', context)


@login_required(login_url='/')
def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject': subject,
        'course': course,
        'staff': staff,
    }
    return render(request, 'Hod/edit_subject.html', context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff,
        )
        subject.created_at = timezone.now()
        subject.updated_at = timezone.now()

        subject.save()
        messages.success(request, 'Updated Successfully')
        return redirect('view_subject')
    return render(request, 'Hod/edit_subject.html')


@login_required(login_url='/')
def DELETE_SUBJECT(request, id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request, 'Deleted Successfully')
    return redirect('view_subject')

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_start=session_year_start,
            session_end=session_year_end,
        )
        session.save()

        messages.success(request, 'Saved Successfully')
        return redirect('add_session')

    return render(request, 'Hod/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()

    context= {
        'session':session,
    }
    return render(request, 'Hod/view_session.html',context)

@login_required(login_url='/')
def EDIT_SESSION(request, id):
    session = Session_Year.objects.filter(id = id)
    context = {
        'session':session,
    }
    return render(request, 'Hod/edit_session.html', context)

@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'Updated Successfully')
        return redirect('view_session')

@login_required(login_url='/')
def DELETE_SESSION(request, id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request, 'Deleted Successfully')
    return redirect('view_session')

@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'staff':staff,
        'see_notification':see_notification,
    }
    return render(request,'hod/staff_notification.html',context)

@login_required(login_url='/')
def SAVE_NOTIFICATION(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_Notification(
            staff_id=staff,
            message=message,
        )
        notification.save()

        # Add a success message to indicate that the notification has been sent
        messages.success(request, 'Notification Sent')

        return redirect('staff_notification')

    # Clear messages if the request is not a POST request
    storage = messages.get_messages(request)
    storage.used = True

    # Add any other logic for handling non-POST requests or rendering templates
    # ...


@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()
    context = {
        'staff_leave':staff_leave,
    }
    return render(request,'hod/staff_leave_view.html',context)


@login_required(login_url='/')
def STUD_LEAVE_VIEW(request):
    stud_leave = Student_leave.objects.all()
    context = {
        'stud_leave':stud_leave,
    }
    return render(request,'hod/student_leave.html',context)

@login_required(login_url='/')
def STUD_APPROVE(request,id):
    stud_leave = Student_leave.objects.get(id = id)
    stud_leave.status = 1
    stud_leave.save()
    return redirect('get_student_leave_view')

@login_required(login_url='/')
def STUD_REJECT(request,id):
    stud_leave = Student_leave.objects.get(id = id)
    stud_leave.status = 2
    stud_leave.save()
    return redirect('get_student_leave_view')

@login_required(login_url='/')
def STAFF_APPROVE(request,id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STAFF_REJECT(request, id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')

@login_required(login_url='/')
def STAFF_FEED_REPLY(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history':feedback_history,
    }
    return render(request,'Hod/staff_feed.html',context)

@login_required(login_url='/')
def STAFF_REPLY_SAVE(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        attachment = request.FILES.get('attachment')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1

        if attachment:
            # Save the attached file
            file_name = f"feedback_attachment_{feedback.id}_{attachment.name}"
            file_path = default_storage.save(file_name, attachment)
            feedback.attachment = file_path

        feedback.save()

        # Delete the feedback after saving the reply
    return redirect('staff_feed')

@login_required(login_url='/')
def STAFF_DELETE_FEEDBACK(request, feedback_id):
    feedback = get_object_or_404(Staff_Feedback, id=feedback_id)

    # You might want to check if the user has the permission to delete this feedback
    # Add your permission check logic here if needed

    feedback.delete()

    # You can add a success message if you want
    # messages.success(request, 'Feedback deleted successfully.')

    return redirect('staff_feed')

@login_required(login_url='/')
def STUDENT_NOTIFICATION(request):
    stud = student.objects.all()
    notification = Student_Notification.objects.all()
    context = {
        'stud':stud,
        'notification':notification,
    }
    return render(request,'Hod/student_send_notification.html',context)

@login_required(login_url='/')
def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')

        try:
            stud = student.objects.get(admin__id=student_id)
            stud_notification = Student_Notification(
                student_id=stud,
                message=message,
            )
            stud_notification.save()
            messages.success(request, 'Successfully Sent')
            return redirect('student_send_notification')
        except student.DoesNotExist:
            messages.error(request, 'Student not found')
            return redirect('student_send_notification')

        return redirect('student_send_notification')
    
@login_required(login_url='/')
def STUD_FEED(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback':feedback,
        'feedback_history':feedback_history,
    }
    return render(request,'Hod/student_feed.html',context)

@login_required(login_url='/')
def STUD_SAVE_FEED(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
    
       
        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
       
        feedback.save()
    return redirect('get_student_feed')

@login_required(login_url='/')
def STUD_DELETE_FEEDBACK(request, feedback_id):
    feedback = get_object_or_404(Student_Feedback, id=feedback_id)

    # You might want to check if the user has the permission to delete this feedback
    # Add your permission check logic here if needed

    feedback.delete()

    # You can add a success message if you want
    # messages.success(request, 'Feedback deleted successfully.')

    return redirect('get_student_feed')

@login_required(login_url='/')
def VIEW_ATTEND(request):
    subject = Subject.objects.all()
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
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            
            attendance = Attendance.objects.filter(subject_id=get_subject, attendance_data=attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }

    return render(request, 'hod/view_attendance.html', context)
