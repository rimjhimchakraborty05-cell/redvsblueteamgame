import time
import base64
import os
import subprocess
from utils import execute_command

class Challenges:
    def __init__(self):
        self.max_attempts = 3
        self.hint_used = False
        self.challenges = {}

    def run_level(self, level):
        start_time = time.time()
        attempts = 0
        self.hint_used = False

        while attempts < self.max_attempts:
            attempts += 1
            success = self._execute_level(level)

            if success:
                time_taken = time.time() - start_time
                score = self._calculate_score(time_taken, attempts)
                return True, score

            print(f"\n❌ Incorrect answer. Attempts remaining: {self.max_attempts - attempts}")
            if attempts < self.max_attempts and not self.hint_used:
                try:
                    choice = input("\nWould you like a hint? (y/n): ").strip().lower()
                    if choice == 'y':
                        self.hint_used = True
                        hint_text = self._get_hint(level)
                        print(f"\n💡 Hint: {hint_text}")
                        print("Note: Using hint reduces score by 25 points!")
                except (KeyboardInterrupt, EOFError):
                    print("\nLevel cancelled.")
                    return False, 0

        return False, 0

    def _get_hint(self, level):
        if hasattr(self, 'challenges') and level in self.challenges:
            return self.challenges[level].get('hint', 'No hint available.')
        return 'No hint available.'

    def _calculate_score(self, time_taken, attempts):
        base_score = 100
        time_penalty = min(int(time_taken / 10), 50)
        attempt_penalty = (attempts - 1) * 10
        hint_penalty = 25 if self.hint_used else 0
        final_score = base_score - time_penalty - attempt_penalty - hint_penalty
        return max(final_score, 10)

    def _show_help(self):
        print("\n" + "=" * 50)
        print("                AVAILABLE COMMANDS                ")
        print("=" * 50)
        print("  submit       : Submit your answer to complete challenge")
        print("  hint         : Show the level hint (-25 points on 1st use)")
        print("  help         : Display this command reference")
        print("  exit / quit  : Exit the game safely")
        print("\nUseful Terminal Commands:")
        print("  dir (Windows) / ls (Linux)     : View directory files")
        print("  dir /a:h (Windows) / ls -la    : View hidden files")
        print("  type <file> (Win) / cat <file> : Read file contents")
        print("  findstr <text> <file> / grep   : Search in files")
        print("=" * 50)

    def _setup_challenge(self, challenge):
        try:
            if 'file' in challenge and 'content' in challenge:
                with open(challenge['file'], 'w', encoding='utf-8') as f:
                    f.write(challenge['content'])
                if challenge.get('hidden') and os.name == 'nt':
                    subprocess.run(f'attrib +h "{challenge["file"]}"', shell=True, capture_output=True)
            elif 'setup' in challenge:
                os.system(challenge['setup'])
            return True
        except Exception as e:
            print(f"Setup error: {e}")
            return False

class RedTeamChallenges(Challenges):
    def __init__(self):
        super().__init__()
        self.challenges = {
            0: {
                "title": "Find Hidden System Files",
                "description": "Find the hidden system configuration file that starts with '.sys'",
                "hint": "Use 'dir /a:h' in Windows or 'ls -la' in Linux",
                "answer": ".sysconfig",
                "file": ".sysconfig",
                "content": "DB_PASSWORD=secret123\n",
                "hidden": True,
                "setup": "echo 'DB_PASSWORD=secret123' > .sysconfig"
            },
            1: {
                "title": "Decode Base64 Credentials",
                "description": "Decode: QWRtaW5AMTIzNDU=",
                "hint": "Use: certutil -decode or base64 -d",
                "answer": "Admin@12345",
                "file": "encoded_creds.txt",
                "content": "QWRtaW5AMTIzNDU=\n",
                "setup": "echo 'QWRtaW5AMTIzNDU=' > encoded_creds.txt"
            },
            2: {
                "title": "Web Server Config",
                "description": "Find the admin password in apache2.conf",
                "hint": "Search for 'AdminPass' in the config",
                "answer": "AdminPass: SuperSecret2023!",
                "file": "apache2.conf",
                "content": "AdminPass: SuperSecret2023!\n",
                "setup": "echo 'AdminPass: SuperSecret2023!' > apache2.conf"
            },
            3: {
                "title": "Password Hash",
                "description": "Find the MD5 hash in shadow.bak",
                "hint": "Check backup files for hashed passwords",
                "answer": "5f4dcc3b5aa765d61d8327deb882cf99",
                "file": "shadow.bak",
                "content": "5f4dcc3b5aa765d61d8327deb882cf99\n",
                "setup": "echo '5f4dcc3b5aa765d61d8327deb882cf99' > shadow.bak"
            },
            4: {
                "title": "SQL Injection",
                "description": "Find vulnerable login request in access.log",
                "hint": "Look for SQL injection patterns",
                "answer": "admin' --",
                "file": "access.log",
                "content": "GET /login.php?user=admin%27+--&pass=test\n",
                "setup": "echo 'GET /login.php?user=admin%27+--&pass=test' > access.log"
            }
        }

    def _execute_level(self, level):
        if level not in range(5):
            print("Invalid level!")
            return False

        challenge = self.challenges[level]
        print(f"\n🔴 Level {level}: {challenge['title']}")
        print(f"Task: {challenge['description']}")

        if not self._setup_challenge(challenge):
            return False

        while True:
            try:
                user_input = input("\nEnter command (or 'submit' to answer, 'hint' for hint, 'help' for commands): ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nLevel interrupted.")
                return False

            if not user_input:
                continue

            cmd_lower = user_input.lower()
            if cmd_lower == 'submit':
                try:
                    answer = input("Enter your answer: ").strip()
                except (KeyboardInterrupt, EOFError):
                    return False
                return answer == challenge['answer']
            elif cmd_lower == 'hint':
                if not self.hint_used:
                    self.hint_used = True
                    print(f"\n💡 Hint: {challenge['hint']}")
                    print("Note: Using hint reduces score by 25 points!")
                else:
                    print(f"\n💡 Hint (already revealed): {challenge['hint']}")
            elif cmd_lower == 'help':
                self._show_help()
            else:
                # Pass current directory as base_dir to sandbox execution
                output = execute_command(user_input, base_dir=os.getcwd())
                print("\nCommand Output:")
                print("-" * 50)
                print(output)
                print("-" * 50)

class BlueTeamChallenges(Challenges):
    def __init__(self):
        super().__init__()
        self.challenges = {
            0: {
                "title": "Detect Malware Signature",
                "description": "Find malicious process signature in syslog",
                "hint": "Check for known malware patterns",
                "answer": "MALWARE-CNC Trojan.Kovter variant outbound connection",
                "file": "syslog",
                "content": "[Alert] MALWARE-CNC Trojan.Kovter variant outbound connection detected\n",
                "setup": "echo '[Alert] MALWARE-CNC Trojan.Kovter variant outbound connection detected' > syslog"
            },
            1: {
                "title": "Failed Login Analysis",
                "description": "Find IP with most failed SSH attempts",
                "hint": "Check auth.log for repeated failures",
                "answer": "198.51.100.123",
                "file": "auth.log",
                "content": "Failed SSH login from 198.51.100.123 - 50 attempts\n",
                "setup": "echo 'Failed SSH login from 198.51.100.123 - 50 attempts' > auth.log"
            },
            2: {
                "title": "Firewall Configuration",
                "description": "Find open ports in firewall config",
                "hint": "Check netstat or firewall rules",
                "answer": "PORT 3389 (RDP) EXPOSED",
                "file": "firewall.conf",
                "content": "PORT 3389 (RDP) EXPOSED - External Access Allowed\n",
                "setup": "echo 'PORT 3389 (RDP) EXPOSED - External Access Allowed' > firewall.conf"
            },
            3: {
                "title": "Critical Updates",
                "description": "Find CVE of pending critical update",
                "hint": "Check Windows Update or apt logs",
                "answer": "CVE-2023-1234",
                "file": "updates.log",
                "content": "Critical Update Required: CVE-2023-1234 - Remote Code Execution\n",
                "setup": "echo 'Critical Update Required: CVE-2023-1234 - Remote Code Execution' > updates.log"
            },
            4: {
                "title": "Network Intrusion",
                "description": "Find suspicious data exfiltration",
                "hint": "Check network traffic logs",
                "answer": "Large outbound transfer to 203.0.113.100:4444",
                "file": "nids.log",
                "content": "Alert: Large outbound transfer to 203.0.113.100:4444 - 2GB data\n",
                "setup": "echo 'Alert: Large outbound transfer to 203.0.113.100:4444 - 2GB data' > nids.log"
            }
        }

    def _execute_level(self, level):
        if level not in range(5):
            print("Invalid level!")
            return False

        challenge = self.challenges[level]
        print(f"\n🔵 Level {level}: {challenge['title']}")
        print(f"Task: {challenge['description']}")

        if not self._setup_challenge(challenge):
            return False

        while True:
            try:
                user_input = input("\nEnter command (or 'submit' to answer, 'hint' for hint, 'help' for commands): ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nLevel interrupted.")
                return False

            if not user_input:
                continue

            cmd_lower = user_input.lower()
            if cmd_lower == 'submit':
                try:
                    answer = input("Enter your answer: ").strip()
                except (KeyboardInterrupt, EOFError):
                    return False
                return answer == challenge['answer']
            elif cmd_lower == 'hint':
                if not self.hint_used:
                    self.hint_used = True
                    print(f"\n💡 Hint: {challenge['hint']}")
                    print("Note: Using hint reduces score by 25 points!")
                else:
                    print(f"\n💡 Hint (already revealed): {challenge['hint']}")
            elif cmd_lower == 'help':
                self._show_help()
            else:
                # Pass current directory as base_dir to sandbox execution
                output = execute_command(user_input, base_dir=os.getcwd())
                print("\nCommand Output:")
                print("-" * 50)
                print(output)
                print("-" * 50)