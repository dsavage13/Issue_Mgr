from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from .models import Issue, Status
from accounts.models import CustomUser, Role, Team

class IssueListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Issue  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        role = Role.objects.get(name="Product Owner")
        team_po = (
            CustomUser.objects
            .filter(team=user.team)
            .filter(role=role)
        )
        
        to_do = Status.objects.get(name="To-Do")
        context["to_do_list"] = (
            Issue.objects
            .filter(status=to_do)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        in_progress = Status.objects.get(name="In Progress")
        context["in_progress_list"] = (
            Issue.objects
            .filter(status=in_progress)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        completed = Status.objects.get(name="Completed")
        context["completed_list"] = (
            Issue.objects
            .filter(status=completed)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        return context

class IssueDetailView(UserPassesTestMixin, DetailView):
    model = Issue
    template_name = "issues/detail.html"
    
    def test_func(self):
        issue = self.get_object()
        if issue.status.name == "To-DO":
            return True
        elif issue.status.name == "In Progress":
            if (self.request.user.is_authenticated
                    and self.request.user == issue.reporter):
                return True
        elif (issue.status.name == "Completed"
                and self.request.user.is_authenticated):
            return True
        else:
            return False
    

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = "issues/new.html"
    fields = ["name", "summary", "description", "status"]
    
    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)
    
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    template_name = "issues/edit.html"
    fields = ["name", "summary", "description", "status"]
    
    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user
    
class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = "issues/delete.html"
    success_url = reverse_lazy("list")
    
    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user