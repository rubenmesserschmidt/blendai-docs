********
Organize
********

Automatically organize objects into collections based on their names and types. This is useful for keeping your scene clean and structured with minimal effort.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/4geFjNvQIkQ" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>


How it Works
============

Select the objects you want to organize and choose *Organize* from BlendAI menu in the top right corner. BlendAI will then automatically create collections and move the objects into them based on their names and types.


Settings
========

Auto Collections
    If enabled, BlendAI will automatically generate the collections and their names based on the selected objects.

    - **Granularity**: The level of detail to organize the objects into collections. Higher Granularity will create more collections with fewer objects in them.

    If disabled, you can define them manually.

    - **Collections**: The collections to organize the objects into. Use the following format: ``Collection 1, Collection 2, Collection 3`` and so on.

Generation Quality
    See :ref:`here<preferences_generation_quality>`.


Model
=====

BlendAI's Organize feature is powered by OpenAI. The processing happens on their servers.
The model used is based on the quality settings in the :ref:`General Settings<preferences_settings_general>`.

Balanced Quality
    ``GPT4o Mini``

High Quality
    ``GPT4o``


.. _organize_limitations:

Limitations
===========

BlendAI's organize feature can make your scene more structured but has some limitations:

- **BlendAI can make mistakes**: The results may not always be perfect. Consider checking the organization after using the feature.
- **Random named objects**: Objects without a descriptive name may not be organized correctly. Meaning this feature only works well if your objects are named properly. This could be improved in the future.


.. _organize_pricing:

Pricing
=======

The price per organization is based on every started amount of objects plus a base price.

Balanced Quality
    :Base Price: ``0`` Credits
    :Per started 20 objects: ``1`` Credit

High Quality
    :Base Price: ``1`` Credit
    :Per started 10 objects: ``1`` Credit

Learn more about :doc:`../credits`.

