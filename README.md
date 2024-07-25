Running the file will create plots automatically with available disk space and delete plots when more space is required. Below are the pre-requesites:
1. Follow the Chia installation guide at https://docs.chia.net/installation/ to install the Chia system on your software.
2. Verify the installation by running <chia --version>
3. Generate keys: 
    (a) <chia keys generate> will generate a new private key (24-word mnemonic seed); you should store this securely.
    (b) <chia keys add> will prompt you to enter your key 
    (c) <chia keys show> will display detailed public and private information on the keys
4. Start the Chia services using <chia start farmer>
5. Check for available disk space and edit the PLOT_SIZE and MIN_FREE_SPACE variables to accomodate, if necessary. The minimum for MIN_FREE_SPACE is 20 x ...
6. Run the manage_plots.py script


Trouble-shooting:
1. You can manually check for the creation of a plot using <chia plots create -k 32 -n 1 -t /path/to/temp/directory -d /path/to/plot/directory>
2. Verify that the script correctly points to the Chia CLI and that all necessary configurations (like keys and settings) are in place.
3. Monitor your system's CPU and RAM usage to ensure it's not being overwhelmed, which could slow down or stop the process.

    
