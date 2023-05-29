import subprocess

# Replace with the path to your .tfl file
flow_path = r'C:/path/to/your/flow.tfl'

# Replace with the path to your prep-cli.bat file
prep_cli_path = r"C:\Program Files\Tableau\Tableau Prep Builder 2023.1\scripts\prep-cli.bat"

# Form the command
command = [prep_cli_path, '-t', flow_path]

# Run the command
subprocess.run(command, shell=True)
