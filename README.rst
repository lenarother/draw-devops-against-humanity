.. image:: https://travis-ci.org/lenarother/draw-devops-against-humanity.svg?branch=master
    :target: https://travis-ci.org/lenarother/draw-devops-against-humanity


============================
Draw Devops Against Humanity
============================

Print a random sentence about development and operations. Inspired and using data from `Devops Against Humanity <https://github.com/bridgetkromhout/devops-against-humanity>`_

This project was used to demonstrate configuration examples at EuroPython 2017.

0.0.4


Installing
==========

pip install draw-devops-against-humanity

Usage
=====

::

    $ draw
    Security through [Catastrophic Failure as a Service].

You can also make it your terminal default gritting. Make sure you have `fortune <https://en.wikipedia.org/wiki/Fortune_(Unix)>`_ installed and insert in your .bashrc or .bash_login:

::

    fortune | draw


Running the tests (dev)
=======================

To run all test and coding style tests use Makefile to install test requiremets and run the tests:

::

    make devinstall
    make tests


License
=======

This project is licensed under the MIT License - see the LICENSE.txt file for details.


Contact
=======

Magdalena Rother (rother.magdalena@gmail.com)


Acknowledgments
===============

This project was inspired by `Bridget Kromhout <https://github.com/bridgetkromhout>`_ `Devops Against Humanity <https://github.com/bridgetkromhout/devops-against-humanity>`_.

`Kristian Rother <https://github.com/krother>`_ provided comments and code review.
