from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.shortcuts import render, get_object_or_404, redirect

from JobWork.decorators import user_is_employer
from JobWork.forms import CreateJobForm
from JobWork.models import Job, Applicant

class DashboardView(ListView):
###view for company dashboard
    model = Job
    template_name = 'jobs/employer/dashboard.html'
    context_object_name = 'jobs'

    @method_decorator(login_required(login_url=reverse_lazy('AccountsUser:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)


class ApplicantPerJobView(ListView):
###view to show applicants per job
    model = Applicant
    template_name = 'jobs/employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 1

    @method_decorator(login_required(login_url=reverse_lazy('AccountsUser:login')))
    @method_decorator(user_is_employer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return Applicant.objects.filter(job_id=self.kwargs['job_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = Job.objects.get(id=self.kwargs['job_id'])
        return context


class JobCreateView(CreateView):
###view to create job post
    form_class = CreateJobForm
    template_name = 'jobs/create.html'
    success_url = reverse_lazy('JobWork:employer-dashboard')

    @method_decorator(login_required(login_url=reverse_lazy('AccountsUser:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('AccountsUser:login')
        if self.request.user.is_authenticated and self.request.user.role != 'employer':
            return reverse_lazy('AccountsUser:login')
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None   
        form = self.get_form()
        if form.is_valid():
            messages.info(request, 'Job Created Successfully!!!')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def delete_view(request, job_id):
###to delete job post
    context ={}
    obj = get_object_or_404(Job, id = job_id)
    if request.method =="POST":
        obj.delete()
        messages.success(request, 'Your Job Post was successfully deleted!')
        return redirect('JobWork:employer-dashboard')
    return render(request, "jobs/employer/delete.html", context)