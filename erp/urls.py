from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^login/$', 'erp.views.login_service', name='login_service'),
    url(r'^logout/$', 'erp.views.logout_service', name='logout_service'),
    url(r'^list_purchase_orders/$', 'erp.views.list_purchase_orders', name='list_purchase_orders'),
    url(r'^update_status_purchase_order/$', 'erp.views.update_status_purchase_order', name='update_status_purchase_order'),
)
