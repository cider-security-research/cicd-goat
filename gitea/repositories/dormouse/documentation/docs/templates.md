## Templates

Here is an example for counter:

```html
{# app/meld/templates/counter.html #}
<div>
    <button meld:click="subtract">-</button>
    <input type="text" meld:model="count" readonly></input>
    <button meld:click="add">+</button>
</div>
```
Let's take a look at that template file in more detail.

The buttons use `meld:click` to call the `add` or `subtract` function of the
Counter component.
The input uses `meld:model` to bind the input to the `count` property on the
Counter component.  

Note, to avoid errors, when adding a comment to a component template use the
Jinja syntax, `{# comment here #}`, rather than the HTML syntax.

### Pass data to a component

You can, of course, pass data to your meld component. Meld is passing **kwargs 
to the render function of the *meld* templatetag, so you can pass any number of 
named arguments. The component is found based on the first parameter, aka name 
of the component, and any number of data passed afterwards. 

Providing a very basic component as an example to display a greeting message using
the passed value for the keyword "name" in the corresponding template.

```html
{# app/meld/templates/greeter.html #}
<div>
    Hello, {{name or "Nobody"}}
</div>
```
which can be invoked using:

```html
{# app/templates/base.html #}
{% meld 'greeter', name="John Doe" %}
```

### Use passed values in a component

You may want to have the ability to access a passed in value within a component.

Using the same example as above, pass in a `name` to the component.

```html
{# app/templates/base.html #}
{% meld 'greeter', name="John Doe" %}
```

Access the `name` attribute within the component with `self.name`.

```py
class Greeter(Component):

    def get_name(self):
        return self.name
```

```html
<div>
    Hello, {{name}}
</div>
```

### Modifiers

Use modifiers to change how Meld handles network requests.

* `lazy`: `<input meld:model.lazy="search">` To prevent updates from happening on every input, you can append a lazy modifier to the end of meld:model. That will only update the component when a blur event happens.

* `debounce`: `<input meld:model.debounce-500="search">` Delay network requests for an amount of time after a keypress. Used to increase performance and sync when the user has paused typing for an amount of time. `debounce-250` will wait 250ms before it syncs with the server. The default is 150ms.

* `defer`: `<input meld:model.defer="search">` Pass the search field with the next network request. Used to improve performance when realtime databinding is not necessary.

* `prevent`: Use to prevent a default action. The following example uses `defer` to delay sending a network request until the form is submitted. An idea of how this can be used: instead of adding a keydown event listener to the input field to capture the press of the `enter` key, a form with `meld:submit.prevent="search"` can be used to to invoke a component's `search` function instead of the default form handler on form submission.

```html
<form meld:submit.prevent="search">
    <input meld:model.defer="search_text" type="text" name="name" id="name" placeholder="Search for name">
    <button meld:click="search">Search</button>

    <!-- To get the same functionality without using meld:submit.prevent="search" you
    would need to add an event listener for the enter key 
    <input meld:model.defer="search_text" meld:keydown.Enter="search" type="text" name="name" id="name" placeholder="Search for name">
    -->
</form>
```
