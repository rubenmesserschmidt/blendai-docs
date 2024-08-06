****
Chat
****

Chat with your personal assistant, whenever you want and wherever you are. Get help with everything you need, from simple questions to complex tasks. The assistant is always there for you, ready to help.

.. _chat_input_field:

Input Field
===========

Message
    Type your message here.

    - **Auto Send**: Automatically send the message on pressing ``ENTER`` by holding this :ref:`hotkey <preferences_keymap>`.
    - **Auto Reply**: Automatically reply to the last message by holding this :ref:`hotkey <preferences_keymap>`.

    .. tip::

        BlendAI does always know in which space you are working right now. Therefore, you can ask questions and get help with the current context in Blender.

Attach Files
    Attach text and image files to your message. Opens a file dialog to select internal and external files.

    - **Internal File Browser**: Browse and select files from your Blender file system. The file select works the same as in the Blender file browser.

    .. note::

        The following file types are supported: ``.txt``, ``.xlsx``, ``.xls``, ``.csv``, ``.py``, ``.png``, ``.jpg``, ``.jpeg``
  
    .. warning::

        The maximum total input size is 1000 characters. This includes the message and all attachments.
        For images, you can attach a maximum of 2 files per message.

Send
    Send your message to BlendAI.


.. _chat_conversation:

Conversation
============

Message
    The message you sent to BlendAI.

    - **Edit**: Edit the message. This will paste your message and attachments if any into the input field.
    - **Remove**: Delete this message including BlendAI's response from the chat.

Response
    BlendAI's response to your message.

    - **Reply**: Reply to this response. If enabled, your next message will be a reply to this response. This is useful for following up on a specific topic.
    - **Copy**: Copy the response to the clipboard.
    - **Info**: Show additional information about the response such as time needed to generate it and quality settings used.

.. _chat_popup:

Popup
=====

Chat with BlendAI in a popup window with this :ref:`hotkey <preferences_keymap>`.
This allows you to get help as fast as possible, without interrupting your workflow.

While your answer is being generated, you can cancel anytime by pressing ``ESC``.

.. note::

    During the generation of an answer, the popup is attached to your cursor and moves with it. This is because it has to be redrawn every frame to show the progress of the generation. Hopefully, Blenders popup system will be improved in the future to allow for a more stable experience.

Create New Chat
    This will create a new empty chat. If you have an active chat, it will be saved to your chat history located in the :ref:`Main Panel<main_panel_menu>`.

Input Field
    See :ref:`chat_input_field`.


Examples
========

You can ask BlendAI virtually anything about Blender and 3D in general. Here are some examples to get you started:

- How can I simulate physics?
- What is the hotkey for the knife tool?
- Where can I show flipped normals?
- Why is my object not rendering?


Limitations
===========

BlendAI's Chat feature is very powerful, but it has its limitations. Here are some things to keep in mind:

- **BlendAI can make mistakes**: The assistant is not perfect and can make mistakes. This is due to the nature of AI but will only improve from here. So consider checking important information.
- **Complex questions**: While BlendAI can help with complex tasks, it does not know perfectly about every feature of Blender.
- **Latest features**: BlendAI does not have real-time information about the latest Blender features. So consider checking the Blender manual or other sources for the latest information.

Pricing
=======

Balanced Quality
    :Price Per Message: ``2`` Credits 

High Quality
    :Price Per Message: ``10`` Credits
