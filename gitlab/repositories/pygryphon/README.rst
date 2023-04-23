PyAztro 
============
|downloads|  |GitHub make-a-pull-requests|  |Maintenance yes| |Paypal| |say thanks|

PyAztro is a client library for `aztro <https://github.com/sameerkumar18/aztro>`_ written in Python.

aztro provides horoscope info for sun signs such as Lucky Number, Lucky Color, Mood, Color, Compatibility with other sun signs, description of a sign for that day etc.

Documentation for aztro API is available `here <https://aztro.sameerkumar.website>`_, documentation for PyAztro most of the common usage.



Requirements
---------------

* Python 3+ (Recommended)
* The ``requests`` and ``dateutils`` library. `pip` should handle this for you when installing pyaztro.

Installation
---------------
::

    $ pip install pyaztro

Usage
------------------
:: 

    >>> import pyaztro
    >>> horoscope = pyaztro.Aztro(sign='aries')

    # Mood
    >>> horoscope.mood
    'Relaxed'
    
    # Lucky time
    >>> horoscope.lucky_time
    '2pm'
    
    # Description
    >>> horoscope.description
    'If you don't have big plans, you can rest assured that you will soon. A surprise missive is waiting. Enjoy. It's spontaneity, not variety, that's the spice of life.'
    
    # Sun sign date range
    >>> horoscope.date_range
    [datetime.datetime(2019, 3, 21, 0, 0), datetime.datetime(2019, 4, 20, 0, 0)]

    # Lucky Color
    >>> horoscope.color
    'Spring Green'
    
    # Sign compatibility
    >>> horoscope.compatibility
    'Aquarius'
    
    # Horoscope date for which the info is valid for
    >>> horoscope.current_date
    datetime.date(2019, 6, 2)
    
    # Lucky number
    >>> horoscope.lucky_number
    85
    

Support
----------
If you encounter any bugs, please let me know by `creating an issue <https://github.com/sameerkumar18/pyaztro/issues/new>`_ or tweeting at me `@sameer_kumar018 <https://www.twitter.com/sameer_kumar018>`_.

Author
------
`Sameer Kumar <https://sameerkumar.website>`_




.. |downloads| image:: https://pepy.tech/badge/pyaztro
    :target: https://pepy.tech/project/pyaztro

.. |GitHub make-a-pull-requests| image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
   :target: http://makeapullrequest.com

.. |say thanks| image:: https://img.shields.io/badge/say-thanks-ff69b4.svg
   :target: https://saythanks.io/to/sameerkumar18
   
.. |Maintenance yes| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://gitHub.com/sameerkumar18/pyaztro

.. |Paypal| image:: https://img.shields.io/badge/Paypal-Donate-blue.svg
   :target: https://www.paypal.me/sameerkumar18
