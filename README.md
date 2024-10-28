# SharePoint Project Connect

## Overview

This project is a Python-based application designed to connect to a SharePoint site and manage lists and items within it. Through a simple graphical interface built with Tkinter, users can perform various operations on SharePoint lists, such as creating and deleting lists, adding items, and managing list columns.

## Features

- **Connect to SharePoint**: Secure authentication with a SharePoint site using the provided credentials.
- **Manage Lists**:
  - Create new lists
  - List all existing lists
  - Delete selected lists
- **Manage Items**:
  - Add new items to specific lists
  - Retrieve and display existing items
- **Manage Columns**:
  - Add custom columns to lists

## Installation

To run this project, you need Python 3 installed on your machine. Install the required dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the menu.py file to start the application:
```bash
python menu.py
```

2. In the application window:

Enter your SharePoint domain, site name, username, and password.
Click Connect to SharePoint to establish the connection.
Use the provided menu options to perform actions on SharePoint lists and items.

## File Structure

- sharepoint_connector.py: Handles connection to the SharePoint site.
- operations/: Contains individual modules for operations like adding items, managing lists, and adding columns.
- menu.py: The main Tkinter GUI that provides the user interface.

