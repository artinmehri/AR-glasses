**DIY AR Smart Glasses (Multimodal AI Wearable Prototype)**
===========================================================

A wearable **AI-assisted vision system** built on a Raspberry Pi Zero 2 W that combines **real-time camera input, voice interaction, and multimodal AI processing (Gemini + Together AI)** with an optical see-through display using a beam splitter.

This project demonstrates a full end-to-end embedded system integrating **hardware design, embedded Linux, signal processing, and cloud AI inference** into a functioning augmented vision prototype.

**📌 Overview**
---------------

This project is a **second-generation AR smart glasses prototype** designed to act as a real-time AI assistant in the user’s field of view.

The system works by capturing:

*   Visual input (Raspberry Pi Camera Module v2)
    
*   Audio input (MS3625 I2S MEMS microphone)
    

Both inputs are processed and sent to a multimodal AI pipeline (Google Gemini + Together AI). The AI generates contextual responses which are displayed through a **0.96” OLED screen reflected via a 45° beam splitter**, creating an optical AR overlay.

### **Core Idea**

A low-cost wearable system that turns the user’s surroundings into an interactive AI interface.

**⚙️ System Architecture**
--------------------------

Camera (CSI) ─────┐
                   ├──→ Raspberry Pi Zero 2 W ──→ WiFi ──→ Gemini / Together AI
Microphone (I2S) ─┘                                 ↓
                                                AI Response
                                                     ↓
                                             OLED (SSD1306)
                                                     ↓
                                          Beam Splitter Optics
                                                     ↓
                                              User’s Eye View
                                              
**✨ Features**
--------------

*   🎥 **Real-time visual capture** via Raspberry Pi Camera Module v2
    
*   🎤 **30-second audio input recording** using I2S MEMS microphone (MS3625)
    
*   🧠 **Multimodal AI processing** (image + audio fusion input)
    
*   🌐 **Cloud inference via Google Gemini + Together AI**
    
*   📟 **OLED-based AR-style overlay display (SSD1306, I2C)**
    
*   🔍 **Beam splitter optical projection (45° see-through display system)**
    
*   🔋 **Battery-powered wearable system (3.7V LiPo + buck converter)**
    
*   ⚙️ **Modular Python architecture for hardware abstraction**
    
*   🧪 **Extensive debugging + hardware iteration lifecycle documented**
    

**🧠 Tech Stack**
-----------------

### **Hardware**

*   Raspberry Pi Zero 2 W (1GHz quad-core, 512MB RAM)
    
*   Pi Camera Module v2 (8MP)
    
*   MS3625 / INMP441 I2S MEMS Microphone
    
*   SSD1306 0.96” OLED Display (I2C)
    
*   Beam splitter optical glass (15mm × 15mm, 45°)
    
*   3.7V LiPo Battery (2000mAh)
    
*   DC-DC Buck Converter (5V output)
    

### **Software**

*   Python 3.14.3
    
*   Raspberry Pi OS (64GB SD card deployment)
    
*   ALSA (arecord) for audio capture
    
*   I2C + I2S kernel interfaces
    
*   Virtual environment (dependency isolation)
    

### **AI APIs**

*   google-genai (Gemini multimodal API)
    
*   together API (fallback / alternative LLM processing)
    

### **Python Libraries**

from together import Together
from google import genai
from google.genai import types

**🧩 Repository Structure**
---------------------------

AR-glasses/
├── main.py                # Core orchestration loop
├── camera_module.py       # Image capture via CSI camera
├── mic_module.py          # I2S audio recording pipeline
├── display_module.py      # OLED rendering + formatting
├── ai_client.py          # Gemini + Together AI integration
├── requirements.txt      # Python dependencies
├── test.jpg              # Sample captured frame
├── tests_cam/            # Camera test utilities
├── oled/                 # OLED libraries/examples
└── __pycache__/          # Python cache files

**🔄 How It Works**
-------------------

1.  User activates system via power switch
    
2.  Camera captures environmental image
    
3.  Microphone records up to 30 seconds of audio query
    
4.  Both inputs are packaged and sent to AI API
    
5.  AI processes multimodal input (vision + speech)
    
6.  Response is generated as text
    
7.  OLED displays response
    
8.  Beam splitter reflects output into user’s field of view
    

**🔌 Installation & Setup**
---------------------------

### **1\. Clone repository**

git clone https://github.com/artinmehri/AR-glasses
cd AR-glasses

### **2\. Create virtual environment**

python3 -m venv venv
source venv/bin/activate

### **3\. Install dependencies**

pip install -r requirements.txt

If system error occurs:

pip install --break-system-packages -r requirements.txt   `

### **4\. Enable Raspberry Pi interfaces**

Edit:

sudo nano /boot/firmware/config.txt   `

Ensure:

dtparam=i2c_arm=on  dtparam=i2s=on  dtoverlay=googlevoicehat-soundcard  camera_auto_detect=1  dtparam=audio=off   `

### **5\. Run system**

python main.py   `

**🎤 Microphone System (Key Implementation)**
---------------------------------------------

Audio is captured using ALSA via I2S interface:

arecord -D plughw:0,0 -f S32_LE -r 48000 -c 1 -d 30 output.wav   `

### **Key design decisions:**

*   48kHz sampling rate for hardware stability
    
*   32-bit S32\_LE format for compatibility
    
*   Temporary WAV file buffering
    
*   Auto cleanup after recording
    

**⚡ Hardware Design Highlights**
--------------------------------

*   Dual power system:
    
    *   3.7V LiPo battery input
        
    *   5V regulated output via buck converter
        
*   Separate buses:
    
    *   I2C (OLED)
        
    *   I2S (Microphone)
        
    *   CSI (Camera)
        
*   Pull-up resistors (4.7kΩ) for stable I2C communication
    
*   Optical beam splitter at 45° for AR projection
    

**🧪 Challenges & Engineering Solutions**
-----------------------------------------

### **Key Issues Solved**

*   I2S microphone silence → fixed via wiring + device tree correction
    
*   OLED I2C failure → corrected overlay + SDA solder repair
    
*   Camera detection issues → ribbon cable reseating
    
*   Power instability → buck converter optimization
    
*   Python dependency conflicts → virtual environment isolation
    
*   API latency + WiFi issues → hotspot fallback system
    

**📊 Performance**
------------------

*   ⏱️ Average AI response time: 12–18 seconds
    
*   🔋 Battery life: 2.5–3.5 hours continuous use
    
*   ⚡ Power draw: 400mA idle / 800mA peak
    
*   📡 Stable operation via WiFi hotspot
    

**🧠 Engineering Learnings**
----------------------------

*   Embedded Linux device configuration (I2C/I2S/CSI)
    
*   Hardware debugging using signal-level reasoning
    
*   Real-world constraints of multimodal AI systems
    
*   Power management in wearable systems
    
*   System-level integration of hardware + cloud AI
    

**🚧 Future Improvements**
--------------------------

*   On-device AI inference (reduce cloud dependency)
    
*   Reduced latency pipeline (<5 seconds target)
    
*   Smaller PCB integration (replace jumper wiring)
    
*   Custom lightweight frame redesign
    
*   Wake-word activation system
    
*   Real-time streaming instead of batch processing
    

**👨‍💻 Authors**
-----------------

**Artin Mehri****Cary Zhuang**

Project: Microcontroller Culminating ActivityDate: January 16, 2026

**📄 License**
--------------

Recommended: **MIT License**

This allows:

*   Academic use
    
*   Portfolio visibility
    
*   Recruiter accessibility
    
*   Open-source collaboration
    

**👀 Recruiter Impression**
---------------------------

### **What stands out**

*   Real embedded system (not just software)
    
*   Multimodal AI pipeline (vision + audio)
    
*   Hardware + software + optics integration
    
*   Strong debugging and iteration history
    
*   Clear engineering ownership of complex subsystems
    

### **Skills demonstrated**

*   Embedded systems (Raspberry Pi, GPIO, I2C, I2S, CSI)
    
*   Python systems architecture
    
*   Hardware debugging & electronics
    
*   AI API integration (Gemini, Together AI)
    
*   Power systems design
    
*   Mechanical integration (3D printed wearable frame)
    
*   System-level thinking
    

### **Recruiter questions this project may trigger**

*   How did you debug I2S silence issues at signal level?
    
*   Why Raspberry Pi Zero 2 W instead of ESP32 or Jetson?
    
*   How did you manage latency in multimodal inference?
    
*   What would you redesign for v3?
    
*   Could this run edge AI instead of cloud?
    

**🛠️ Suggested Improvements (Honest)**
---------------------------------------

*   Add real architecture diagram image (not ASCII only)
    
*   Add photos + demo video prominently at top
    
*   Clean up repo (remove **pycache**)
    
*   Add setup script for Raspberry Pi
    
*   Add wiring schematic PDF directly in repo
    
*   Add “system boot flow diagram”
