# PyDevMgr

PyDevMgr provides a desktop GUI for launching shell scripts and applications. The launch parameters are stored in a YAML file in the application directory. This project uses the wxPython library to provide cross-platform support.

The PyDevMgr displays the names of the tasks, sorted in a descending order based on the number of times the task has been invoked.

## Requirements

This project was built using Python 3.8.6 and the following libraries:


| Library | Version |
| ------- | ------- |
| numpy   | ==1.19.4 |
| ObjectListView | ==1.3.1 |
| Pillow | ==8.0.1 |
| PyYAML | ==5.3.1 |
| six | ==1.15.0 |
| wxPython | ==4.1.1 |

## Notes

Having just updated to Mac Big Sur and Python 3.9, I am saddened to see that pyinstaller is currently non-functional due to Apple changing where/how some of the necessary system libraries are stored. As soon as that issue gets resolved, I will create distribution packages.

## ToDos

[ ] Add accelerators for keyboard shortcuts
[ ] Create iconset
[ ] Package application for Linux, Windows, Max OS
[ ] Add binding to handle application minimization
[ ] Add binding to handle application restoration from being minimized
[ ] Ensure that application does not maximize