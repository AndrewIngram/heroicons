=========
heroicons
=========

.. image:: https://img.shields.io/github/workflow/status/adamchainz/heroicons/CI/main?style=for-the-badge
   :target: https://github.com/adamchainz/heroicons/actions?workflow=CI

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
   :target: https://github.com/adamchainz/heroicons/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/heroicons.svg?style=for-the-badge
   :target: https://pypi.org/project/heroicons/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Use `heroicons <https://heroicons.com/>`__ in your Django and Jinja templates.

Requirements
------------

Python 3.7 to 3.11 supported.

Django 3.2 to 4.1 supported.

----

**Working on a Django project?**
Improve your skills with `one of my books <https://adamj.eu/books/>`__.

----

Usage
-----

The ``heroicons`` package supports both Django templates and Jinja templates.
Follow the appropriate guide below.

Django templates
~~~~~~~~~~~~~~~~

1. Install with ``python -m pip install heroicons[django]``.

2. Add to your ``INSTALLED_APPS``:

   .. code-block:: python

       INSTALLED_APPS = [
           ...,
           "heroicons",
           ...,
       ]

Now in your templates you can load the template library with:

.. code-block:: django

    {% load heroicons %}

This provides three tags to render SVG icons: ``heroicon_outline``, ``heroicon_solid`` and ``heroicon_mini``, corresponding to the three icon styles in the set.
The tags take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `heroicons.com grid <https://heroicons.com/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed sizes: ``24`` for outline and solid, and ``20`` for mini.

* Any number of keyword arguments.
  These will be added as attributes in the output HTML.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

  Most attributes will be added to the ``<svg>`` tag containing the icon, but these attributes will be attached to the inner ``<path>`` tags instead:

  * ``stroke-linecap``
  * ``stroke-linejoin``
  * ``vector-effect``

Note: unlike the SVG code you can copy from `heroicons.com <https://heroicons.com/>`__, there is no default ``class``.

Examples
^^^^^^^^

An outline “academic-cap” icon:

.. code-block:: django

    {% heroicon_outline "academic-cap" %}

The same icon, solid, at 40x40 pixels, with some CSS classes:

.. code-block:: django

    {% heroicon_outline "academic-cap" size=40 class="h-4 w-4 inline" %}

That icon again, but with the paths changed to a narrower stroke width, and a "data-controller" attribute declared:

.. code-block:: django

    {% heroicon_outline "academic-cap" stroke_width=1 data_controller="academia" %}

Jinja templates
~~~~~~~~~~~~~~~

1. Install with ``python -m pip install heroicons[jinja]``.

2. Adjust your Jinja ``Environment`` to add the three global functions ``heroicon_outline``, ``heroicon_solid`` and ``heroicon_mini``, imported from ``heroicons.jinja``.
   For example:

   .. code-block:: python

       from heroicons.jinja import heroicon_outline, heroicon_solid, heroicon_mini
       from jinja2 import Environment

       env = Environment()
       env.globals.update(
           {
               "heroicon_outline": heroicon_outline,
               "heroicon_solid": heroicon_solid,
               "heroicon_mini": heroicon_mini,
           }
       )

Now in your templates you can call those functions, which render ``<svg>`` icons corresponding to the icon styles in the set.
The functions take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `heroicons.com grid <https://heroicons.com/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed sizes: ``24`` for outline and solid, and ``20`` for mini.

* Any number of keyword arguments.
  These will be added as HTML attributes to the output HTML.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

  Most attributes will be added to the ``<svg>`` tag containing the icon, but these attributes will be attached to the inner ``<path>`` tags instead:

  * ``stroke-linecap``
  * ``stroke-linejoin``
  * ``vector-effect``

Note: unlike the SVG code you can copy from `heroicons.com <https://heroicons.com/>`__, there is no default ``class``.

Examples
^^^^^^^^

An outline “academic-cap” icon:

.. code-block:: jinja

    {{ heroicon_outline("academic-cap") }}

The same icon, solid, at 40x40 pixels, with some CSS classes:

.. code-block:: jinja

    {{ heroicon_solid("academic-cap", size=40, class="h-4 w-4 inline") %}

That icon again, but with the paths changed to a narrower stroke width, and a "data-controller" attribute declared:

.. code-block:: jinja

    {{ heroicon_outline("academic-cap", stroke_width=1, data_controller="academia") %}
