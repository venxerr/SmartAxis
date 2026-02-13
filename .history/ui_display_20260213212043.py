"""
UI display module for pygame controller-to-mouse project.
Handles rendering of controller status and input information.
"""

import pygame
from config import *


class UIDisplay:
    """Manages the user interface display."""
    
    def __init__(self, screen):
        """Initialize UI display system."""
        self.screen = screen
        self.font_large = None
        self.font_small = None
        self._initialize_fonts()
    
    def _initialize_fonts(self):
        """Initialize pygame fonts."""
        pygame.font.init()
        self.font_large = pygame.font.SysFont(None, UI_FONT_SIZE)
        self.font_small = pygame.font.SysFont(None, UI_SMALL_FONT_SIZE)
    
    def draw_background(self):
        """Draw the background."""
        self.screen.fill(BACKGROUND_COLOR)
    
    def draw_status_section(self, controller_info, mouse_pos):
        """Draw controller status section."""
        y_pos = STATUS_SECTION_TOP
        
        # Title
        title = self.font_large.render("Controller Status", True, HIGHLIGHT_COLOR)
        self.screen.blit(title, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT * 2
        
        # Controller connection status
        status_color = SUCCESS_COLOR if controller_info["id"] >= 0 else ERROR_COLOR
        status_text = "Connected" if controller_info["id"] >= 0 else "Disconnected"
        status = self.font_small.render(f"Status: {status_text}", True, status_color)
        self.screen.blit(status, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT
        
        # Controller name
        name_text = self.font_small.render(f"Controller: {controller_info['name']}", True, TEXT_COLOR)
        self.screen.blit(name_text, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT
        
        # Controller ID
        id_text = self.font_small.render(f"ID: {controller_info['id']}", True, TEXT_COLOR)
        self.screen.blit(id_text, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT
        
        # Mouse position (placeholder for future implementation)
        mouse_text = self.font_small.render(f"Mouse: ({mouse_pos[0]}, {mouse_pos[1]})", True, TEXT_COLOR)
        self.screen.blit(mouse_text, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT * 2
        
        # Instructions
        instructions = [
            "Move joysticks to see axis values change",
            "Press buttons to see button states change",
            "Press ESC to quit",
        ]
        
        for instruction in instructions:
            instr_text = self.font_small.render(instruction, True, TEXT_COLOR)
            self.screen.blit(instr_text, (UI_PADDING, y_pos))
            y_pos += UI_LINE_HEIGHT
    
    def draw_axis_section(self, axis_values):
        """Draw controller axis values section."""
        y_pos = AXIS_SECTION_TOP
        
        # Title
        title = self.font_large.render("Axis Values", True, HIGHLIGHT_COLOR)
        self.screen.blit(title, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT * 2
        
        # Draw axis values
        if not axis_values:
            no_data = self.font_small.render("No axis data available", True, TEXT_COLOR)
            self.screen.blit(no_data, (UI_PADDING, y_pos))
            return
        
        # Calculate column positions
        col1_x = UI_PADDING
        col2_x = SCREEN_WIDTH // 2
        
        current_col = col1_x
        row = 0
        
        for i, (axis_name, value) in enumerate(sorted(axis_values.items())):
            # Alternate between columns
            if i % 8 == 0 and i > 0:
                current_col = col2_x
                row = 0
            
            # Create axis display
            axis_display = f"{axis_name}: {value:6.3f}"
            
            # Create visual bar for axis value
            bar_width = 200
            bar_height = 15
            bar_x = current_col + 120
            bar_y = y_pos + row * UI_LINE_HEIGHT
            
            # Draw bar background
            pygame.draw.rect(self.screen, (50, 50, 60), 
                           (bar_x, bar_y, bar_width, bar_height))
            
            # Draw bar value (centered, -1 to 1 range maps to bar width)
            bar_fill_width = int((value + 1) / 2 * bar_width)
            bar_color = HIGHLIGHT_COLOR if abs(value) > 0.1 else (80, 80, 90)
            pygame.draw.rect(self.screen, bar_color,
                           (bar_x, bar_y, bar_fill_width, bar_height))
            
            # Draw axis label and value
            axis_text = self.font_small.render(axis_display, True, TEXT_COLOR)
            self.screen.blit(axis_text, (current_col, y_pos + row * UI_LINE_HEIGHT))
            
            row += 1
    
    def draw_button_section(self, button_states):
        """Draw controller button states section."""
        y_pos = BUTTON_SECTION_TOP
        
        # Title
        title = self.font_large.render("Button States", True, HIGHLIGHT_COLOR)
        self.screen.blit(title, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT * 2
        
        if not button_states:
            no_data = self.font_small.render("No button data available", True, TEXT_COLOR)
            self.screen.blit(no_data, (UI_PADDING, y_pos))
            return
        
        # Calculate grid positions
        buttons_per_row = 8
        button_size = 40
        button_spacing = 10
        start_x = UI_PADDING
        
        row = 0
        col = 0
        
        for i, (button_name, pressed) in enumerate(sorted(button_states.items())):
            # Calculate position
            x_pos = start_x + col * (button_size + button_spacing)
            y_pos_button = y_pos + row * (button_size + button_spacing)
            
            # Draw button background
            button_color = SUCCESS_COLOR if pressed else (80, 80, 90)
            pygame.draw.rect(self.screen, button_color,
                           (x_pos, y_pos_button, button_size, button_size))
            pygame.draw.rect(self.screen, TEXT_COLOR,
                           (x_pos, y_pos_button, button_size, button_size), 2)
            
            # Draw button label
            button_label = button_name.replace("button_", "")
            label_text = self.font_small.render(button_label, True, TEXT_COLOR)
            text_rect = label_text.get_rect(center=(x_pos + button_size//2, 
                                                   y_pos_button + button_size//2))
            self.screen.blit(label_text, text_rect)
            
            # Update grid position
            col += 1
            if col >= buttons_per_row:
                col = 0
                row += 1
    
    def draw_hat_section(self, hat_states, y_offset=500):
        """Draw controller hat (D-pad) states section."""
        y_pos = y_offset
        
        # Title
        title = self.font_large.render("Hat (D-pad) States", True, HIGHLIGHT_COLOR)
        self.screen.blit(title, (UI_PADDING, y_pos))
        y_pos += UI_LINE_HEIGHT * 2
        
        if not hat_states:
            no_data = self.font_small.render("No hat data available", True, TEXT_COLOR)
            self.screen.blit(no_data, (UI_PADDING, y_pos))
            return
        
        hat_size = 60
        hat_spacing = 80
        start_x = UI_PADDING
        
        for i, (hat_name, hat_value) in enumerate(sorted(hat_states.items())):
            x_pos = start_x + i * hat_spacing
            
            # Draw hat background
            pygame.draw.rect(self.screen, (50, 50, 60),
                           (x_pos, y_pos, hat_size, hat_size))
            pygame.draw.rect(self.screen, TEXT_COLOR,
                           (x_pos, y_pos, hat_size, hat_size), 2)
            
            # Draw hat label
            hat_label = hat_name.replace("hat_", "Hat ")
            label_text = self.font_small.render(hat_label, True, TEXT_COLOR)
            self.screen.blit(label_text, (x_pos, y_pos - 20))
            
            # Draw hat direction indicators
            center_x = x_pos + hat_size // 2
            center_y = y_pos + hat_size // 2
            dot_size = 8
            
            # Draw center dot
            pygame.draw.circle(self.screen, TEXT_COLOR, (center_x, center_y), dot_size)
            
            # Draw direction dots based on hat value (x, y)
            hat_x, hat_y = hat_value
            
            # Up
            if hat_y == 1:
                pygame.draw.circle(self.screen, HIGHLIGHT_COLOR,
                                 (center_x, center_y - 20), dot_size)
            # Down
            if hat_y == -1:
                pygame.draw.circle(self.screen, HIGHLIGHT_COLOR,
                                 (center_x, center_y + 20), dot_size)
            # Left
            if hat_x == -1:
                pygame.draw.circle(self.screen, HIGHLIGHT_COLOR,
                                 (center_x - 20, center_y), dot_size)
            # Right
            if hat_x == 1:
                pygame.draw.circle(self.screen, HIGHLIGHT_COLOR,
                                 (center_x + 20, center_y), dot_size)
            
            # Draw hat value text
            value_text = self.font_small.render(f"({hat_x}, {hat_y})", True, TEXT_COLOR)
            self.screen.blit(value_text, (x_pos, y_pos + hat_size + 5))
    
    def draw(self, controller_info, axis_values, button_states, hat_states, mouse_pos):
        """Draw the complete UI."""
        self.draw_background()
        self.draw_status_section(controller_info, mouse_pos)
        self.draw_axis_section(axis_values)
        self.draw_button_section(button_states)
        self.draw_hat_section(hat_states)
        
        # Draw footer
        footer = self.font_small.render("Controller-to-Mouse Project - Setup Complete", 
                                       True, TEXT_COLOR)
        footer_rect = footer.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
        self.screen.blit(footer, footer_rect)