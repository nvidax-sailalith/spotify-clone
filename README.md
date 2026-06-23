# 🎵 Beatwave - Immersive Audio Hub

[![Live Site](https://img.shields.io/badge/Live-Hosted_on_GitHub_Pages-059669?style=for-the-badge&logo=github)](https://nvidax-sailalith.github.io/spotify-clone/index.html)
[![Technology](https://img.shields.io/badge/Tech-HTML5_/_CSS3_/_JS-3b82f6?style=for-the-badge)](https://nvidax-sailalith.github.io/spotify-clone/index.html)
[![Design](https://img.shields.io/badge/Design-Spotify_Dark_HUD-1db954?style=for-the-badge)](https://nvidax-sailalith.github.io/spotify-clone/index.html)

> **Beatwave** is a sleek, Spotify-inspired dark UI music player implemented in a single self-contained HTML page. It features real-time audio visualization across multiple modes and an autonomous Web Audio API synthesizer engine that procedurally generates tracks completely offline.

⚡ **Experience the Live App:** [nvidax-sailalith.github.io/spotify-clone](https://nvidax-sailalith.github.io/spotify-clone/index.html)

---

## 📸 Interface Preview & Aesthetic Style
The interface replicates Spotify's premium obsidian HUD layout:
*   **Obsidian Panel Grid:** Clean, rounded cards with `#121212` backgrounds separated by precise `8px` spacing gaps.
*   **Vibrant Accent Animations:** Smooth micro-interactions, scaling play controls, and a rotating vinyl-disc album art animation that syncs to playback.
*   **Dark Mode Optimization:** Custom overrides for select option elements to ensure perfect text contrast in any system environment.

---

## 🛠️ Key Features

### 1. Offline Procedural Synthesizer Engine
Never lose your music. If network streams fail or you go offline, Beatwave initiates its built-in Web Audio API synthesiser to procedurally generate beats:
*   **Drums (Kick, Snare, Hi-hat):** Low-level oscillator and noise buffer scheduling.
*   **Synthesized Harmony:** Dynamically scheduled basslines and lead melodies mapped to retro chord presets.
*   *Note: This engine automatically pauses and bypasses when playing local files to preserve original audio.*

### 2. Four High-Fidelity Visualization Modes
Dynamic rendering of audio frequencies directly onto interactive canvases:
1.  **Spectrograph Bars:** Classical frequency bars with custom double-color gradients.
2.  **Orbital Radial Ray:** Circular rays pulsing outwards to the bass register amplitude.
3.  **Liquid Oscilloscope:** Real-time time-domain oscilloscope sine-wave path.
4.  **Neon Helix Dust:** Neon particles floating and translating to frequency levels.

### 3. Local Files Upload (Offline Audio Playback)
*   **Local Ingestion:** Upload `.mp3`, `.wav`, or `.ogg` files directly from your computer using the upload tray button.
*   **Filename Metadata Parser:** Automatically extracts song titles and artists from local filenames.
*   **Auto-Bypass:** Intelligently disables the synth engine and adjusts CORS credentials dynamically for local `blob:` URLs to guarantee clean audio playback.

### 4. Custom Playlist & Operations
*   Create, view, and delete custom playlists directly in the sidebar.
*   Click the options menu (`...`) on any song row to quickly assign or toggle it inside your playlists without losing scroll position.

---

## 🚀 Getting Started

Since it is a single-file application, you can run it locally in two ways:

### Method 1: Local Server (Recommended)
Running through an HTTP server ensures that Web Audio context parameters and local stream loading policies work without browser sandbox restrictions.

1. Open a terminal in this folder and run:
   ```bash
   python server.py
   ```
2. The server starts on [http://localhost:8080](http://localhost:8080) and automatically opens your browser.

### Method 2: Direct File Execution
Double-click `index.html` to open it in Chrome, Edge, or Firefox. Toggling **Web Audio Synth** ON lets you experience the offline synthesizer engine.

---

*Developed with 💚 as an advanced AI-guided "vibe coding" music player.*
