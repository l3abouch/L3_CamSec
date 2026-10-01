<div align="center">

```
██╗     ██████╗      ██████╗ █████╗ ███╗   ███╗███████╗███████╗ ██████╗
██║     ╚════╝     ██╔════╝██╔══██╗████╗ ████║██╔════╝██╔════╝██╔════╝
██║      ╚███╗     ██║     ███████║██╔████╔██║███████╗█████╗  ██║
██║      ╔══╝██╗   ██║     ██╔══██║██║╚██╔╝██║╚════██║██╔══╝  ██║
███████╗██████╔╝   ╚██████╗██║  ██║██║ ╚═╝ ██║███████║███████╗╚██████╗
╚══════╝╚═════╝     ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝
```

# L3\_CamSec

**Camera Permission Security Lab**

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-green?style=flat-square&logo=linux&logoColor=white)](https://github.com/l3abouch/L3_CamSec)
[![License](https://img.shields.io/badge/License-Educational-yellow?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0-cyan?style=flat-square)](https://github.com/l3abouch/L3_CamSec/releases)
[![Stars](https://img.shields.io/github/stars/l3abouch/L3_CamSec?style=flat-square&color=orange)](https://github.com/l3abouch/L3_CamSec/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/l3abouch/L3_CamSec?style=flat-square&color=purple)](https://github.com/l3abouch/L3_CamSec/commits)

*A local security laboratory for understanding browser camera permissions,*
*access control, and image capture behavior — in a fully controlled environment.*

</div>

---

> **⚠️ IMPORTANT**
> L3\_CamSec is designed exclusively for **educational use** and **authorized security testing**.
> Use it only on systems, browsers, and devices **you own or have explicit permission to test**.
> The author is not responsible for any misuse of this project.

---

## 📋 Project Information

| Property | Value |
|----------|-------|
| Version | 1.0 |
| Language | Python 3 + HTML/JS |
| Server | Python HTTP Server — `127.0.0.1:8080` |
| Platform | Linux |
| Network Scope | **Local only** (`localhost`) |
| Dependencies | None — stdlib only |
| Status | Active |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎥 **Camera Permission Demo** | Demonstrates how browsers handle camera permission requests |
| 🖼️ **Local Image Capture** | Captures images and saves them locally — nothing leaves your machine |
| 💾 **Local Storage Only** | All captured images stay under `logs/camera/` on your device |
| 🌐 **Built-in Web Server** | Single-command Python HTTP server — no external tools needed |
| ⚙️ **JSON Configuration** | Configurable through `config/config.json` |
| 🔒 **Localhost Binding** | Bound to `127.0.0.1` — never exposed to the network by default |
| 🐍 **Zero Dependencies** | Pure Python standard library — no pip installs required |
| 🐧 **Linux Native** | Designed for Linux security lab environments |

---

## 🗂️ Project Structure

```
L3_CamSec/
│
├── config/
│   └── config.json          # Laboratory configuration
│
├── server/
│   └── server.py            # Python HTTP server
│
├── web/
│   ├── index.html           # Landing page — permission request
│   └── continue.html        # Post-permission laboratory interface
│
├── logs/
│   └── camera/              # Auto-created — captured images stored here
│       └── photo_YYYY-MM-DD_HH-MM-SS.jpg
│
├── tests/                   # Test scripts
├── docs/                    # Documentation
│
├── l3_camsec                # CLI launcher (chmod +x)
├── .gitignore               # Excludes logs/ from Git
└── README.md
```

> **`logs/` is excluded from Git via `.gitignore`.**
> Captured images and session logs are never committed to this repository.

---

## 📦 Installation

```bash
git clone https://github.com/l3abouch/L3_CamSec.git
cd L3_CamSec
chmod +x l3_camsec
./l3_camsec
```

Then open your browser and navigate to:

```
http://127.0.0.1:8080
```

---

## ⚙️ Requirements

- Linux (any modern distribution)
- Python 3
- A modern web browser with camera support
- A connected camera or webcam
- Localhost access (`127.0.0.1`)

No external Python packages required — the project uses only the standard library.

---

## 🧭 How It Works

```
[ ./l3_camsec ]
      │
      ▼
[ Python HTTP Server starts on 127.0.0.1:8080 ]
      │
      ▼
[ Browser opens index.html ]
      │
      ▼
[ Browser asks user for camera permission ]
      │
      ├── Denied  → Permission denied — lab demonstrates refusal behavior
      │
      └── Granted → continue.html loads
                        │
                        ▼
                [ Image captured via browser API ]
                        │
                        ▼
                [ Saved to logs/camera/photo_YYYY-MM-DD_HH-MM-SS.jpg ]
```

Everything happens locally. No data leaves `127.0.0.1`.

---

## 💾 Image Storage

Captured images are saved to:

```
logs/camera/photo_YYYY-MM-DD_HH-MM-SS.jpg
```

Example:

```
logs/camera/photo_2026-09-30_23-17-31.jpg
```

- Files are stored **only on the local machine running the lab**
- The `logs/` directory is **excluded from Git** via `.gitignore`
- No image is uploaded, transmitted, or shared

---

## ⚙️ Configuration

Edit `config/config.json` to adjust laboratory settings:

```json
{
  "host": "127.0.0.1",
  "port": 8080,
  "log_dir": "logs/camera"
}
```

> **Do not change `host` to `0.0.0.0` unless you are in a fully isolated network
> and understand the security implications.**

---

## 🔒 Security Design

| Decision | Reason |
|----------|--------|
| Bound to `127.0.0.1` | Prevents any network exposure by default |
| `logs/` excluded from Git | Prevents accidental commit of captured images |
| No external dependencies | Reduces attack surface and supply chain risk |
| User-controlled permission | Browser permission model is never bypassed |
| Local storage only | No data transmission — everything stays on device |

---

## 📚 What You Can Learn

L3\_CamSec is a practical lab for exploring:

- How browsers implement camera permission models
- What happens when a web page requests device access
- How to handle browser APIs for media capture
- Local web application structure and HTTP server behavior
- Privacy-aware file handling and storage design
- Defensive security awareness around device permissions

---

## 🐧 Supported Platforms

| Distribution | Supported |
|-------------|-----------|
| Kali Linux | ✅ |
| Debian | ✅ |
| Ubuntu | ✅ |
| Linux Mint | ✅ |
| Fedora | ✅ |
| Pop!\_OS | ✅ |
| Arch Linux | ✅ |

---

## ⚠️ Disclaimer

> L3\_CamSec is provided **for educational and authorized security testing purposes only**.
>
> - Do **not** use this project to access cameras, devices, or systems without explicit authorization.
> - Do **not** deploy this on public or shared networks.
> - Do **not** use captured images for any purpose other than your own authorized testing.
>
> The author is **not responsible** for any misuse, legal consequences, or damage
> resulting from improper use of this project.
>
> By using L3\_CamSec, you confirm that you are testing only on systems
> **you own or have written permission to test**.

---

## 🤝 Contributing

Contributions, ideas, and bug reports are welcome.

Feel free to open an [Issue](https://github.com/l3abouch/L3_CamSec/issues)
or submit a [Pull Request](https://github.com/l3abouch/L3_CamSec/pulls).

---

## 👨‍💻 Author

<div align="center">

**L3ABOUCH**

[![GitHub](https://img.shields.io/badge/GitHub-l3abouch-181717?style=flat-square&logo=github)](https://github.com/l3abouch)
[![Instagram](https://img.shields.io/badge/Instagram-@l3abo__uch-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/l3abo_uch)
[![YouTube](https://img.shields.io/badge/YouTube-@l3abouch-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/@l3abouch)

</div>

---

## 📜 Changelog

| Version | Highlights |
|---------|-----------|
| **1.0** | Initial release — local camera permission lab, Python HTTP server, JSON config, local image storage, localhost binding |

---

## 🗺️ Roadmap

- [ ] Configurable capture resolution
- [ ] Multiple capture sessions with session IDs
- [ ] HTML report generation from captured session
- [ ] Unit tests for server and capture modules
- [ ] Browser compatibility matrix
- [ ] Optional CLI flags (`--port`, `--host`, `--no-browser`)

---

<div align="center">

If this project helped you understand browser security better,
consider giving it a ⭐ on GitHub.

[![Star this repo](https://img.shields.io/badge/⭐%20Star%20on%20GitHub-L3__CamSec-orange?style=for-the-badge)](https://github.com/l3abouch/L3_CamSec)

</div>
