import os
import sys
import time
import subprocess
from datetime import datetime

# Configure standard streams for UTF-8 encoding safely
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from banner import show_banner
from challenge import RedTeamChallenges, BlueTeamChallenges
from utils import choose_team, execute_command

def clean_directory(dir_path):
    """Safely cleans up all files inside the specified challenge directory."""
    if not os.path.exists(dir_path):
        return
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            try:
                if os.name == 'nt':
                    subprocess.run(f'attrib -h "{item_path}"', shell=True, capture_output=True)
                os.remove(item_path)
            except Exception:
                pass

def main():
    game_root = os.path.dirname(os.path.abspath(__file__))
    challenge_dir = os.path.join(game_root, "challenge_files")

    try:
        show_banner()
        team = choose_team()
        level = 0
        total_score = 0
        start_time = datetime.now()

        # Create isolated challenge environment directory
        if not os.path.exists(challenge_dir):
            os.makedirs(challenge_dir)
        os.chdir(challenge_dir)

        print(f"\n{team} Team Selected - Game Starting!")
        print("Each level has 3 attempts. Time and attempts affect your score.")
        print("Type 'help' for available commands, or 'exit' to quit.")
        time.sleep(1.5)

        challenges = RedTeamChallenges() if team == "Red" else BlueTeamChallenges()

        while level < 5:
            print(f"\n=== Level {level} ===")
            
            # Ensure working directory is strictly the challenge sandbox
            os.chdir(challenge_dir)
            clean_directory(challenge_dir)

            success, score = challenges.run_level(level)

            if success:
                total_score += score
                print(f"\n✅ Level Cleared! Score: {score} points")
                print(f"Total Score: {total_score}")
                level += 1
            else:
                print("\n❌ Level failed. Restarting level...")
                time.sleep(1)

        total_time = (datetime.now() - start_time).total_seconds()
        print(f"\n🎉 Congratulations! {team} Team has completed all levels! 🎉")
        print(f"Total Score: {total_score}")
        print(f"Total Time: {total_time:.1f} seconds")

    except (KeyboardInterrupt, SystemExit):
        print("\nGame session ended. Cleaning up and exiting...")
    finally:
        # Guarantee cleanup back to game root
        try:
            os.chdir(game_root)
            clean_directory(challenge_dir)
            if os.path.exists(challenge_dir):
                os.rmdir(challenge_dir)
        except Exception:
            pass

if __name__ == "__main__":
    main()