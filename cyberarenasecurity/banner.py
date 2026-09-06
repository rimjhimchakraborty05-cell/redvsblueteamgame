import os
import sys

def show_banner():
    # Try reconfiguring stdout to utf-8 if supported
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

    unicode_banner = """
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗ ██████╗ ███████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████╗█████╗  ██║     
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗╚════██║██╔══╝  ██║     
╚██████╗   ██║   ██████╔╝███████╗██║  ██║███████║███████╗╚██████╗
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝
-----------------------------------------------------------
               WELCOME TO CYBERSEC ARENA
   A Cybersecurity Challenge Game for Hackers & Defenders!
-----------------------------------------------------------
"""

    ascii_banner = """
  ____ YBER  ____  ____  ____    _    ____  _____ _   _    _    
 / ___|     | __ )|  _ \|  _ \  / \  |  _ \| ____| \ | |  / \   
| |   _____ |  _ \| |_) | |_) |/ _ \ | |_) |  _| |  \| | / _ \  
| |__|_____|| |_) |  __/|  _ </ ___ \|  _ <| |___| |\  |/ ___ \ 
 \____|     |____/|_|   |_| \_\_/   \_\_| \_\_____|_| \_/_/   \_\
-----------------------------------------------------------
               WELCOME TO CYBERSEC ARENA
   A Cybersecurity Challenge Game for Hackers & Defenders!
-----------------------------------------------------------
"""

    os.system("cls" if os.name == "nt" else "clear")
    try:
        print(unicode_banner)
    except (UnicodeEncodeError, UnicodeError):
        print(ascii_banner)
