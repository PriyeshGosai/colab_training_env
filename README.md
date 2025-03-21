# Clone GitHub Repository to Google Drive in Google Colab

This Colab utility function allows you to clone any public GitHub repository directly into your **Google Drive's MyDrive folder**. It is especially useful for Colab users who want to persist and interact with code from GitHub repositories across sessions.

## Features
- 📂 **Clones GitHub repos directly into Google Drive**
- 🔁 **Automatically backs up existing folders** with timestamped names
- 🔌 **Mounts Google Drive automatically** if not already mounted
- 📎 **Displays instructions** to access the cloned folder via [drive.google.com](https://drive.google.com)

## Suggested usage

A sample notebook named `clone_to_drive.ipynb` is provided in this repository. To use it:

1. Copy the notebook into your own training repository.
2. Update it with your repository URL and relevant details.
3. When sharing the training materials, direct users to this notebook and instruct them to run it once to complete the setup (clone the repository into their Google Drive).

This ensures users have the necessary files ready before starting the training.


## Function: `clone_colab_sheet(repository)`

### Description
Clones a GitHub repository into your Google Drive when working in Google Colab. If the target folder already exists, it is backed up before the new clone is downloaded, preventing accidental overwrites. After cloning, a message is displayed with instructions on how to locate the folder in Google Drive.

### Parameters
- `repository` *(str)*: The full HTTPS URL of the GitHub repository.

### Example Usage
```python
clone_colab_sheet('https://github.com/example_repository')
```

### Output
After running, the repository will be available at:
```
/content/drive/MyDrive/<repo_name>
```
And in Google Drive:
```
My Drive/<repo_name>
```

If a folder with the same name already exists, it will be backed up as:
```
My Drive/<repo_name>_backup_<timestamp>
```

### Requirements
This function is designed to run in **Google Colab** and assumes you have access to Google Drive via the Colab environment.

## Author
[Priyesh Gosai](https://github.com/PriyeshGosai)
