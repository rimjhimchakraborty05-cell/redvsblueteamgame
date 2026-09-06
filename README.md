# CyberArena Security: Real-Time Cybersecurity Red Team vs Blue Team Game

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic%20Use-green.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)]()

> A command-line based cybersecurity training simulation platform providing hands-on offensive (Red Team) and defensive (Blue Team) challenge scenarios in a controlled, sandboxed environment.

---

## 📌 Project Overview

**CyberArena Security** bridges the gap between theoretical cybersecurity education and practical command-line operations. Participants select between **Red Team (Attacker)** and **Blue Team (Defender)** roles, navigating through 5 escalating levels of real-world scenarios.

The game features:
- **Sandboxed Execution**: Automated setup and cleanup of challenge directories (`challenge_files/`) ensuring an isolated, non-destructive learning environment.
- **Dynamic Scoring Engine**: Calculates score based on completion speed, attempts used (3 attempts max per level), and hint usage.
- **Built-In Terminal System**: Allows players to run system reconnaissance commands (`dir`, `ls`, `type`, `cat`, `findstr`, etc.) directly inside the game loop.
- **Assistance & Guidance**: In-game `help` and `hint` systems for progressive learning.

---

## 🎮 Game Tracks & Challenges

### 🔴 Red Team (Offensive Security)
| Level | Challenge Name | Objective | Skills Tested |
|:---:|:---|:---|:---|
| **0** | Find Hidden System Files | Uncover hidden configuration file (`.sysconfig`) | File attributes, system enumeration (`dir /a:h`, `ls -la`) |
| **1** | Decode Base64 Credentials | Decode encoded administrative credentials | Cryptographic decoding (`certutil`, `base64`) |
| **2** | Web Server Config Extraction | Extract admin password from `apache2.conf` | Configuration analysis, pattern searching |
| **3** | Shadow Password Hash | Locate password hash from `shadow.bak` | Linux shadow files, password auditing |
| **4** | SQL Injection Analysis | Extract vulnerable SQL injection query from `access.log` | Web security, SQL injection pattern detection |

### 🔵 Blue Team (Defensive Security)
| Level | Challenge Name | Objective | Skills Tested |
|:---:|:---|:---|:---|
| **0** | Detect Malware Signature | Identify Kovter trojan CNC signature in `syslog` | Log inspection, malware signature matching |
| **1** | Failed Login Analysis | Identify malicious IP conducting brute-force SSH attempts | Authentication log auditing, IP tracking |
| **2** | Firewall Misconfiguration | Detect unauthorized exposed ports (`firewall.conf`) | Network security, port exposure auditing |
| **3** | Critical Vulnerability Audit | Identify CVE identifier for pending critical update | Vulnerability management, CVE tracking |
| **4** | Network Intrusion & Exfiltration | Detect suspicious high-volume data exfiltration | NIDS analysis, incident response |

---

## 📊 Scoring Mechanism

Each level starts with a maximum possible score of **100 points**:

$$\text{Final Score} = \max(10, 100 - \text{Time Penalty} - \text{Attempt Penalty} - \text{Hint Penalty})$$

- **Time Penalty**: $-1$ point per 10 seconds spent (capped at $-50$ points).
- **Attempt Penalty**: $-10$ points per failed attempt (maximum 3 attempts per level).
- **Hint Penalty**: $-25$ points if the hint is revealed.
- **Minimum Score**: 10 points guaranteed upon level completion.

---

## 📂 Project Architecture

```
cybersec-arena-game/
├── README.md                 # Project documentation
├── .gitignore                # Git ignore patterns
├── run.py                    # Root entry point launcher
├── run_game.bat              # 1-click Windows batch launcher (UTF-8 enabled)
└── cyberarenasecurity/       # Core package
    ├── main.py               # Game state controller & loop
    ├── banner.py             # ASCII art & display banners (UTF-8/ASCII fallback)
    ├── challenge.py          # Red & Blue team challenge definitions
    ├── utils.py              # Command execution, sandboxing & team selector
    └── clang/
        └── nandini.py        # Password strength & entropy estimation tool
```

---

## 🚀 Installation & Running

### Prerequisites
- Python 3.8 or higher installed on your system.
- Standard terminal (Windows Command Prompt, PowerShell, Windows Terminal, or Linux Bash).

### Quick Start

#### On Windows:
Double-click `run_game.bat`, or run from PowerShell / Command Prompt:
```powershell
python run.py
```
*(Alternatively, you can navigate directly into `cyberarenasecurity` and run `python main.py`)*

#### On Linux / macOS:
```bash
python3 run.py
```

---

## 🕹️ In-Game Commands

When prompted inside any challenge level:
- `submit` : Submit your final answer for verification.
- `hint` : Display the hint for the current challenge (-25 score penalty on first use).
- `help` : View in-game command reference and helpful terminal commands.
- `exit` / `quit` : Safely clean up challenge files and exit the game.
- Any valid shell command (e.g., `dir`, `ls`, `type <file>`, `cat <file>`) to inspect files.

---

## 👥 Academic Credits & Acknowledgements

* **Institution:** CMR College of Engineering & Technology (Autonomous), Kandlakoya, Hyderabad
* **Affiliation:** JNTU Hyderabad (JNTUH)
* **Department:** Department of Computer Science and Engineering (Cyber Security)
* **Academic Batch:** 2023 – 2027 (Batch 20)
* **Supervisor:** Asst. Prof. G. Manisha

### Project Team Members:
- **K. Dhananjaya Reddy** ([GitHub: @DHANANJAYA0](https://github.com/DHANANJAYA0))
- **K.V. Manohar**
- **Rimjhim Chakraborty**

---

## 📄 License
Academic and educational use under JNTUH / CMRCET guidelines.
