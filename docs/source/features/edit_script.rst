***********
Edit Script
***********

Adjust your scripts to your needs with BlendAI. Perfect for fine tuning or adding new features.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Ia1XNWWdN7w?si=wKjy_rmILVCbmNR7&amp;start=350" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


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
    

Model
=====

BlendAI's Edit Script feature is powered by OpenAI. The processing happens on their servers.
The model used is based on the quality settings in the :ref:`General Settings<preferences_settings_general>`.

Balanced Quality
    ``GPT4o Mini``

High Quality
    ``GPT4o``


.. _edit_script_limitations:

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
    :Price per started 1000 characters: ``1`` Credit

High Quality
    :Price per started 200 characters: ``1`` Credit

Learn more about :doc:`../credits`.

