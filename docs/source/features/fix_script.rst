**********
Fix Script
**********

Let BlendAI try to fix errors in your scripts.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Ia1XNWWdN7w?si=wKjy_rmILVCbmNR7&amp;start=450" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


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


Model
=====

BlendAI's Fix Script feature is powered by OpenAI. The processing happens on their servers.
The model used is based on the quality settings in the :ref:`General Settings<preferences_settings_general>`.

Balanced Quality
    ``GPT4o Mini``

High Quality
    ``GPT4o``


.. _fix_script_limitations:

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
    :Price per started 1000 characters: ``1`` Credit

High Quality
    :Price per started 200 characters: ``1`` Credit

Learn more about :doc:`../credits`.

