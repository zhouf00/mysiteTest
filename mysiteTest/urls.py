"""mysiteTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from mysiteTest.settings import MEDIA_ROOT

import xadmin

from django.conf.urls.static import static
import mysiteTest.settings as settings
from users.views_user import IndexView, LoginView, LogoutView
from system.views import SystemView
from personal import views as personal_views
from PMsys import views as pmsys_views


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^tinymce', include('tinymce.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'^$', IndexView.as_view(), name='index'),

    # 用户登陆
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 系统设置
    url(r'^system/$', SystemView.as_view(), name='system'),
    url(r'^system/basic/', include(('users.urls', 'system-basic'), namespace='system-basic')),
    url(r'^system/rbac/', include(('rbac.urls', 'system-rbac'), namespace='system-rbac')),

    url(r'^personal/$', personal_views.PersonalView.as_view() , name='personal'),
    url(r'^personal/userinfo/', personal_views.UserInfoView.as_view(), name='personal-user_info'),

    # 工程信息

    url(r'^project/$', pmsys_views.ProjectView.as_view(), name='project'),
    url(r'^project/pro_over/$', pmsys_views.ProjectOverView.as_view(), name='pro_over'),
    url(r'^project/pro_over/data$', pmsys_views.ProjectOverGetdataView.as_view(), name='pro_over_data'),
    url(r'project/pro_over/detail$',pmsys_views.ProjectOverDetailView.as_view(), name='pro_over_detail'),
    url(r'^project/pro_list/$', pmsys_views.ProjectListView.as_view(), name='pro_list'),
    url(r'^project/pro_list/show/', include(('PMsys.urls', 'list-show'), namespace='list-show')),
    url(r'^project/new_pro/$', pmsys_views.ProjectNewView.as_view(), name='new_pro'),
    url(r'^project/work_log/$', pmsys_views.ProjectWorklogView.as_view(), name='work_log'),
    url(r'^project/facilities/$', pmsys_views.ProjectFacilities.as_view(), name='pro_facil'),
    url(r'^project/facilities/show/', include(('PMsys.urls', 'facil-show'), namespace='facil-show')),
]
