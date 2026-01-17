import subprocess
import os

def record_audio(duration=30, rate=48000, channels=1):
    """
    Record audio from MS3625/INMP441 I2S microphone
    
    Args:
        duration: Recording time in seconds (default 30 for conversation)
        rate: Sample rate (48000Hz - hardware default)
        channels: 1=mono
    
    Returns:
        bytes: WAV file data, or None if failed
    """
    
    i2s_device = "plughw:0,0"
    temp_file = "/tmp/i2s_recording.wav"
    
    cmd = [
        'arecord',
        '-D', i2s_device,
        '-f', 'S32_LE',
        '-r', str(rate),
        '-c', str(channels),
        '-d', str(duration),
        temp_file
    ]
    
    print(f"🎤 Recording {duration} seconds...")
    print("   Speak now!")
    
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        if not os.path.exists(temp_file):
            print("❌ Recording file not created")
            return None
        
        with open(temp_file, 'rb') as f:
            wav_bytes = f.read()
        
        os.remove(temp_file)
        
        size_kb = len(wav_bytes) / 1024
        print(f"✅ Recorded {size_kb:.1f} KB")
        
        return wav_bytes
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Recording failed: {e.stderr}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None