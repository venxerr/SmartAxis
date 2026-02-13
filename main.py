"""
Main entry point for the controller-to-mouse pygame project.
Sets up the game loop and coordinates between input handling and UI display.
"""

import pygame
import sys
from config import *
from controller_input import ControllerInput
from ui_display import UIDisplay


class ControllerApp:
    """Main application class for controller input visualization."""
    
    def __init__(self):
        """Initialize the application."""
        pygame.init()
        
        # Set up display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)
        
        # Set up clock for FPS control
        self.clock = pygame.time.Clock()
        
        # Initialize components
        self.controller_input = ControllerInput()
        self.ui_display = UIDisplay(self.screen)
        
        # Application state
        self.running = True
        self.mouse_pos = (0, 0)  # Placeholder for future mouse movement
        
        print("Controller-to-Mouse Project initialized")
        print("Connect a controller and move joysticks/press buttons to see input data")
    
    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.JOYDEVICEADDED:
                print("Controller connected")
                self.controller_input._detect_controller()
            elif event.type == pygame.JOYDEVICEREMOVED:
                print("Controller disconnected")
                self.controller_input.connected = False
                self.controller_input.controller = None
    
    def update(self):
        """Update application state."""
        # Update controller input
        self.controller_input.update()
        
        # Update mouse position (placeholder for future implementation)
        # In the future, this will convert controller input to mouse movement
        self.mouse_pos = pygame.mouse.get_pos()
        
        # TODO: Future implementation - convert controller input to mouse movement
        # if self.controller_input.connected:
        #     self._update_mouse_from_controller()
    
    def _update_mouse_from_controller(self):
        """Placeholder for future mouse movement implementation."""
        # This method will convert controller axis values to mouse movement
        # For now, it's just a placeholder
        pass
    
    def render(self):
        """Render the application."""
        # Get current controller state
        controller_info = self.controller_input.get_controller_info()
        axis_values = self.controller_input.get_all_axes()
        button_states = self.controller_input.get_all_buttons()
        hat_states = self.controller_input.get_all_hats()
        
        # Draw UI
        self.ui_display.draw(controller_info, axis_values, 
                           button_states, hat_states, self.mouse_pos)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main application loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        
        self.cleanup()
    
    def cleanup(self):
        """Clean up resources before exiting."""
        self.controller_input.disconnect()
        pygame.quit()
        print("Application shutdown complete")
        sys.exit()


def main():
    """Entry point for the application."""
    app = ControllerApp()
    app.run()


if __name__ == "__main__":
    main()