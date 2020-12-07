# pylaunch Use Cases

## Overview

This document contains the use cases for the pylaunch application.

## Use Cases

### Application Start Up

When the application starts up, it will check for its data file. If the data file is present, then its data will be loaded into an internal data structure. The datagrid in the scroll window will be loaded from this data if there is any to be loaded. The use case ends when the data has been loaded and the data displayed in the datagrid.

### Application Shut Down

The use case begins when the user clicks the __close__ button on the main window. The application updates the data file from the internal data structure to ensure that the data file represents the most current state of the data. The use case ends when the data has been completely written to persistent storage and the application shuts down.

### Launch Managed Application

The use case begins when the user selects a managed application from the scroll window and either clicks the __launch__ button or double-clicks the entry in the scroll window. The application will open a child shell and execute the command associated with the managed application. The use case ends when the managed application has been launched.

### Add New Managed Application

The use case begins when the user clicks the '+' button. The Add New Application dialog will be displayed for the user to enter the parameters associated with the new managed application. When the user has completed the data entry, the user can save the data by clicking the __save__ button or discard the data by clicking the __cancel__ button. After the user clicks the button, the dialog will close and the scroll window data will be updated. The use case ends when the dialog closes.

### Delete Managed Application

The use case begins when the user clicks the '-' button. The application will display a confirmation dialog to ensure the user wishes to continue with the deletion. After the user confirms or discards the deletion, the dialog will close and the use case ends.