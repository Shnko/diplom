from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

from core.models import Child

admin.site.unregister(User)
admin.site.unregister(Group)

# Fix for 'unfold'-themed user and group models
# See https://unfoldadmin.com/docs/installation/auth/
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


# Fix for 'unfold'-themed user and group models
# See https://unfoldadmin.com/docs/installation/auth/
@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(Child)
class ChildAdmin(ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'patronymic', 'date_of_birth']
    actions_on_top = True
    search_fields = ['first_name', 'last_name', 'patronymic']
    list_filter = ['date_of_birth']
    sortable_by = ('id', 'first_name', 'last_name', 'patronymic', 'date_of_birth')
