********
Organize
********

Automatically organize objects into collections based on their names and types. This is useful for keeping your scene clean and structured with minimal effort.


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


Limitations
===========

BlendAI's organize feature can make your scene more structured but has some limitations:

- **BlendAI can make mistakes**: The results may not always be perfect. Consider checking the organization after using the feature.
- **Random named objects**: Objects without a descriptive name may not be organized correctly. Meaning this feature only works well if your objects are named properly. This could be improved in the future.


Pricing