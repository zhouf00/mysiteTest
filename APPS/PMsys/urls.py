from django.conf.urls import url

from APPS.PMsys import views_list, views_pro

urlpatterns = [
    # 设备
    url(r'^dev/$', views_list.ListDevView.as_view(), name='dev'),
    url(r'^dev/detail/$', views_list.ListDevDetailView.as_view(), name='dev_detail'),

    # 服务器
    url(r'^server/$', views_list.ListServerView.as_view(), name='server'),

    # 库存
    url(r'^deli/$', views_list.ListDeliView.as_view(), name='deli'),

    # 联系人
    url(r'^person/$', views_list.ListPersonView.as_view(), name='person'),

    # 项目相关
    url(r'^related/$', views_list.ListRelatedView.as_view(), name='related'),
    url(r'^related/file_delete/$', views_pro.FileDeleteView.as_view(), name='file_delete'),
    url(r'^related/procedure/$', views_pro.ProcedureView.as_view(), name='procedure'),
    url(r'^related/stay/$', views_pro.StayView.as_view(), name='stay'),
    url(r'^related/trip/$', views_pro.TripView.as_view(), name='trip'),
    url(r'^related/explain/$', views_pro.ExplainView.as_view(), name='explain'),

    # 资源信息
    url(r'^manu_info/$', views_list.FacilManuView.as_view(), name='manu_info'),
    url(r'^dev_info/$', views_list.FacilDevView.as_view(), name='dev_info'),
    url(r'^col_info/$', views_list.FacilColView.as_view(), name='col_info'),
    url(r'^sensor_info/$', views_list.FacilSensorView.as_view(), name='sensor_info'),
    url(r'^passwd_info/$', views_list.FacilPasswdView.as_view(), name='passwd_info'),
]