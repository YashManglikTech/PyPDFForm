Module: PDF Form Helpers
Purpose: Fill PDF forms with various form elements (text, checkboxes, radio buttons, images, signatures)

Main Functions:

1. check_radio_handler(widget, middleware, radio_button_tracker):
    - Get font size from widget or middleware settings
    - Calculate drawing coordinates
    - If checkbox and checked:
        Mark for drawing
    - If radio button:
        Track group position
        If selected position matches current button:
            Mark for drawing
    - Return drawing parameters (text, x, y, draw_flag)

2. signature_image_handler(widget, middleware, images_to_draw):
    - If image stream exists:
        Convert to JPG format
        Calculate image coordinates and dimensions
        Add to drawing list
        Return true
    - Otherwise return false

3. text_handler(widget, middleware):
    - Calculate text line coordinates
    - Get drawing coordinates
    - Return drawing parameters (text, x, y, true)

4. get_drawn_stream(to_draw, stream, action):
    For each page in document:
        Create watermark list
        Generate watermarks for elements to draw
        Merge watermarks with PDF stream
    Return modified PDF

5. fill(template_stream, widgets):
    Initialize tracking dictionaries
    For each page and widget:
        Get widget key
        Based on widget type:
            - Checkbox/Radio: Handle with check_radio_handler
            - Signature/Image: Handle with signature_image_handler
            - Text: Handle with text_handler
        If drawing parameters valid:
            Add to drawing instructions
    Draw text elements
    If images exist:
        Draw image elements
    Return modified PDF

6. enable_adobe_mode(pdf, adobe_mode):
    If adobe mode requested and form exists:
        Set PDF needs appearances flag

7. simple_fill(template, widgets, flatten, adobe_mode):
    Create PDF reader and writer
    Enable adobe mode if requested
    For each page and annotation:
        Get widget key
        Based on widget type:
            - Checkbox: Update checkbox value
            - Radio: Track and update radio value
            - Dropdown: Update dropdown value
            - Text: Update text value
        If flatten requested:
            Flatten appropriate widget type
    Write modified PDF to bytes
    Return modified PDF

Flow:
1. User provides PDF template and widget data
2. System either:
   a. Uses watermark-based filling (fill())
      - Draws elements on top of PDF
      - Better for complex rendering
   OR
   b. Uses simple filling (simple_fill())
      - Modifies PDF form fields directly
      - Better for simple forms
3. Returns modified PDF with filled form elements
