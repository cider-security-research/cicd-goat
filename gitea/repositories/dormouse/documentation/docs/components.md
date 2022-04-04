# Components

Components are Python classes stored in `meld/components` either within your application folder or in the base directory
of your project.

Combined with a Jinja template, components enable you to create dynamic content without the need to write JavaScript.

The best way to start to understand how components work is to look at an example.

```py
# app/meld/components/counter.py

from flask_meld import Component


class Counter(Component):
    count = 0

    def add(self):
        self.count = int(self.count) + 1

    def subtract(self):
        self.count = int(self.count) - 1
```

The class above creates a property named `count` and defines the `add` and
`subtract` functions which will modify the `count` property. Combining the use of properties and functions in this way
allows you to customize the behavior of your components.

```html
{# app/meld/templates/counter.html #}
<div>
    <button meld:click="subtract">-</button>
    <input type="text" meld:model="count" readonly></input>
    <button meld:click="add">+</button>
</div>
```

The template includes two buttons and an input field. The buttons bind to the functions using `meld:click="add"`
and `meld:click:"subtract"` while the input binds to the
`count` property with `meld:model="count"`.

Components can be included in your Jinja templates using the `meld` tag referring to the name of your component.

```html
{# app/templates/index.html #}
<html>
<body>
    <h1>Counter Page</h1>
    {% meld 'counter' %}
</body>
</html>
```

## Properties

Components store model data for the class using `properties`.

```
class Counter(Component):
    count = 0
```

## Data Binding

You can bind a compenent property to an html element with `meld:model`. For instance, you can easily update a property
by binding it to an `input` element. When a user types text in the input field, the property is automatically updated in
the component.

```
class Person(Component):
    name = ""
---------------------------------------------
<div>
    <input meld:model="name" type="text">

    <h1>Hello {{ name }}</h1>
</div>
```

You can use `meld:model` on the following elements:

```
<input type="text">
<input type="radio">
<input type="checkbox">
<select>
<textarea>
```

## Custom events

You can use custom events to call a method in one component from a different component. Let's extend the `counter`
component above to listen for a `set-count` event, then build a new component that emits it. To listen for the event, we
just need to define a method on the component and use the `@flask_meld.listen` decorator. No changes are needed to the
template.

```py
# app/meld/components/counter.py

from flask_meld import Component, listen


class Counter(Component):
    count = 0

    def add(self):
        self.count = int(self.count) + 1

    def subtract(self):
        self.count = int(self.count) - 1

    @listen("set-count")
    def set_count(self, count):
        self.count = count
```

Now let's define a second component `SetCount` that will have a text box and a button. When a user clicks the button, we
want to emit an event with the value from the text box that can be picked up by the counter. To do this, we just
use `flask_meld.emit`.

```py
# app/meld/components/set_count.py

from flask_meld import Component, emit


class SetCount(Component):
    value = 0

    def set_count(self):
        emit("set-count", count=self.value)
```

Note that the `count` argument to `emit` will be passed as a keyword argument to the listening function. The template
for this component is pretty simple, we just need to define the text box and button and hook them to the Component.

```html
{# templates/meld/set_count.html #}
<div>
    <input type="text" meld:model="value"></input>
    <button meld:click="set_count">Set Count</button>
</div>
```

Finally, add `{% meld 'set_count' %}` to your page template and run the app!

Pretty simple right? You can use this to create very dynamic user interfaces using pure Python and HTML. We would love
to see what you have built using Meld so please share!
