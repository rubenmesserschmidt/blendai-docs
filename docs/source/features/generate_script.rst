***************
Generate Script
***************

Automate recurring tasks to streamline your workflow by creating scripts with BlendAI.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Ia1XNWWdN7w" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


How it Works
============

When starting the script generation, BlendAI will create a new Python file with an appropriate name. Then it will generate the script based on the instructions you provided.
The resulting script will automatically be loaded into the text editor and attached to BlendAI's response in the :doc:`chat`.


Settings
========

Description
    Instructions of what the script should do. The more detailed the description, the better the script can be generated.

Space
    The space in which the script should be working in. For example, if you want to automate a task for shaders, choose the Node Editor.

Generation Quality
    See :ref:`here<preferences_generation_quality>`.

.. tip::

    Test your generated script in the space of your choice with :doc:`test_script`.


Model
=====

BlendAI's Generate Script feature is powered by OpenAI. The processing happens on their servers.
The model used is based on the quality settings in the :ref:`General Settings<preferences_settings_general>`.

Balanced Quality
    ``GPT4o Mini``

High Quality
    ``GPT4o``


.. _generate_script_limitations:

Limitations
===========

BlendAI's generate script feature can help you automate tasks but has some limitations:

- **BlendAI can make mistakes**: The generated scripts may contain errors and not works as expected. So use them with caution.
- **3D Objects**: BlendAI cant generate scripts that can create complex 3D models, but it can help you making it easier to create them by yourself.
- **Script complexity**: BlendAI can only generate scripts up to 8000 characters long. The more complex the script, the more likely it will contain errors.


.. _generate_script_pricing:

Pricing
=======

Balanced Quality
    :Price per script: ``2`` Credits

High Quality
    :Price per script: ``10`` Credits

Learn more about :doc:`../credits`.

