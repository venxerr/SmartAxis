"""
Configuration constants for the controller-to-mouse pygame project.
"""

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Controller Input to Mouse Movement"
FPS = 60

# Colors
BACKGROUND_COLOR = (30, 30, 40)
TEXT_COLOR = (220, 220, 220)
HIGHLIGHT_COLOR = (100, 150, 255)
ERROR_COLOR = (255, 100, 100)
SUCCESS_COLOR = (100, 255, 150)

# UI settings
UI_PADDING = 20
UI_FONT_SIZE = 24
UI_SMALL_FONT_SIZE = 18
UI_LINE_HEIGHT = 30

# Controller settings (placeholders for future implementation)
CONTROLLER_DEADZONE = 0.1
MOUSE_SENSITIVITY = 10.0
BUTTON_MAPPINGS = {
    # Placeholder for button to mouse action mappings
    "A": "left_click",
    "B": "right_click",
    "X": "middle_click",
    "Y": "scroll_up",
}

# UI layout positions
STATUS_SECTION_TOP = 50
AXIS_SECTION_TOP = 200
BUTTON_SECTION_TOP = 400