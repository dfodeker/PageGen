# Welcome to the PageGen 
This readme serves as documentation for the  Custom Shopify app that creates a page in a Shopify store.
This going to serve as a general information page for the Python and next.js apps and will cover the installation of the python application. 

It works by calling the Shopify `Creates a page` endpoint, the update page api.


Further information can be found at [Create page Shopify api](https://shopify.dev/api/admin-rest/2022-07/resources/page).

There are two versions of this app 
* A version of the app built with `Python and Flask` 
* A version of the app built with `Next.js`

The next.js version does not have the functionality to check it a page exists and can only create pages
The Python & Flask version takes it further by adding extra functionality: checking if a page already exists and updating it with the appropriate content. 

##  Getting Started
*Step 1. Clone the code into a fresh folder*
```
$ git clone https://github.com/dfodeker/PageGen.git 
$ cd PageGen
```
*Step 2. Create a Virtual Environment and install Dependencies.*
Create a new Virtual Environment for the project and activate it. If you don’t have the ### virtualenv
 command yet, you can find installation  [instructions here](https://virtualenv.readthedocs.io/en/latest/) . Learn more about  [Virtual Environments](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments) .
```
$ virtualenv venv
$ source venv/bin/activate
```
Next, we need to install the project dependencies, which are listed in ### requirements.txt
.
` (venv) $ pip install -r requirements.txt`

* git clone https://github.com/dfodeker/PageGen.git 

* change the url of the store to reflect yours shopify store

* Run pip3 install -r requirements.txt 

* Edit the Index.html to reflect what you’d like to be displayed

To run the server 
`(venv) $ flask run`

## Quick start
These apps can be opened undefended of the shoplift development store they are installed on. 
> The Next.js app is available  at  [Page Gen](https://lucky-pasca-ce4036.netlify.app) . It is currently hosted using Netlify
>
> The Python/Flask version is available at [PageGen py](https://spinning-walrus-vacuum.wayscript.cloud)
>

## What’s Included?
*  [Flask](http://flask.pocoo.org/)  - A microframework for Python web applications
*  [Werkzeug](http://werkzeug.pocoo.org/)  - A Flask framework that implements WSGI for handling requests.
*  [Bulma](https://getbootstrap.com/)  - An open source design system for HTML, CSS, and JS.
*  [Jinja2](http://jinja.pocoo.org/docs/2.10/)  - A templating language for Python, used by Flask.

 
Known issues 
Py version of this app successfully creates page and checks if the page already exists but has issues updating page. Could not be fixed due time constraints. app runs with no errors and  
Plan to fix issue
* write unit tests to determine source of issue.
*issue was fixed after writing this doc
*creating a updating a page might delete the previous content on the page


![generated image](https://github.com/dfodeker/justvibes/blob/mvp/assets/Screen%20Shot%202022-07-25%20at%202.07.29%20AM.png?raw=true)
