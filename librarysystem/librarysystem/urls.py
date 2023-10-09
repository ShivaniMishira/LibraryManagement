from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sign_in_entry , name="sign_in_entry"),
    path('sign_in_submit', views.sign_in_submit , name="sign_in_submit"),
    path('sign_up_submit', views.sign_up_submit , name="sign_up_submit"),
    path('sign_up_entry', views.sign_up_entry , name="sign_up_entry"),
    path('sign_out', views.sign_out , name="sign_out"),
    path('for_pass', views.for_pass , name="for_pass"),
    path('user_show', views.user_show , name="user_show"),
    path('book_show', views.book_show, name="book_show"),
    path('book_add', views.book_add, name="book_add"),
    path('book_issued', views.book_issued, name="book_issued"),
    path('issue_show', views.issue_show, name="issue_show"),
    path('issue_form', views.issue_form, name="issue_form"),
    path('book_return', views.book_return, name="book_return"),
    path('ret', views.ret, name="ret"),
    path('ret_show', views.ret_show, name="ret_show"),
    path('book_update/<int:id>', views.book_update, name="book_update"),
    path('book_edit/<int:id>', views.book_edit, name="book_edit"),
    path('book_delete/<int:id>', views.book_delete, name="book_delete"),
    path('book_issued/<int:id>', views.book_issued, name="book_issued"),
    path('stu_update', views.stu_update, name="stu_update"),
    path('stu_edit', views.stu_edit, name="stu_edit"),
    path('prem', views.prem, name="prem"),
    path('sub', views.sub, name="sub"),
    path('forum', views.forum, name="forum"),
    path('forumadd', views.forumadd, name="forumadd"),
    path('reply/<int:id>', views.reply, name="reply"),
    path('discussion', views.discussion, name="discussion"),
    path('search', views.search, name="search"),
    path('post_search', views.post_search, name="post_search"),
    path('student_profile', views.student_profile, name="student_profile"),


    
]


