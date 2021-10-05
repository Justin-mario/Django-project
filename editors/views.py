from django.shortcuts import render, redirect
from .form import EditorForm
from .models import Editor


def get_an_editor(request, pk):
    try:
        editor = Editor.objects.get(id=pk)
        return render(request, "get_an_editor.html", {"editor": editor})
    except Editor.DoesNotExist:
        context = {
            "error": "This Editor does not exist."
        }
        return render(request, "error_form.html", context)


def create_editor(request):
    form = EditorForm()
    if request.method == "POST":
        form = EditorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("editor_index")
        else:
            context = {
                "error": form.errors
            }
            return render(request, "error_form.html", context)
    else:
        return render(request, "editor_form.html", {"form": form})



def get_all_editors(request):
    editors = Editor.objects.all()
    context = {
        "editors": editors
    }
    return render(request, "editor.html", context)
