from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def first_view(request):
    return render(request, 'module1/first_view.html', {})

def uimage(request):
    form_class =UploadImageForm
    form = form_class(request.POST or None)

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'module1/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'module1/uimage.html', {'form': form})