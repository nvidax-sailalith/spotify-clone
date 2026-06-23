# Beatwave - Immersive Audio Hub

A sleek, Spotify-inspired dark UI music player implemented in a single self-contained HTML page. 

It features real-time audio visualization across multiple modes and an autonomous Web Audio API synthesizer engine that procedurally generates tracks completely offline when streams are unavailable.

## 🌟 Key Features
- **Sleek Premium Dark HUD**: Features glassmorphism (`backdrop-filter`), smooth hover states, dynamic playing states, rotating vinyl-disc album art, and an responsive sidebar grid layout.
- **Procedural Synthesizer Engine**: Automatically synthesizes retro synthwave, lofi, techno, or ambient space tracks using low-level Web Audio API oscillators, noise generators, filters, and amp envelopes.
- **Offline Reliability**: If network streams are blocked by CORS or the user is offline, the app switches to Synth mode, ensuring that audio playback and the visualizer are 100% functional.
- **Four Visualization Modes**:
  1. **Spectrograph Bars**: Classical frequency bar bars with neon gradients.
  2. **Orbital Radial Ray**: Circular orbital rays pulsing to bass amplitude.
  3. **Liquid Oscilloscope**: Liquid time-domain sine-wave plot.
  4. **Neon Helix Dust**: Procedural particles floating upwards and reacting to tempo.
- **Custom Playlists**: Create, view, add, and remove playlists dynamically through the Sidebar navigation layout.
- **Full Player Bar Controls**: Interactive seeking timeline, volume controls, mute/unmute toggles, shuffle, repeat, and play/pause buttons.

## 🚀 Getting Started

Since it is a single-file application, you can run it in two ways:

### Method 1: Python Web Server (Recommended)
Running it through a local HTTP server ensures that Web Audio context parameters and stream loading policies work without browser sandbox warnings (e.g. `file://` security restrictions).

1. Open a terminal/command prompt in this folder.
2. Run the provided Python script:
   ```bash
   python server.py
   ```
3. The server will start on `http://localhost:8080` and automatically open your default browser.

### Method 2: Direct File Execution
Double-click `index.html` to open it directly in Google Chrome, Microsoft Edge, or Firefox. Note that some streaming tracks may trigger browser security blocks depending on browser settings; simply leave the **Web Audio Synth** switch toggled **ON** to enjoy the synthesized tracks.
