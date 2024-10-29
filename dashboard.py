import curses
import psutil
import time
from datetime import datetime

def draw_dashboard(stdscr):
    # Initialize the screen and disable cursor
    curses.curs_set(0)
    stdscr.nodelay(1)  # Make getch() non-blocking
    stdscr.timeout(1000)  # Refresh every 1 second

    while True:
        stdscr.clear()  # Clear the screen on every refresh

        # Get system stats
        cpu_usage = psutil.cpu_percent(interval=1)
        mem_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        net_info = psutil.net_io_counters()

        # Display Title and Timestamp
        stdscr.addstr(0, 2, "SYSTEM RESOURCE USAGE DASHBOARD", curses.A_BOLD)
        stdscr.addstr(1, 2, f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # CPU Usage
        stdscr.addstr(3, 2, f"CPU Usage: {cpu_usage}%")

        # Memory Usage
        stdscr.addstr(5, 2, f"Memory Usage: {mem_info.percent}%")
        stdscr.addstr(6, 4, f"Total: {mem_info.total // (1024 ** 2)} MB")
        stdscr.addstr(7, 4, f"Used: {mem_info.used // (1024 ** 2)} MB")
        stdscr.addstr(8, 4, f"Free: {mem_info.available // (1024 ** 2)} MB")

        # Disk Usage
        stdscr.addstr(10, 2, f"Disk Usage: {disk_info.percent}%")
        stdscr.addstr(11, 4, f"Total: {disk_info.total // (1024 ** 3)} GB")
        stdscr.addstr(12, 4, f"Used: {disk_info.used // (1024 ** 3)} GB")
        stdscr.addstr(13, 4, f"Free: {disk_info.free // (1024 ** 3)} GB")

        # Network Statistics
        stdscr.addstr(15, 2, "Network Statistics:")
        stdscr.addstr(16, 4, f"Bytes Sent: {net_info.bytes_sent // (1024 ** 2)} MB")
        stdscr.addstr(17, 4, f"Bytes Received: {net_info.bytes_recv // (1024 ** 2)} MB")

        # Instructions
        stdscr.addstr(19, 2, "Press 'q' to quit or 's' to save the report to a file.", curses.A_BOLD)

        # Handle user input
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('s'):
            save_report(cpu_usage, mem_info, disk_info, net_info)

        stdscr.refresh()
        time.sleep(1)  # Pause for 1 second before next update

def save_report(cpu, mem, disk, net):
    """Save the current resource usage to a text file."""
    with open("system_report.txt", "a") as f:
        f.write(f"Report at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"CPU Usage: {cpu}%\n")
        f.write(f"Memory Usage: {mem.percent}%\n")
        f.write(f"Disk Usage: {disk.percent}%\n")
        f.write(f"Network - Bytes Sent: {net.bytes_sent // (1024 ** 2)} MB, ")
        f.write(f"Bytes Received: {net.bytes_recv // (1024 ** 2)} MB\n")
        f.write("-" * 40 + "\n")
    print("Report saved to system_report.txt")

if __name__ == "__main__":
    curses.wrapper(draw_dashboard)
