**********
Fix Script
**********

Let BlendAI try to fix errors in your scripts.


How it Works
============

The feature will be executed on the current active script in the text editor. When starting the script fix, BlendAI will overwrite the script with the fixed version. If you want to keep the old version, make sure to save it before.
The resulting script will automatically be loaded into the text editor and attached to BlendAI's response in the :doc:`chat`.
The response will show a comparsion of what changes were made.


Settings
========

Error Message
    The error message you received when trying to run the script.

Additional Info (optional)
    Additional information about the error, e.g. under which circumstances it occured. This can help BlendAI to better understand the problem.

Generation Quality
    See :ref:`here<preferences_generation_quality>`.

.. tip::

    Test the fixed script in the space it is made for with :doc:`test_script`.


Limitations
===========

BlendAI's fix script feature can help you fix errors in your scripts but has some limitations:

- **BlendAI can make mistakes**: The resulting scripts may still contain errors. So you may have to run it multiple times or fix it by yourself.
- **Script length**: BlendAI can only generate scripts up to 8000 characters long. If your script is longer, consider splitting it into multiple parts.


.. _fix_script_pricing:

Pricing
=======

The pricing is based on the length of the input script.

Balanced Quality
    :Price per started 500 characters: ``1`` Credit

High Quality
    :Price per started 100 characters: ``1`` Credit

Learn more about :doc:`../credits`.

