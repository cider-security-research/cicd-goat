# Introduction
Flask-Meld is a library to provide server rendered templates over websockets for Flask 
applications.  Meld gives you tools to dynamic frontend experiences without the need 
to write any Javascript.

Instead of syncing data between the client and the server via HTTP requests,
Meld uses a persistent WebSocket connection. When data is updated on the
client, the data is sent to the server where the Component renders the new HTML
and sends it back to the client. 

The page HTML is written using Jinja templates, just as you would with Flask. 
Meld utilizes Morphdom to intelligently update the DOM so only elements on
the page that have been changed will be updated. This gives a fast, smooth,
reactive experience for the user with server-side rendered templates.


## Installation

Install Flask-Meld in your virtual environment. 

```bash
pip install flask-meld
```

Meld uses the [Application Factory](https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/) 
approach to structuring an application and gives the user a CLI tool to get
their project setup quickly by automating much of the boilerplate code for
you.

## Updating Flask-Meld

```bash
pip install --upgrade flask-meld
```
