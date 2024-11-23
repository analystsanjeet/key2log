# Keybom - Advanced Keylogger Tool

## Author
Created by: Sanjeet Kalyan

## Description
Keybom is an advanced keylogging tool written in Python that records keyboard inputs and provides detailed statistics about keystroke patterns. The tool features comprehensive logging, real-time statistics tracking, and error handling capabilities.

## Features
- Real-time keystroke logging with timestamps
- Special key detection and logging
- Keystroke statistics tracking
- JSON-formatted statistics export
- Debug logging system
- Periodic statistics saving
- Clean terminal interface with banner

## Files Generated
1. `keyboard_log.txt` - Main keystroke log file
2. `keystroke_stats.json` - Statistics and analytics data
3. `keylogger_debug.log` - Debug and error logging

## Requirements
- Python 3.x
- pynput library

## Installation
1. Install the required package:
```bash
pip3 install pynput


Clone or download the script
Make the script executable:

chmod +x keybom.py


Usage
Run the script using Python:

python3 keybom.py

To stop the keylogger, press Ctrl + C
Statistics Tracked

Total number of keystrokes
Runtime duration
Special keys frequency
Character frequency distribution

Features in Detail

Real-time logging with millisecond precision
Automatic file creation and initialization
Error handling and debug logging
Statistics updated every 60 seconds
UTF-8 encoding support
Clean program termination handling

Output Format
Keyboard Log Format
=== Keybom Activity Log ===
Created by: Sanjeet Kalyan
========================================
YYYY-MM-DD HH:MM:SS.mmm: key_pressed

Statistics Format (JSON)
{
    "tool_name": "Keybom",
    "author": "Sanjeet Kalyan",
    "total_keystrokes": count,
    "runtime": "duration",
    "special_keys_frequency": {},
    "character_frequency": {}
}

Legal Disclaimer
This tool is for educational and authorized testing purposes only. Use only on systems you own or have explicit permission to test. Unauthorized keylogging may be illegal in your jurisdiction.
Error Handling
The tool includes comprehensive error handling for:

File operations
Keyboard event processing
Statistics saving
Program initialization and termination

Contributing
Feel free to submit issues and enhancement requests.



License

This README provides a comprehensive overview of your tool, including installation instructions, usage guidelines, features, and important disclaimers. You may want to:

1. Add a specific license
2. Add more detailed installation instructions if needed
3. Include screenshots if desired
4. Add contact information
5. Include contribution guidelines
6. Add any specific system requirements or compatibility notes

Remember to update the README as you make changes to the tool's functionality.