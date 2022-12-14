# -*- coding: utf-8 -*-
"""
Formularios para la app main
"""
# Standard Libraries
import re
from datetime import date

# Django Libraries
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import (
    EmailInput,
    ModelForm,
    NumberInput,
    PasswordInput,
    Select,
    TextInput,
)
from django.utils.translation import gettext_lazy as _

# Thirdparty Libraries
from bootstrap_datepicker_plus.widgets import DatePickerInput

# Local Folders Libraries
from .models import UserCustom


class MyDatePickerInput(DatePickerInput):
    template_name = "datepicker_plus/date-picker.html"


class PerfilForm(ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """

    class Meta:
        model = UserCustom
        fields = (
            "first_name",
            "last_name",
            "email_secundario",
            "telefono",
            "celular",
            "fecha_nacimiento",
            "sex",
        )
        widgets = {
            "first_name": TextInput(attrs={"class": "form-control"}),
            "otros_nombres": TextInput(attrs={"class": "form-control"}),
            "last_name": TextInput(attrs={"class": "form-control"}),
            "otros_apellidos": TextInput(attrs={"class": "form-control"}),
            "email_secundario": TextInput(attrs={"class": "form-control"}),
            "letra_cedula_identidad": Select(attrs={"class": "form-control"}),
            "cedula_identidad": NumberInput(attrs={"class": "form-control"}),
            "telefono": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+58 (___) ___-__-__",
                    "data-mask": "+58 (000) 000-00-00",
                }
            ),
            "celular": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+58 (___) ___-__-__",
                    "data-mask": "+58 (000) 000-00-00",
                }
            ),
            "fecha_nacimiento": MyDatePickerInput(
                options={
                    "format": "DD/MM/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                },
                attrs={
                    "class": "form-control",
                    "placeholder": "__/__/____",
                    "data-mask": "00/00/0000",
                },
            ),
            "sex": Select(attrs={"class": "form-control select2-control"}),
        }

    def clean(self):
        super().clean()
        # fecha_nacimiento = self.cleaned_data.get("fecha_nacimiento")
        # cedula_identidad = str(self.cleaned_data.get('cedula_identidad'))

        # Validamos que la persona tiene menos de diez y ocho(18) a??os
        # fecha_actual = date.today()
        # print('Fecha: %s' % fecha_nacimiento)
        # edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        # if edad < 18:
        #     self.add_error('fecha_nacimiento', "Disculpe, debe ser mayor de edad para poder registrarse en\
        #                      el sistema")

        #  Si la persona tiene nueve(9) a??os o mas, validamos la c??dula tenga la forma 99999999
        # patron_mayor_edad = re.compile('^\d{5,8}$')
        # if edad >= 9 and patron_mayor_edad.match(cedula_identidad) is None:
        #     self.add_error('cedula_identidad', "La c??dula de identidad de las personas mayores o iguales\
        #                      a nueve (9) a??os de edad, debe comenzar con V ?? E, seguido de hasta ocho (8) \
        #                      digitos correspondientes al n??mero de la c??dula")

    def clean_telefono(self):
        """
        Validamos que el tel??fono cumpla con el formato
        """
        diccionario_limpio = self.cleaned_data
        telefono = diccionario_limpio.get("telefono")
        patron = re.compile(r"^\+58\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$")
        if telefono:
            if patron.match(telefono) is None:
                raise forms.ValidationError(
                    "El n??mero de tel??fono local debe\
                                                cumplir con la forma +58 (999)\
                                                999-99-99"
                )
        return telefono

    def clean_celular(self):
        """
        Validamos que el celular cumpla con el formato
        """
        diccionario_limpio = self.cleaned_data
        celular = diccionario_limpio.get("celular")
        patron = re.compile(r"^\+58\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$")
        if celular:
            if patron.match(celular) is None:
                raise forms.ValidationError(
                    "El n??mero de tel??fono celular debe cumplir con la forma +58 (999) 999-99-99"
                )
        return celular


class PersonaChangeForm(UserChangeForm):
    """Para algo sera esto
    """

    class Meta(UserChangeForm.Meta):
        model = UserCustom
        fields = (
            "username",
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined",
            "first_name",
            "last_name",
        )


# ==================================================================================== #
class PasswordRecoveryForm(ModelForm):
    """Para enviar el correo de recuperacion de la cuenta
    """

    class Meta:
        model = UserCustom
        fields = ("email",)
        widgets = {
            "email": EmailInput(
                attrs={"class": "form-control", "placeholder": _("Email")}
            ),
        }


# ==================================================================================== #
class PasswordSetForm(forms.Form):
    """Para enviar el correo de recuperacion de la cuenta
    """

    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": _("Password")}
        )
    )
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": _("Retype password")}
        )
    )

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print("entre8888")
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))


class PersonaCreationForm(UserCreationForm):
    """Con esta clase de formulario se renderiza la plantilla de registro de
    ususarios
    """

    class Meta(UserCreationForm.Meta):
        model = UserCustom
        fields = (
            "username",
            # 'first_name',
            # 'last_name',
            "email",
        )
        widgets = {
            "username": TextInput(
                attrs={"class": "form-control", "placeholder": _("User")}
            ),
            # 'first_name': TextInput(
            #     attrs={'class': 'form-control', 'placeholder': _('First name')}
            # ),
            # 'last_name': TextInput(
            #     attrs={'class': 'form-control', 'placeholder': _('Surname')}
            # ),
            "email": EmailInput(
                attrs={"class": "form-control", "placeholder": _("Email")}
            ),
        }


class AvatarForm(ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
    """

    class Meta:
        model = UserCustom
        fields = ("avatar",)
