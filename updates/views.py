from django.views.generic import ListView, DetailView
from .models import Update
from django.shortcuts import render, get_object_or_404

class UpdateListView(ListView):
    model = Update
    template_name = 'updates/update_list.html'
    context_object_name = 'updates'
    paginate_by = 5  # optional: paginate 5 posts per page

class UpdateDetailView(DetailView):
    model = Update
    template_name = 'updates/update_detail.html'
    context_object_name = 'update'


def update_list(request):
    updates = Update.objects.filter(is_published=True)
    return render(request, 'updates/update_list.html', {'updates': updates})


def update_detail(request, slug):
    update = get_object_or_404(Update, slug=slug, is_published=True)

    next_post = Update.objects.filter(
        created_at__gt=update.created_at,
        is_published=True
    ).order_by('created_at').first()

    prev_post = Update.objects.filter(
        created_at__lt=update.created_at,
        is_published=True
    ).order_by('-created_at').first()

    return render(request, 'updates/update_detail.html', {
        'update': update,
        'next_post': next_post,
        'prev_post': prev_post,
    })
