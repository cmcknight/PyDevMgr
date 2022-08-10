import os
import sys

import wx
import yaml
from ObjectListView import ObjectListView, ColumnDefn

from EditorDialog import EditorDialog
from TaskObject import TaskObject


class MainPanel(wx.Panel):
    """
    The MainPanel class contains the controls and related logic
    for the PyDevMgr application.
    """


    def __init__(self, parent):
        """
        Class constructor
        """
        super().__init__(parent)
        self.parent = parent
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.cfg_filename = sys.path[0] + '/pydevmgr.cfg'
        self.tasks = []
        self.__load_tasks()

        # set up the main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # set up the ObjectListView control
        self.olv_tasks = ObjectListView(self, style=wx.LC_REPORT | wx.SUNKEN_BORDER,
                                        useAlternateBackColors=False,
                                        typingSearchesSortColumn=False)
        self.olv_tasks.SetColumns([ColumnDefn('Task', 'left', -1, 'task_name',
                                              isSpaceFilling=True, isEditable=False,
                                              isSearchable=False, minimumWidth=300)])
        self.olv_tasks.SetObjects(self.tasks)
        self.olv_tasks.SetFont(font)
        main_sizer.Add(self.olv_tasks, 1, wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT, 10)

        # ObjectListView control event handlers
        self.olv_tasks.Bind(wx.EVT_KEY_DOWN, self.__on_olv_keydown)
        self.olv_tasks.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.__launch_command)
        self.olv_tasks.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.__unselect_item)
        self.olv_tasks.Bind(wx.EVT_LIST_ITEM_SELECTED, self.__select_item)

        # add the CRUD buttons
        row_sizer = wx.BoxSizer()
        self.btn_add = wx.Button(self, wx.ID_ANY, size=(32, 32), label="+")
        self.btn_add.Bind(wx.EVT_BUTTON, self.__add_new_task)
        row_sizer.Add(self.btn_add, 0, wx.ALIGN_LEFT | wx.LEFT, 10)

        self.btn_edit = wx.Button(self, wx.ID_ANY, size=(48, 32), label="Edit")
        self.btn_edit.Bind(wx.EVT_BUTTON, self.__edit_task)
        self.btn_edit.Disable()
        row_sizer.Add(self.btn_edit, 0, wx.ALIGN_LEFT)

        self.btn_delete = wx.Button(self, wx.ID_ANY, size=(32, 32), label="-")
        self.btn_delete.Bind(wx.EVT_BUTTON, self.__delete_task)
        self.btn_delete.Disable()
        row_sizer.Add(self.btn_delete, 0, wx.ALIGN_LEFT)
        main_sizer.Add(row_sizer, 0, wx.ALIGN_LEFT)

        # add the operational buttons
        row_sizer = wx.BoxSizer()
        self.btn_close = wx.Button(self, wx.ID_EXIT, label="Close")
        self.btn_close.Bind(wx.EVT_BUTTON, self.__on_close)
        row_sizer.Add(self.btn_close, 0, 0)

        self.btn_launch = wx.Button(self, wx.ID_ANY, label="Launch")
        self.btn_launch.Bind(wx.EVT_BUTTON, self.__launch_command)
        row_sizer.Add(self.btn_launch, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT, 10)
        main_sizer.Add(row_sizer, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        self.Bind(wx.EVT_KEY_DOWN, self.__on_keydown)
        self.SetSizer(main_sizer)

    def __on_keydown(self, event):
        keycode = event.GetKeyCode()
        modifier = event.GetModifiers()
        if keycode == ord('Q') and modifier == wx.MOD_CONTROL:
            self.parent.Close()

    # Event Handlers
    def __add_new_task(self, event):
        """
        Add task to task object list
        """
        task = TaskObject()
        res, task = self.__call_add_edit_dialog(task, True)
        if res == 1:
            # add task object to tasks
            self.tasks.append(task)
            self.__save_tasks()

    def __delete_task(self, event):
        """
        Delete task from task object list
        """
        task = self.olv_tasks.GetSelectedObject()
        del self.tasks[self.tasks.index(task)]
        self.__save_tasks()

    def __edit_task(self, event):
        """
        Edit task in task object list
        """
        res, task = self.__call_add_edit_dialog(self.olv_tasks.GetSelectedObject(), False)
        if res == 1:
            # Refresh list
            self.__save_tasks()

    def __on_close(self, event):
        """
        Close application
        """
        event.Skip()


    def __launch_command(self, event):
        """
        Launch command from selected task object
        """
        task = self.olv_tasks.GetSelectedObject()
        if task.command != '' and task.command is not None:
            os.system(task.command)
        task.invoked += 1
        # save task data
        self.__save_tasks()
        self.olv_tasks.RefreshObjects(self.olv_tasks)

    def __on_olv_keydown(self, event):
        """
        Manage Enter key from ObjectListView control
        :param event:
        :type event:
        :return:
        :rtype:
        """
        keycode = event.GetKeyCode()
        if (keycode == 13):
            self.__launch_command(event)

    def __select_item(self, event):
        """
        Enable buttons when an object is selected
        """
        self.btn_edit.Enable()
        self.btn_delete.Enable()

    def __unselect_item(self, event):
        """
        Disable buttons when an object is unselected
        """
        self.btn_edit.Disable()
        self.btn_delete.Disable()

    # Helper methods
    def __call_add_edit_dialog(self, task, addFlag):
        """
        Invoke the editor dialog
        :param task: selected task object (if editing) or new task object
        :type task: TaskObject
        :param addFlag: Signal whether object is being editor or added
        :type addFlag: Boolean
        :return: res, task
        :rtype: integer, TaskObject
        """
        res = 0
        with EditorDialog(task, addFlag) as dlg:
            res = dlg.ShowModal()
        return res, dlg.task

    def __load_tasks(self):
        """
        Private method to load tasks from the configuration file
        """
        # does the file exist?
        if (os.path.exists(self.cfg_filename) == False):
            # no, create an empty file
            with open(self.cfg_filename, 'w') as f:
                f.write('# pydevmgr.cfg\n\n')
        else:
            # check for Tasks list
            with open(self.cfg_filename, 'r+') as f:
                d = f.read()
                f.seek(0, 0)

                # load task list
                tasks = yaml.load(f, Loader=yaml.FullLoader)
                if tasks != None:
                    # process the tasks into objects
                    for t in tasks:
                        task = TaskObject(task_name=t['task_name'],
                                          description=t['description'],
                                          command=t['command'],
                                          invoked=t['invoked'])
                        self.tasks.append(task)
                        self.tasks.sort(key=lambda item: item.invoked, reverse=True)
                else:
                    f.write('# pydevmgr.cfg\n\n')

    def __save_tasks(self):
        """
        Save the task objects to persistent storage
        """
        tasklist = []
        for t in self.tasks:
            tasklist.append(t.__dict__)
        with open(self.cfg_filename, 'w') as f:
            f.write('# pydevmgr.cfg\n\n')
            yaml.dump(tasklist, f, sort_keys=True)
        self.olv_tasks.SetObjects(self.tasks)
