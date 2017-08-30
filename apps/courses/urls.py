# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/5/13 15:31'

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseInfoView, CommentView, AddComment, VideoPlayView

urlpatterns = [
    #课程机构列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentView.as_view(), name="course_comments"),

    #添加课程评论
    url(r'^add_comment/$', AddComment.as_view(), name="add_comments"),

    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),

]