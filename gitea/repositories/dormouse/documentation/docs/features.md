# Features
## Loading States
Sometimes a component might take a little bit of time to finish an action, for example,
making a request to an external API. In these cases it can be helpful to give some
feedback to the user that the request is still processing. Enter loading states.

### Show/Hide Elements During Loading States

```html
<div>
    <button meld:click="sponsor">Support open-source software</button>

    <div meld:loading>
        Processing Github request...
    </div>
</div>
```

When the "sponsor" button is clicked, the "Processing Github request..." will be
displayed. Once the action has completed the message will disappear.

You can also "hide" an element during a loading state using the `.remove` modifier.

```html
<div>
    <button meld:click="sponsor">Support open-source software</button>

    <div meld:loading.remove>
        Hide this div while loading
    </div>
</div>
```

### Targeting specific actions
If your component has multiple actions you may want to show loading states
only for specific actions.

```html
<div>
  <button meld:click="add" id="addAction">Add</button>
  <button meld:click="remove" id="removeAction">Remove</button>

  <div meld:loading meld:target="addAction">Adding item</div>
  <div meld:loading meld:target="removeAction">Removing item</div>
</div>
```

An element’s `meld:key` can also be targeted.

```html
<div>
  <button meld:click="add" meld:key="addKey">Add</button>
  <button meld:click="remove" meld:key="removeKey">remove</button>

  <div meld:loading meld:target="addKey">Adding item</div>
  <div meld:loading meld:target="removeKey">Removing item</div>
</div>
```

### Set set class of element during loading state

Add or remove classes from an element during loading states by adding the `.class` modifier

```html
<div>
  <button meld:click="update" meld:loading.class="opacity-50">Update</button>
</div>
```

Classes can also be removed durning a loading state. Below if the update button is
pressed the `bg-purple` class will be removed from the input during the loading state and 
is added back when the loading state completes.

```html
<div>
  <button class="bg-purple" meld:loading.class.remove="bg-purple" meld:click="update">Update</button>
</div>
```

### Set attribute of element during loading state

An element can set an attribute during a loading state. A great use case for setting an
attribute is to add the "disabled" attribute to elements when an action is triggered.

```html
<div>
  <button meld:click="update" meld:loading.attr="disabled">Update</button>
</div>
```




## Form Validation

A big part of creating web applications is using forms. Flask-Meld integrates with
Flask-WTF to give you real-time form validation without writing any Javascript.

### Integration with WTForms for validation

Define your form with Flask-WTF

```py
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
```

### Create your template

Use WTForm helpers to create your form in your HTML template. 

```html
<!-- app/meld/templates/register.html -->
<div>
    <form method="POST">
        <div>
            {{ form.email.label }}
            {{ form.email }}
            <span> {{ errors.password | first }} </span>
        </div>

        <div>
            {{ form.password.label }}
            {{ form.password }}
            <span> {{ errors.password | first }} </span>
        </div>
        <div>
            {{ form.password_confirm.label }}
            {{ form.password_confirm }}
            <span> {{ errors.password_confirm | first }} </span>
        </div>
        <div>
            {{ form.submit }}
        </div>
    </form>
</div>
```

Using the WTForm helpers saves you some typing. 
Alternatively, you can define your HTML form without using the helpers. 
For example, to make a field use
`<input id="email" meld:model="email" name="email" required="" type="text" value="">`
Make sure that `meld:model="name_of_field"` exists on each field.

### Define the form in the component

```py
# app/meld/components/register.py
from flask_meld import Component
from forms import RegistrationForm


class Register(Component):
    form = RegistrationForm()
```

## Realtime form validation

To make your form validate as a user types use the `updated` function. This will provide
the form field and allow you to validate on the fly. Simply call `validate` on the
field.

```py
# meld/components/register.py
from flask_meld import Component
from forms import RegistrationForm


class Register(Component):
    form = RegistrationForm()

    def updated(self, field):
        self.validate(field)
```

### Routes

You can create a custom method on your component (such as a `save` method) to handle
submissions or you can use your regular old Flask routes. 

```py
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # do anything you need with your form data...
        return redirect(url_for("index"))
    return render_template("register_page.html")
```
