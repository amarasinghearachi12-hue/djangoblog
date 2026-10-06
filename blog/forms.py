
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "cover_image", "tags", "status"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "content": forms.Textarea(
                attrs={
                    "rows": 8,
                    "class": "form-control"
                }
            ),
            "cover_image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
            "tags": forms.CheckboxSelectMultiple(),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title.strip()) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 characters long."
            )

        return title

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title and content:
            if title.strip().lower() in content.strip().lower()[:50]:
                raise forms.ValidationError(
                    "Don't repeat the title verbatim at the start of the content."
                )

        return cleaned_data