# Controller-to-Mouse PyGame Project

A PyGame project setup for processing controller inputs and visualizing them with a minimal UI. This project provides the foundation for converting controller inputs to mouse movements.

## Project Structure

```
controller_project/
├── venv/                    # Virtual environment
├── main.py                  # Main application entry point
├── controller_input.py      # Controller input handling module
├── ui_display.py           # UI rendering module
├── config.py               # Configuration constants
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

## Features

- **Controller Detection**: Automatically detects and connects to available controllers
- **Input Visualization**: Real-time display of:
  - Controller connection status
  - Axis values (joysticks, triggers) with visual bars
  - Button states with colored indicators
  - Hat/D-pad states with directional indicators
- **Modular Architecture**: Separated concerns for easy extension
- **Placeholder for Mouse Conversion**: Ready for future implementation of controller-to-mouse movement

## Setup Instructions

### 1. Virtual Environment (Already Created)
The virtual environment has been set up in the `venv` directory.

### 2. Dependencies Installation
Pygame has been installed in the virtual environment. To reinstall if needed:
```bash
venv\Scripts\pip install -r requirements.txt
```

### 3. Running the Application
Activate the virtual environment and run the main script:
```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Run the application
python main.py
```

## Usage

1. Connect a game controller to your computer
2. Run the application
3. The UI will display:
   - Controller connection status (green if connected, red if not)
   - Real-time axis values as you move joysticks or triggers
   - Button states that light up when pressed
   - Hat/D-pad directional indicators
4. Press ESC or close the window to exit

## UI Components

### Status Section
- Shows controller connection status
- Displays controller name and ID
- Shows current mouse position (placeholder)

### Axis Values Section
- Shows all controller axes with numeric values
- Visual bars represent axis values (-1.0 to 1.0)
- Bars highlight when values exceed deadzone threshold

### Button States Section
- Grid of all controller buttons
- Buttons light up green when pressed
- Gray when not pressed

### Hat/D-pad Section
- Visual representation of hat/d-pad positions
- Dots indicate pressed directions
- Shows numeric (x, y) values

## Configuration

Edit `config.py` to customize:
- Screen dimensions and title
- Colors for UI elements
- Controller deadzone sensitivity
- UI layout positions
- Placeholder button mappings

## Future Implementation

This project is set up for future extension to convert controller inputs to mouse movements. Key areas for implementation:

1. **Mouse Movement Conversion**:
   - Map controller axes to mouse cursor movement
   - Implement acceleration and smoothing
   - Add configurable sensitivity settings

2. **Button Mapping**:
   - Map controller buttons to mouse clicks
   - Implement scroll wheel functionality
   - Add customizable mappings

3. **Advanced Features**:
   - Multiple controller support
   - Profile saving/loading
   - Calibration tools
   - On-screen keyboard integration

## Development Notes

- The project uses a modular architecture for easy maintenance
- Each component (input handling, UI, configuration) is separated
- TODOs and placeholders are marked for future implementation
- Error handling for controller disconnection/reconnection

## Requirements

- Python 3.7+
- PyGame 2.5.2
- Windows/Linux/macOS with controller support

## Troubleshooting

- **No controller detected**: Ensure controller is properly connected and recognized by your OS
- **Pygame not found**: Activate virtual environment or reinstall dependencies
- **UI not updating**: Check controller connection and try reconnecting

## License

This project is set up for educational and development purposes.