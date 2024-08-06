***********
Edit Script
***********

Adjust your scripts to your needs with BlendAI. Perfect for fine tuning or adding new features.


How it Works
============

The feature will be executed on the current active script in the text editor.
The resulting script will automatically be loaded into the text editor and attached to BlendAI's response in the :doc:`chat`.
The response will show a comparsion of what changes were made.


Settings
========

Description
    Instructions of what you want to change in the script. The more detailed the description, the better the script can be generated.

New File
    If enabled, the new script will be generated in a new file.

    - **File Name**: The name of the new file.

    If disabled, the current script will be overwritten.

Generation Quality
    See :ref:`here<preferences_generation_quality>`.

.. tip::

    Test the adjusted script in the space it is made for with :doc:`test_script`.


Limitations
===========

BlendAI's fix script feature can help you fix errors in your scripts but has some limitations:

- **BlendAI can make mistakes**: The adjusted script may not work as expected. Consider trying different instructions or adjust them yourself.
- **Script length**: BlendAI can only generate scripts up to 8000 characters long. If your script is longer, consider splitting it into multiple parts.


.. _edit_script_pricing:

Pricing
=======

The pricing is based on the length of the input script.

Balanced Quality
    :Price per started 500 characters: ``1`` Credit

High Quality
    :Price per started 100 characters: ``1`` Credit

Learn more about :doc:`../credits`.

