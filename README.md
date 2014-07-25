html-prototypes
===============

html-prototypes is a [Flask](http://flask.pocoo.org/) application, with [Grunt](http://gruntjs.com/) workflow to generate assets.


## Requirements

### [Node](http://nodejs.org/)

You may already have it, try:

```
node --version
```

Your version needs to be at least v0.10.0.

### Grunt

Make sure you've installed the Grunt command line interface --- see http://gruntjs.com/getting-started

### The Sass ruby gem

You probably already have Ruby installed, try

```
ruby -v
```

When you've confirmed you have Ruby installed, run ```gem install sass``` to install Sass.

### A Python virtual environment

1. install [virtualenv](https://virtualenv.pypa.io/en/latest)

2. install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

Note very important the part in virtualenvwrapper install intructions about sourcing the virtualenvwrapper.sh in your .bash_profile.

On my machine I have the following in my .bash_profile

```
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

So when I call ```mkvirtualenv some-name``` I get a some-name virtual environment directory in ~/.virtualenvs

Now create a virtualenv for the html-prototypes project

```
mkvirtualenv html-prototypes
```

This automatically activates the virtualenv. Once done any pip installs will install into that virtualenv.

Anytime you want to activate the virtualenv from that point on, you just enter

```
workon html-prototypes
```


## Getting started

Once you've got the requirements in place:

* Clone this repo.
* Ensure you’ve cd’ed into the style-guide folder, then ```npm install``` to install dependencies.
* Start your Python virtual environment: ```workon html-prototypes```
* To run the server and have sass files watched: ```grunt```
