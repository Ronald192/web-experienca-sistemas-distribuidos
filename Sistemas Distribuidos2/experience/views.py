from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from .models import Experience
from .forms import ExperienceForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q


# Create your views here.


class StaffRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class ExperienceListView(ListView):
    model = Experience

    def get_context_data(self, **kwargs):
        context = super(ExperienceListView, self).get_context_data(**kwargs)
        context['form'] = ExperienceForm()
        return context

    def get_queryset(self):
        queryset = self.request.GET.get("buscar")
        context = super(ExperienceListView, self).get_queryset()
        if queryset:
            return context.filter(
                Q(title__icontains=queryset) |
                Q(content__icontains=queryset)
            ).distinct()
        return context


class ExperienceDetailView(DetailView):
    model = Experience


@method_decorator(login_required, name='dispatch')
class ExperienceCreate(CreateView):
    model = Experience
    form_class = ExperienceForm
    success_url = reverse_lazy('experience:experiences')

    def form_valid(self, form):
        self.form_usuario = form.save(commit=False)
        self.form_usuario.user = self.request.user
        self.form_usuario.save()
        return super(ExperienceCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ExperienceUpdate(UpdateView):
    model = Experience
    fields = ['title', 'content', 'image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('experience:update', args=[self.object.id]) + '?ok'


@method_decorator(login_required, name='dispatch')
class ExperienceDelete(DeleteView):
    model = Experience
    success_url = reverse_lazy('experience:experiences')  # una vez creado regresa


class ExperienceListUser(ListView):
    model = Experience

    def get_queryset(self):
        expUser = super(ExperienceListUser, self).get_queryset()
        return expUser.filter(user=self.request.user)


def experience_detail(request, experience_id, experience_slug):
    experience = get_object_or_404(Experience, id=experience_id)
    is_liked = False
    if experience.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'experience': experience,
        'is_liked': is_liked,
        'total_likes': experience.total_likes(),
    }
    return render(request, 'experience/experience_detail.html', context)


@login_required
def like_experience(request):
    experience = get_object_or_404(Experience, id=request.POST.get('experience_id'))
    is_liked = False
    if experience.likes.filter(id=request.user.id).exists():
        experience.likes.remove(request.user)
        is_liked = False
    else:
        experience.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(reverse('experience:experiences'))
