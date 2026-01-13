import wave
import io
import numpy as np
import soundfile as sf
import subprocess
import os

def record_audio():
    
    # Settings for INMP441 I2S microphone
    CHUNK = 1024           # Read 1024 samples at a time
    RATE = 16000          # 16kHz sample rate (good for voice)
    CHANNELS = 1           # Mono (INMP441 is mono)
    DURATION = 5           # Record for 5 seconds
    
    # I2S device path for Raspberry Pi
    # This assumes I2S is properly configured in config.txt
    i2s_device = "hw:0,0"  # ALSA device for I2S (may need adjustment)
    
    # Check if I2S device exists
    try:
        result = subprocess.run(['arecord', '-l'], capture_output=True, text=True)
        if 'card 0' not in result.stdout:
            print("Warning: I2S audio device not found. Make sure I2S is enabled in config.txt")
            print("Run: sudo raspi-config -> Advanced Options -> I2S")
            return None
    except FileNotFoundError:
        print("Error: arecord not found. Install alsa-utils: sudo apt-get install alsa-utils")
        return None
    
    # Record audio using arecord (ALSA command line tool)
    temp_file = "/tmp/i2s_recording.wav"
    cmd = [
        'arecord',
        '-D', i2s_device,      # I2S device
        '-f', 'S32_LE',        # 32-bit signed little endian (INMP441 outputs 24-bit in 32-bit frame)
        '-r', str(RATE),       # Sample rate
        '-c', str(CHANNELS),   # Mono
        '-d', str(DURATION),   # Duration in seconds
        temp_file
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        
        # Read the recorded file
        with open(temp_file, 'rb') as f:
            wav_bytes = f.read()
            
        # Clean up temp file
        os.remove(temp_file)
        
        # Show file info
        size_kb = len(wav_bytes) / 1024
        size_mb = len(wav_bytes) / (1024 * 1024)
        
        print(f"📊 File size: {len(wav_bytes):,} bytes")
        print(f"   = {size_kb:.1f} KB")
        print(f"   = {size_mb:.3f} MB")
        print(f"   Format: 32-bit I2S (INMP441 compatible)")
        
        return wav_bytes
        
    except subprocess.CalledProcessError as e:
        print(f"Error recording audio: {e}")
        print("Make sure I2S is properly configured and INMP441 is connected")
        return None
    except FileNotFoundError:
        print("Error: Temporary file not found")
        return None
    