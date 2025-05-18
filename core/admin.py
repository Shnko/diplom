from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin, TabularInline

from core.models import Child, ChildAdmission, ChildDeath, Employee, Employment, ChildReturned, ChildParent, ChildCare, \
    AdoptionParent, ChildAdopted, TransferToTreatment, TransferByCertainAge, ChildSickness, ChildRepatriation, \
    InternationalAdoption, Orphanage, Checkup, PlannedRates

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

class ChildDeathInline(TabularInline):
    model = ChildDeath

@admin.register(Child)
class ChildAdmin(ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic', 'date_of_birth', 'disability_category', 'death_date']
    actions_on_top = True
    search_fields = ['first_name', 'last_name', 'patronymic']
    list_filter = ['date_of_birth', 'disability_category', 'childdeath__date_of_death']
    sortable_by = ('first_name', 'last_name', 'patronymic', 'date_of_birth')
    inlines = [ChildDeathInline]

    @admin.display(description="Дата смерти")
    def death_date(self, obj):
        return obj.childdeath.date_of_death

@admin.register(ChildAdmission)
class ChildAdmissionAdmin(ModelAdmin):
    list_display = ['get_child_name', 'date_of_admission']

    @admin.display(description='ребёнок')
    def get_child_name(self, obj):
        return f'{obj.child.last_name} {obj.child.first_name} {obj.child.patronymic}'


@admin.register(ChildDeath)
class ChildDeathAdmin(ModelAdmin):
    list_display = ['get_child_name', 'date_of_death', 'get_child_death_age']

    @admin.display(description=_('child name'))
    def get_child_name(self, obj):
        return f'{obj.child.last_name} {obj.child.first_name} {obj.child.patronymic}'

    @admin.display(description=_('child death age'))
    def get_child_death_age(self, obj):
        age = obj.date_of_death.year - obj.child.date_of_birth.year - (
                (obj.date_of_death.month, obj.date_of_death.day) < (
        obj.child.date_of_birth.month, obj.child.date_of_birth.day))
        return age


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ['last_name', 'first_name', 'patronymic']
    sortable_by = ('last_name', 'first_name', 'patronymic')


@admin.register(Employment)
class EmploymentAdmin(ModelAdmin):
    list_display = ['get_employee_name', 'report_category', 'rate', 'start_date_of_employment', 'end_date_of_employment']
    sortable_by = ('rate', 'start_date_of_employment', 'end_date_of_employment' )


    @admin.display(description='ФИО сотрудника')
    def get_employee_name(self, obj):
        return f'{obj.employee.last_name} {obj.employee.first_name} {obj.employee.patronymic}'


class ChildParentInline(TabularInline):
    model = ChildParent

@admin.register(ChildReturned)
class ChildReturnedAdmin(ModelAdmin):
    list_display = ['child', 'date_of_adoption']
    inlines = [ChildParentInline]

@admin.register(ChildCare)
class ChildCareAdmin(ModelAdmin):
    list_display = ['child', 'date_of_adoption', 'care_type']

class AdoptionParentInline(TabularInline):
    model = AdoptionParent

@admin.register(ChildAdopted)
class ChildReturnedAdmin(ModelAdmin):
    list_display = ['child', 'date_of_adoption']
    inlines = [AdoptionParentInline]

@admin.register(ChildRepatriation)
class ChildRepatriationAdmin(ModelAdmin):
    list_display = ['child', 'date_of_repatriation']

@admin.register(TransferToTreatment)
class TransferToTreatmentAdmin(ModelAdmin):
    list_display = ['child', 'date_of_transfer', 'organization']

@admin.register(TransferByCertainAge)
class TransferByCertainAgeAdmin(ModelAdmin):
    list_display = ['child', 'date_of_transfer', 'type']

@admin.register(InternationalAdoption)
class InternationalAdoptionAdmin(ModelAdmin):
    list_display = ['child', 'date_of_adoption']

@admin.register(ChildSickness)
class ChildSicknessAdmin(ModelAdmin):
    list_display = ['child', 'icd_code', 'date_of_diagnosis']

@admin.register(Checkup)
class CheckupAdmin(ModelAdmin):
    list_display = ['child', 'date_of_checkup', 'diagnosis']


@admin.register(Orphanage)
class OrphanageAdmin(ModelAdmin):
    list_display = ['location_type', 'count_of_seats']

@admin.register(PlannedRates)
class PlannedRatesAdmin(ModelAdmin):
    list_display = ['category', 'count']