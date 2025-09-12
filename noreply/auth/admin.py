from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe


from auth.models import Client


class ReadOnlyPasswordWidget(forms.Widget):
    template_name = 'admin/readonly_password_with_copy.html'

    def render(self, name, value, attrs=None, renderer=None):
        html = f'''
        <input type="password" value="{value or ''}" readonly id="id_{name}" style="width: 70%;">
        <button type="button" onclick="navigator.clipboard.writeText(document.getElementById('id_{name}').value)">Скопировать</button>
        '''
        return mark_safe(html)


class ClientAdminForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'client_secret': ReadOnlyPasswordWidget(),
        }


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # form = ClientAdminForm
    list_display = (
        "client_id",
        "comment",
        "is_active",
    )
    search_fields = (
        "client_id",
        "comment",
    )
    list_filter = (
        "is_active",
    )
    readonly_fields = (
        "client_secret_display",
    )
    fields = (
        "client_id",
        "client_secret_display",
        "comment",
        "is_active",
    )

    def client_secret_display(self, obj):
        return mark_safe(f'''
            <input type="password" value="{obj.client_secret}" readonly style="width:70%;">
            <button type="button" onclick="navigator.clipboard.writeText('{obj.client_secret}')">Скопировать</button>
        ''')
    client_secret_display.short_description = "Client Secret"
