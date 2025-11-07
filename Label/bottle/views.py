from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import FSSAIEntry
from .forms import FSSAIEntryForm, ReviewForm
from django.contrib import messages


def landing(request):
    """Landing page that explains the project and points to the upload and gallery."""
    features = [
        'Upload your FSSAI authorization and logo',
        'Generate simple label design ideas automatically',
        'Preview and collect reviews from users',
        'Download certificate and iterate on branding',
    ]
    return render(request, 'bottle/landing.html', {'features': features})


def home(request):
    """Show list of uploaded FSSAI entries and a link to upload new."""
    entries = FSSAIEntry.objects.order_by('-submitted_at')
    return render(request, 'bottle/home.html', {'entries': entries})


def upload_entry(request):
    """Upload a new FSSAI certificate and logo."""
    if request.method == 'POST':
        form = FSSAIEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save()
            messages.success(request, 'Entry submitted — preview your label below.')
            return redirect(reverse('bottle:detail', args=[entry.id]))
    else:
        form = FSSAIEntryForm()
    return render(request, 'bottle/upload.html', {'form': form})


def detail(request, pk):
    """Detail page: show uploaded data, logo, reviews, and generate simple label ideas."""
    entry = get_object_or_404(FSSAIEntry, pk=pk)

    # handle review submission
    if request.method == 'POST':
        rform = ReviewForm(request.POST)
        if rform.is_valid():
            rev = rform.save(commit=False)
            rev.entry = entry
            rev.save()
            messages.success(request, 'Thank you for your review!')
            return redirect(reverse('bottle:detail', args=[entry.id]))
    else:
        rform = ReviewForm()

    # Simple label ideas generator (deterministic small samples)
    logo_url = entry.logo.url if entry.logo else ''
    ideas = [
        "Minimalist: white background, small centered logo, bold product name under logo.",
        "Premium: dark matte wrap, gold foil text for brand, logo embossed top-left.",
        "Eco: kraft-paper texture background, logo in green, '100% natural' badge.",
    ]

    return render(request, 'bottle/detail.html', {
        'entry': entry,
        'review_form': rform,
        'ideas': ideas,
        'logo_url': logo_url,
    })

def upload_fssai(request):
    if request.method == 'POST':
        form = FSSAIEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save()
            return redirect('label_preview', entry.id)
    else:
        form = FSSAIEntryForm()
    return render(request, 'fssai_app/upload_form.html', {'form': form})

def label_preview(request, entry_id):
    entry = get_object_or_404(FSSAIEntry, pk=entry_id)
    # Mock "idea generation" – in real project, could use AI
    ideas = [
        "A sleek transparent bottle with your logo on a blue label.",
        "Eco-friendly paper label with minimalist FSSAI info.",
        "Matte finish with embossed logo and silver FSSAI tag."
    ]
    return render(request, 'fssai_app/label_preview.html', {'entry': entry, 'ideas': ideas})

def reviews(request, entry_id):
    entry = get_object_or_404(FSSAIEntry, pk=entry_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.entry = entry
            review.save()
            return redirect('reviews', entry_id)
    else:
        form = ReviewForm()
    return render(request, 'fssai_app/reviews.html', {'entry': entry, 'form': form, 'reviews': entry.reviews.all()})
