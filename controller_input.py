"""
Controller input handling module for pygame controller-to-mouse project.
Handles controller detection, input polling, and state management.
"""

import pygame
from config import CONTROLLER_DEADZONE


class ControllerInput:
    """Manages controller input detection and state."""
    
    def __init__(self):
        """Initialize controller input system."""
        self.controller = None
        self.controller_id = -1
        self.connected = False
        self.axis_values = {}
        self.button_states = {}
        self.hat_states = {}
        
        # Initialize pygame joystick module if not already initialized
        if not pygame.joystick.get_init():
            pygame.joystick.init()
        
        self._detect_controller()
    
    def _detect_controller(self):
        """Detect and connect to available controllers."""
        joystick_count = pygame.joystick.get_count()
        
        if joystick_count > 0:
            # Connect to the first available controller
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
            self.controller_id = 0
            self.connected = True
            
            # Initialize axis and button tracking
            self._initialize_state_tracking()
            print(f"Controller connected: {self.controller.get_name()}")
        else:
            self.connected = False
            print("No controllers detected")
    
    def _initialize_state_tracking(self):
        """Initialize dictionaries to track controller state."""
        if self.controller:
            # Track all axes
            num_axes = self.controller.get_numaxes()
            for i in range(num_axes):
                self.axis_values[f"axis_{i}"] = 0.0
            
            # Track all buttons
            num_buttons = self.controller.get_numbuttons()
            for i in range(num_buttons):
                self.button_states[f"button_{i}"] = False
            
            # Track all hats (D-pads)
            num_hats = self.controller.get_numhats()
            for i in range(num_hats):
                self.hat_states[f"hat_{i}"] = (0, 0)
    
    def update(self):
        """Update controller state by polling current inputs."""
        if not self.connected:
            # Try to reconnect if controller was disconnected
            self._detect_controller()
            return
        
        try:
            # Update axis values
            for i, axis_name in enumerate(list(self.axis_values.keys())):
                value = self.controller.get_axis(i)
                # Apply deadzone
                if abs(value) < CONTROLLER_DEADZONE:
                    value = 0.0
                self.axis_values[axis_name] = round(value, 3)
            
            # Update button states
            for i, button_name in enumerate(list(self.button_states.keys())):
                self.button_states[button_name] = bool(self.controller.get_button(i))
            
            # Update hat states
            for i, hat_name in enumerate(list(self.hat_states.keys())):
                self.hat_states[hat_name] = self.controller.get_hat(i)
                
        except pygame.error:
            # Controller disconnected
            self.connected = False
            self.controller = None
            print("Controller disconnected")
    
    def get_axis_value(self, axis_index):
        """Get value of specific axis."""
        axis_name = f"axis_{axis_index}"
        return self.axis_values.get(axis_name, 0.0)
    
    def get_button_state(self, button_index):
        """Get state of specific button."""
        button_name = f"button_{button_index}"
        return self.button_states.get(button_name, False)
    
    def get_hat_state(self, hat_index):
        """Get state of specific hat (D-pad)."""
        hat_name = f"hat_{hat_index}"
        return self.hat_states.get(hat_name, (0, 0))
    
    def get_all_axes(self):
        """Get all axis values as a dictionary."""
        return self.axis_values.copy()
    
    def get_all_buttons(self):
        """Get all button states as a dictionary."""
        return self.button_states.copy()
    
    def get_all_hats(self):
        """Get all hat states as a dictionary."""
        return self.hat_states.copy()
    
    def get_controller_info(self):
        """Get controller information."""
        if self.connected and self.controller:
            return {
                "name": self.controller.get_name(),
                "id": self.controller_id,
                "num_axes": self.controller.get_numaxes(),
                "num_buttons": self.controller.get_numbuttons(),
                "num_hats": self.controller.get_numhats(),
            }
        return {
            "name": "No controller",
            "id": -1,
            "num_axes": 0,
            "num_buttons": 0,
            "num_hats": 0,
        }
    
    def disconnect(self):
        """Clean up controller connection."""
        if self.controller:
            self.controller.quit()
        self.connected = False
        self.controller = None
        print("Controller disconnected")