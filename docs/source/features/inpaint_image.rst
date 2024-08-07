*************
Inpaint Image
*************

Preview ideas and remove or replace objects in your images. This is perfect for getting an idea of how something would look like before spending much work on it.

How it Works
============

BlendAI will change masked out areas in the current open image in the image editor. The result is a new image which will automatically be loaded into the editor. So you will always keep the original image.

- **Result Resolution**: 1024 x 1024 pixels, no matter the original image resolution.


Settings
========

Description
    The description of what you want to change. Do not tell what to replace, but what there should be instead. Here are some examples:

    - A hole in the wall
    - Clear sky without clouds
    - A crack in the glass
    - Blue flowers in the grass

Mask
    :Alpha: Use the alpha channel of the image as the mask for inpainting.
    - **Paint Mask**: This will switch to the mask paint mode where you can paint the alpha in the image. To finish painting, press ``Shift + Enter``, this will bring the popup back up where you can commit and start the generation. To cancel painting, press ``Shift + Esc``.

    .. tip::

        When you dont need the mask anymore, go to Sidebar > Image and choose *Discard* in the top right corner. This will revert the changes to the images alpha channel.

    :Image: Use another image as the mask for inpainting. All white pixels in the image will be used as the mask, black pixels will be kept. Make sure the mask image has the same dimensions as the original image.
    - **Open**: This will open a file dialog where you can select the mask image.


Model
=====

BlendAI's Inpaint feature is powered by StabilityAI. The processing happens on servers from Replicate.

:Model:
    ``stable-diffusion-inpainting``


.. _inpaint_image_limitations:

Limitations
===========

BlendAI's inpaint feature will give you insights that save you much work, but it has its limitations:

- **Description understanding**: BlendAI can miss details of your description which can lead to inpainted images that are not what you expected.
- **Random patterns**: The inpainted parts of the image can contain random patterns.
- **No changes**: The inpainted image can look the same as the original image, especially when the mask is too small.
- **Color and quality**: The resulting image can have subtle color and quality changes in the non-masked areas.


.. _inpaint_image_pricing:

Pricing
=======

:Price per Inpaint: ``10`` Credits

Learn more about :doc:`../credits`.