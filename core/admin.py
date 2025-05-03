from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

from core.models import Child, ChildAdmission, ChildDeath

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
    list_display = ['id', 'last_name', 'first_name', 'patronymic', 'date_of_birth']
    actions_on_top = True
    search_fields = ['first_name', 'last_name', 'patronymic']
    list_filter = ['date_of_birth']
    sortable_by = ('id', 'first_name', 'last_name', 'patronymic', 'date_of_birth')

@admin.register(ChildAdmission)
class ChildAdmissionAdmin(ModelAdmin):
    list_display = ['id', 'get_child_name', 'date_of_admission']

    @admin.display(description=_('child name'))
    def get_child_name(self, obj):
        return f'{obj.child.last_name} {obj.child.first_name} {obj.child.patronymic}'

@admin.register(ChildDeath)
class ChildDeathAdmin(ModelAdmin):
    list_display = ['id', 'get_child_name', 'date_of_death']

    @admin.display(description=_('child name'))
    def get_child_name(self, obj):
        return f'{obj.child.last_name} {obj.child.first_name} {obj.child.patronymic}'
    # def get_child_age(self, obj):
    #     age = datetime.now() - Child.date_of_birth