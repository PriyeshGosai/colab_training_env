def clone_colab_sheet(repository):
    """
    Clone a GitHub repository into your Google Drive (MyDrive) in Google Colab.

    If the repository already exists in your MyDrive, the function will back it up
    by renaming it with a timestamp before cloning a fresh copy.

    After cloning, a message will be displayed with instructions on how to locate
    the folder via drive.google.com.

    Parameters:
    -----------
    repository : str
        The full HTTPS GitHub repository URL. 
        Example: 'https://github.com/Username/YourRepo'

    Usage:
    ------
    clone_colab_sheet('https://github.com/Username/YourRepo')

    Notes:
    ------
    - Must be run in a Google Colab environment.
    - Requires Google Drive access (handled automatically).
    - Clones into /content/drive/MyDrive/<repo_name>
    """
    
    # Check if running in Google Colab
    try:
        import google.colab
    except ImportError:
        raise EnvironmentError("❌ This function must be run in a Google Colab environment.")
    
    from google.colab import drive
    import os
    import subprocess
    import shutil
    from datetime import datetime
    from IPython.display import display, Markdown

    # Extract repo name from URL
    repo_name = repository.rstrip('/').split('/')[-1]

    # Mount Google Drive
    drive.mount('/content/drive')

    # Set paths
    base_dir = '/content/drive/MyDrive'
    repo_path = os.path.join(base_dir, repo_name)
    os.chdir(base_dir)

    # Backup existing repo if it exists
    if os.path.exists(repo_path):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_dir = f"{repo_name}_backup_{timestamp}"
        backup_path = os.path.join(base_dir, backup_dir)

        print(f"⚠️ Repository '{repo_name}' already exists. Backing up to '{backup_dir}' before overwriting...")
        shutil.move(repo_path, backup_path)

    # Clone fresh copy of the repository
    print(f"⬇️ Cloning repository '{repo_name}'...")
    subprocess.run(['git', 'clone', repository])

    # Change directory to the repo
    os.chdir(repo_path)

    # Display message with instructions
    display(Markdown(f"""
✅ **Repository '{repo_name}' has been cloned successfully.**  
📁 To access the files, go to [**drive.google.com**](https://drive.google.com), open **My Drive**, and look for the folder named **`{repo_name}`**.
    """))
