from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')  # 'Agg' backend for rendering to a file instead of displaying on screen
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

def handle_uploaded_file(f):
    upload_dir = 'uploaded_files'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            # Process the file with pandas
            df = pd.read_csv(file_path)
            # Store df to session or pass it to context
            request.session['csv_data'] = df.to_dict()
            return HttpResponseRedirect('/results/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def results(request):
    df = pd.DataFrame(request.session.get('csv_data'))
    head = df.head().to_html()
    description = df.describe().to_html()
    missing_values = df.isnull().sum().to_frame('missing_values').to_html()
    context = {
        'head': head,
        'description': description,
        'missing_values': missing_values,
    }
    return render(request, 'results.html', context)

def plot_to_html(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def visualize_data(request):
    csv_data = request.session.get('csv_data')
    if not csv_data:
        return render(request, 'visualization.html', {'plot': 'No data available'})

    df = pd.DataFrame(csv_data)

    fig, ax = plt.subplots()
    sns.histplot(df.select_dtypes(include=['number']).melt(value_name='value')['value'], ax=ax)
    plot_uri = plot_to_html(fig)
    
    context = {
        'plot': plot_uri,
    }
    return render(request, 'visualization.html', context)