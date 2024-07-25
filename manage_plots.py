import os
import shutil
import subprocess
import time

# Configuration
PLOT_SIZE = 101.4 * 1024 * 1024 * 1024  # Size of a plot in bytes (101.4 GB)
MIN_FREE_SPACE = 20 * 1024 * 1024 * 1024  # Minimum free space to maintain in bytes (30 GB)
PLOT_DIR = "chia-plots"  # Final plot directory
TEMP_DIR = "chia-temp"  # Temporary plotting directory
DELAY_BETWEEN_CHECKS = 3600  # Time between checks in seconds (1 hour)

def get_free_space(directory):
    """Returns the free space in the specified directory in bytes."""
    total, used, free = shutil.disk_usage(directory)
    return free

def create_plot():
    """Creates a new Chia plot."""
    try:
        command = [
            "chia", "plots", "create",
            "-k", "32",  # Plot size (k=32 is standard)
            "-n", "1",  # Number of plots to create
            "-t", TEMP_DIR,  # Temporary directory
            "-d", PLOT_DIR  # Final directory
        ]
        print(f"Running command: {' '.join(command)}")
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            for line in proc.stdout:
                print(line, end='')
            for line in proc.stderr:
                print(f"Error: {line}", end='')
        if proc.returncode != 0:
            print(f"Plot creation failed with return code {proc.returncode}")
        else:
            print("Plot created successfully.")
    except Exception as e:
        print(f"Exception occurred while creating plot: {e}")

def delete_oldest_plot():
    """Deletes the oldest plot in the plot directory."""
    try:
        plots = [os.path.join(PLOT_DIR, f) for f in os.listdir(PLOT_DIR) if f.endswith(".plot")]
        if plots:
            oldest_plot = min(plots, key=os.path.getctime)
            print(f"Oldest plot to delete: {oldest_plot}")
            os.remove(oldest_plot)
            print(f"Deleted plot: {oldest_plot}")
        else:
            print("No plots found to delete.")
    except Exception as e:
        print(f"Exception occurred while deleting plot: {e}")

def manage_plots():
    while True:
        try:
            free_space = get_free_space(PLOT_DIR)
            print(f"Free space: {free_space / (1024 * 1024 * 1024):.2f} GB")

            if free_space >= PLOT_SIZE + MIN_FREE_SPACE:
                print("Creating new plot...")
                create_plot()
            elif free_space < MIN_FREE_SPACE:
                print("Free space below threshold. Deleting oldest plot...")
                delete_oldest_plot()
            else:
                print("No action needed.")

            time.sleep(DELAY_BETWEEN_CHECKS)
        except Exception as e:
            print(f"Exception occurred in manage_plots: {e}")

if __name__ == "__main__":
    manage_plots()
