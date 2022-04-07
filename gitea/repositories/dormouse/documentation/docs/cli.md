# Commands

You've already learned how to use the command-line interface to do some things.
This chapter documents all the available commands.

To get help from the command-line, simply call `meld` to see the complete list of commands,
then `--help` combined with any of those can give you more information.

## new 

### meld new project
This command will help you kickstart your new Meld project by creating
a directory structure suitable for most projects.

```bash
meld new project meld-example
```

will create a folder as follows:

```text
meld-example
├── app
│   └── __init__.py
│   └── meld
│   └── static
│   └── templates
│   └── wsgi.py
├── tests
├── config.py
└── requirements.txt
```

### meld new component
This command will create a template and a component file with the given name.

```bash
meld new component meld_component
```

```text
meld-example
├── app
│   └── meld
│       └── components
│           └── meld_component.py
│       └── templates
│           └── meld_component.html
```
