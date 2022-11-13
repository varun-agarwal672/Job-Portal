from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "JobWork"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', home.about,name='About'),
    path('contact', home.contact,name='Contact'),
    path('intro', home.intro,name='Intro'),
    path('search', SearchView.as_view(), name='searh'),
    path('employer/dashboard', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),
        path('delete/<int:job_id>/', delete_view, name='employer-dashboard-delete'),

    ])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)