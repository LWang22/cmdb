from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from app.views import *
import settings
urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':  settings.STATIC_ROOT}
    ),
    # Examples:
    # url(r'^$', 'CMDB.views.home', name='home'),
    # url(r'^CMDB/', include('CMDB.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin', include(admin.site.urls)),
    (r'^oprationfile/$',oprationfile),
    (r'^oprationfile_check',oprationfile_check),
    (r'^oprationfile_update',oprationfile_update),
    (r'^oprationfile_result',oprationfile_result),
    (r'^index',index),
    (r'^download$',download),
    (r'^download_result',download_result),
    (r'^$',login),
    (r'^login',login),
    (r'^logout/$',logout),
    (r'^idc/$',idc),
    (r'^addidc/$',addidc),
    (r'^idc/idc_delete/$',idc_delete),
    (r'^idc/idc_update/$',idc_update),
    (r'^mac/$',mac),
    (r'^addmac/$',addmac),
    (r'^mac/check_host',check_host),
    (r'^mac/mac_delete/$',mac_delete),
    (r'^mac/mac_edit/$',mac_edit),
    (r'^service',service_result),
    (r'^macresult/$',macresult),
    (r'^group$',group),
    (r'^group_result',group_result),
    (r'^group/group_delete',group_delete),
    (r'^group_manage/$',group_manage),
    (r'^group_manage/group_manage_delete',group_manage_delete),
    (r'addgroup_host/$',addgroup_host),
    (r'^file$',upfile),
    (r'^groupfile/$',groupfile),
    (r'^file_result',file_result),
    (r'del_upload_file',del_upload_file),
    (r'^groupfile_result',groupfile_result),
    (r'^command/$',command),
    (r'^command_group/$',command_group),
    (r'^command_group/check_result',check_result),
    (r'^command_group_result',command_group_result),
    (r'^command_result/$',command_result),
    (r'^job/$',job),
    (r'^asset/$',asset),
    (r'^asset_download/$',asset_download),
    (r'^asset_auto/$',asset_auto),
    (r'^asset_auto_result/$',asset_auto_result),
    (r'asset/asset_delete/$',asset_delete),
    (r'^authin/$',authin),
    (r'^user/$',user),
    (r'^adduser/$',adduser),
    (r'^user/user_delete/$',user_delete),
    (r'^user/user_forbidden/$',user_forbidden),
    (r'^user/user_start/$',user_start),
    (r'^userinfo',user_info),
    (r'^user_search',user_search),
    (r'^userpasswd',user_passwd),
    (r'^result_passwd',result_passwd),
    (r'log/list/offline/$',log_list_offline),
    (r'log/list/file/$',log_list_file),
    (r'log/list/cmd/$',log_list_cmd),
    (r'log/search/',log_search),
    (r'accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
)
