*******
Explain
*******

Let BlendAI explain you any setting, operator, or node in Blender. This is a powerful feature to get help with Blender's vast amount of features and settings, even for the most experienced users.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/VN5mNeF6bz4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

How it Works
============

Simply right-click on what you wanna know more of and choose *Explain* from the context menu. BlendAI will then provide you with a detailed explanation of the property and its use cases.
For explaining nodes, select it before opening the context menu.

.. tip::

    When holding ``Shift`` while clicking *Explain*, BlendAI will answer in the Chat :ref:`chat_popup`.

You can reply to the explanation as usual to ask further questions or get more information.


Model
=====

BlendAI's Explain feature is powered by OpenAI. The processing happens on their servers.
The model used is based on the quality settings in the :ref:`General Settings<preferences_settings_general>`.

Balanced Quality
    ``GPT4o Mini``

High Quality
    ``GPT4o``


.. _explain_limitations:

Limitations
===========

The explain feature is very helpful but has some limitations:

- **BlendAI can make mistakes**: Just like when chatting, BlendAI can make mistakes when explaining things. Consider checking important information.
- **New features**: BlendAI may not know about the latest features in Blender and may not be able to explain them correctly. Use the Blender manual or other sources for the latest information.
- **Complex Operators**: Some operators come in many different configurations, which can lead to BlendAI telling you about internal settings that may not be useful for you.
- **Composition nodes**: Composition nodes are not supported yet but will be added in the future.


.. _explain_pricing:

Pricing
=======

Balanced Quality
    :Price per Explanation: ``1`` Credit

High Quality
    :Price per Explanation: ``3`` Credits

Learn more about :doc:`../credits`.