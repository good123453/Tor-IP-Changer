# Tor-IP-Changer
Tor IP Changer - Anonymous IP rotation tool for privacy and security. Automatically changes your IP through Tor network at customizable intervals. Includes auto-installation of dependencies. For legal privacy protection and security testing.



# Tor IP Changer 🛡️

A powerful Tor-based IP rotation tool for privacy, security, and anonymity. Automatically change your IP address at customizable intervals using the Tor network.

## ⚠️ IMPORTANT DISCLAIMER

**This tool is for LEGAL purposes only:**
- ✅ Personal privacy protection
- ✅ Security testing & research
- ✅ Network anonymity
- ✅ Cybersecurity education
- ✅ Self-defense against tracking

**Illegal activities are strictly prohibited. User is responsible for their actions.**

## Features ✨

- 🔄 Automatic IP rotation via Tor
- ⏱️ Customizable rotation intervals
- ♾️ Infinite or limited IP changes
- 🔧 Auto-installation of dependencies (Tor, requests)
- 🎯 Easy-to-use interactive menu
- 🛠️ Clean error handling & logging
- 🐧 Linux/Ubuntu optimized

## Command Categories 📚

- **Automatic Dependency Check** - Installs Tor and Python requests if missing
- **IP Address Detection** - Shows current IP through Tor proxy
- **IP Rotation** - Changes IP on demand or at intervals
- **Infinite Mode** - Keep changing IP indefinitely
- **Timed Mode** - Set specific number of IP changes

## How to Use ���

### Prerequisites
- Linux/Ubuntu system
- Python 3.x installed
- Internet connection
- Sudo access (for Tor installation)

### Installation

```bash
# Clone the repository
git clone https://github.com/good123453/Tor-IP-Changer.git
cd Tor-IP-Changer

# Run the tool
python3 Tor_IP_Changer.py
```

### Usage Steps

1. **Run the program:**
   ```bash
   python3 Tor_IP_Changer.py
   ```

2. **Enter rotation interval** (in seconds, e.g., 60)

3. **Enter number of changes** (or press Enter for infinite)

4. **Tool automatically:**
   - Starts Tor service
   - Changes your IP at intervals
   - Displays new IP address
   - Press Ctrl+C to stop

### Example

```
[+] time to change Ip in Sec [type=60] >> 60
[+] How many times do you want to change your IP? >> 10

Starting IP rotation...
[+] Your IP has been Changed to: 185.220.101.45
[+] Your IP has been Changed to: 45.142.120.11
...
```

## Requirements 📦

```
requests>=2.25.0
requests[socks]>=2.25.0
Tor service (auto-installed if missing)
```

## How It Works 🔧

1. **Dependency Check** - Automatically installs missing packages
2. **Tor Service** - Starts Tor if not running
3. **Proxy Setup** - Configures SOCKS5 proxy (127.0.0.1:9050)
4. **IP Check** - Fetches current IP through Tor
5. **IP Rotation** - Reloads Tor to get new circuit/IP
6. **Logging** - Shows each IP change

## Security Notes 🔐

- Uses SOCKS5 proxy for anonymity
- Communicates through Tor network
- Does NOT store connection logs
- Local operation only
- No data transmission beyond Tor

## Troubleshooting 🔨

### "Tor start failed"
```bash
sudo service tor start
sudo service tor status
```

### "NetworkError: your connection are weak"
- Check internet connection
- Verify Tor is running: `systemctl status tor`
- Wait for Tor to connect to network (takes ~30 seconds)

### "Permission denied"
```bash
# Run with sudo
sudo python3 Tor_IP_Changer.py
```

### Tor not installed
Tool auto-installs it, but you can manually install:
```bash
sudo apt update
sudo apt install tor -y
sudo service tor start
```

## System Requirements 🖥️

- **OS:** Linux/Ubuntu (Debian-based)
- **Python:** 3.6 or higher
- **RAM:** 256MB minimum
- **Internet:** Required
- **Privileges:** Sudo access needed for Tor service

## Author 👨‍💻

Created by **Neo**

## Credits 🙏

- Original concept: mrFD
- Tor Project: https://www.torproject.org/
- Python Community

## License 📄

MIT License - See LICENSE file for details

## Contributing 🤝

Found a bug? Have suggestions? Feel free to:
- Open an issue
- Submit improvements
- Share feedback

## Educational Purpose 📚

This tool is designed for:
- Learning network security concepts
- Understanding proxy systems
- Research on anonymity
- Cybersecurity education
- Privacy protection techniques

## Legal Notice ⚖️

This tool comes "as-is" without warranties. Users are responsible for:
- Compliance with local laws
- Ethical use of the tool
- All consequences of using this tool

**Do not use for:**
- Illegal activities
- Unauthorized access
- DDoS attacks
- Fraud or scams
- Harassment

---

**Stay Safe & Respect Privacy! 🛡️**

**For support:** Create an issue on GitHub
