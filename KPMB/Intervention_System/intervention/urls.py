from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),

    # main page for each roles
    path("student/<str:studentId>", views.studentPage, name="studentPage"),
    path("lecturer/<str:mentorId>", views.lecturerPage, name="lecturerPage"),
    path("admin/<str:adminId>", views.adminPage, name="adminPage"),

    # lecturer make report about student behavior
    path("lecturer/lectReport/<str:mentorId>", views.viewsReport, name="lectReport"),
    path("lecturer/lectReport/report/<str:mentorId>", views.lectReport),
    path("lecturer/lectReport/report/updateReport/<str:repId>", views.viewUpdateReport, name="updateLectReport"),
    path("lecturer/lectReport/report/updateReport/update/<str:repId>", views.submitUpdateReport),

    # Lecturer delete report
    path("lecturer/lectReport/report/deleteReport/<str:repId>/<str:mentorId>", views.viewDeleteReport, name="viewDeleteRepo"),
    # path("lecturer/lectReport/report/deleteReport/delete/<str:repId>", views.submitDeleteReport, name="submitDeleteRepo"),

    # Lecturer search report
    path("lecturer/<str:mentorId>/search", views.searchReport, name="searchReportData"),

    # lecturer find student and mentee
    path("lecturer/myStudent/<str:mentorId>", views.displayStudent, name="myStudent"),
    path("lecturer/myStudent/findMyMentee/<str:mentorId>", views.findMyMentee, name="findMyMentee"),

    # lecturer make appointment
    path("lecturer/myAppointment/<str:mentorId>", views.makeAppointment, name="homeAppointment"),
    path("lecturer/myAppointment/submitAppointment/<str:mentorId>", views.submitAppointment, name="submitLectApp"),
    path("lecturer/myAppointment/submitAppointment/updateViewsAppointment/<str:appId>", views.updateAppointment, name="makeAppointment"),
    # path("lecturer/myAppointment/submitAppointment/updateAppointment/<str:appId>", views.updateAppointment, name="makeAppointment"),
    path("lecturer/myAppointment/submitAppointment/updateAppointment/update/<str:appId>", views.submitUpdateAppointment, name="submitAppointment"),
    path("lecturer/myAppointment/pending/<str:mentorId>", views.viewPendingApp, name="Pending"),
    path("lecturer/myAppointment/success/<str:appId>/<str:mentorId>", views.approveApp, name="success"),
    path("lecturer/myAppointment/reject/<str:appId>/<str:mentorId>", views.rejectApp, name="reject"),

    # Lecturer delete appointment
    path("lecturer/myAppointment/submitAppointment/<str:appId>/<str:mentorId>", views.viewDeleteAppo, name="viewDeleteAppo"),

    # ADMIN SECTION --------------------------------------------------->>>>

    # Display report by lecturer
    path("admin/report/<str:adminId>", views.displayReport, name="adminDisplayReport"),
    # Display appointment by lecturer
    path("admin/appointment/<str:adminId>", views.displayApp, name="adminDisplayApp"),

    path("admin/student/<str:adminId>", views.adminDisplayStudent, name="adminDisplayStudent"),

    path("admin/mentor/<str:adminId>", views.adminDisplayMentor, name="adminDisplayMentor"),

    # boleh tambah student and tentu kan mentor dieorang
    path("admin/addStudent/<str:adminId>", views.adminAddStudent, name="adminAddStudent"),
    path("admin/addStudent/<str:adminId>/addingStudent", views.adminSubmitAddStudent, name="addStudent"),
    
    # boleh tambah lecturer
    path("admin/addMentor/<str:adminId>", views.adminAddMentor, name="adminAddMentor"),
    path("admin/addMentor/<str:adminId>/addingMentor", views.adminSubmitAddMentor, name="addMentor"),
    
    # boleh delete lecturer
    path("admin/deleteMentor/<str:adminId>/<str:mentorId>", views.adminDeleteMentor, name="adminDeleteMentor"),

    # boleh delete student
    path("admin/deleteStudent/<str:adminId>/<str:studentId>", views.adminDeleteStudent, name="adminDeleteStudent"),


# STUDENT SECTION ---------------------->
    path('student/profile/<str:studentId>',views.viewProfileStudent,name='profile'),
    path('student/profile/edit/<str:studentId>',views.editProfileStudent,name='editProfile'),
    path('student/profile/edit/<str:studentId>/editing',views.submitEditProfileStudent,name='submitEditProfile'),
    path('student/<str:studentId>/makeappointment',views.viewStudentAppointment,name='studentViewAppointment'),
    path('student/<str:studentId>/makeappointment/submitApp',views.submitStudentApp,name='submitStudentApp'),
    

    # path("about", views.about, name="about"),
    # path("contact", views.contact, name="contact"),
    # path("newMentor", views.newMentor, name="newMentor"),
    # path("update/<str:mentorId>", views.update, name="update"),
    # path("update/updatedata/<str:mentorId>", views.updateData, name="update"),
    # path("viewdelete/<str:mentorId>", views.viewDelete, name="viewdelete"),
    # path("viewdelete/deletedata/<str:mentorId>", views.delete, name="delete"),
    # path("searchpage", views.searchpage, name="searchpage"),
]