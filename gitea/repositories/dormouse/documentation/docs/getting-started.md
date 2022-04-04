# Getting Started

## Project setup

### Create a new project
First, let's create our new project, let's call it `meld-example`:

```bash
meld new project meld-example
```

This will create the `meld-example` directory with the following content:

```text
meld-example
├── app
│   └── __init__.py
│   └── meld
│   │   └── components
│   │   └── templates
│   └── static
│   └── templates
│   └── wsgi.py
├── tests
├── config.py
└── requirements.txt
```

### Use Meld in an existing project
Meld can be added to an existing application by completing the following steps:

- Import Meld into your application with `from flask_meld import Meld`
- Initialize the Meld extension. 
    - If you are using the Application Factory pattern, this means adding 
    `meld = Meld()` and `meld.init_app(app)` in your `__init__.py` file.
    - If using a single `app.py` instead of using the `init_app` you can simply
      initialize Meld by using `Meld(app)
    - Add `{% meld_scripts %}` in the `body` of your base HTML template
    - Use the socketio server to serve your application with `socketio.run(app)` or to 
    specify a port and debugging use `socketio.run(app=app, port=5000, debug=True)`

