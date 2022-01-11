from django.views.generic import ListView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# --ListView


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'  # template 파일로 넘겨주는 객체 리스트에 대한 context 변수명
    paginate_by = 2  # 한 페이지에 보여주는 객체 리스트의 숫자

# --DetailView


class PostDV(DeleteView):
    model = Post

# --ArchiveView


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True  # 해당연도에 해당하는 객체의 리스트 만들어 템플릿에 넘겨줌


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
