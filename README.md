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

```

## Clone or download the script
```bash
git clone https://github.com/sanjeetkalyan/keybom.git
```
## Make the script executable:
```bash
chmod +x keybom.py

```

## Usage
- Run the script using Python:
```bash
python3 keybom.py
```
- To stop the keylogger, press Ctrl + C
- Statistics Tracked

- Total number of keystrokes
- Runtime duration
- Special keys frequency
- Character frequency distribution

## Features in Detail

- Real-time logging with millisecond precision
Automatic file creation and initialization
Error handling and debug logging
Statistics updated every 60 seconds
UTF-8 encoding support
Clean program termination handling

## Output Format
- Keyboard Log Format
```bash
=== Keybom Activity Log ===
Created by: Sanjeet Kalyan
========================================
YYYY-MM-DD HH:MM:SS.mmm: key_pressed
```

## Statistics Format (JSON)
```bash
{
    "tool_name": "Keybom",
    "author": "Sanjeet Kalyan",
    "total_keystrokes": count,
    "runtime": "duration",
    "special_keys_frequency": {},
    "character_frequency": {}
}
```

## Legal Disclaimer
This tool is for educational and authorized testing purposes only. Use only on systems you own or have explicit permission to test. Unauthorized keylogging may be illegal in your jurisdiction.
Error Handling
The tool includes comprehensive error handling for:

## File operations
Keyboard event processing
Statistics saving
Program initialization and termination

## Contributing
Feel free to submit issues and enhancement requests.



## MIT License

Copyright (c) 2024 Sanjeet Kalyan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
