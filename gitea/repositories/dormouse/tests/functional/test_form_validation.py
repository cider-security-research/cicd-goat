from flask_meld.component import Component
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class RegistrationForm(Form):
    email = StringField(("Email"), validators=[DataRequired(), Email()])
    password = PasswordField(("Password"), validators=[DataRequired()])
    password_confirm = PasswordField(
        ("Confirm Password"), validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Submit")


class FormComponent(Component):
    form = RegistrationForm()


def test_component_has_form():
    component = FormComponent()
    assert component._form


def test_form_is_part_of_a_meld_component():
    component = FormComponent()
    assert "meld:model" in component._form.email.__call__()


def test_set_form_data():
    form_data = {"email": "test@test.com"}
    component = FormComponent()
    component._set_field_data("email", form_data["email"])
    assert component._form.email.data == "test@test.com"


def test_component_init_sets_form_data():
    form_data = {"email": "test@test.com"}
    component = FormComponent(**form_data)
    assert component._form.email.data == "test@test.com"


def test_form_validate_is_true():
    form_data = {
        "email": "test@test.com",
        "password": "somepass",
        "password_confirm": "somepass",
    }
    component = FormComponent(**form_data)
    assert component.validate()


def test_form_validate_has_errors_if_failed():
    form_data = {
        "email": "test@test.com",
        "password": "somepass",
        "password_confirm": "nomatch",
    }
    component = FormComponent(**form_data)
    assert not component.validate()
    assert component._form.password_confirm.errors


def test_component_has_errors_if_validation_fails():
    form_data = {"email": "", "password": "somepass", "password_confirm": "nomatch"}
    component = FormComponent(**form_data)
    component.validate()
    assert len(component.errors) == 2


def test_form_fields_are_attributes():
    component = FormComponent(RegistrationForm)
    assert getattr(component, "email") is None


def test_form_validates():
    component = FormComponent(RegistrationForm)
    form = component._form
    setattr(form["email"], "data", "help")
    assert getattr(component, "email") is None


def test_form_submit_model_is_not_set():
    component = FormComponent()
    assert "meld:model" not in component._form.submit.__call__()
