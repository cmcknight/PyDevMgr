import sys
import os
import yaml
import wx
from ObjectListView import ObjectListView, ColumnDefn

class TaskObject():
    def __init__(self):
        self.task_name = ''
        self.description = ''
        self.command = ''
        self.invoked = 0;

    def __init__(self, dict):
        self.task_name = dict['task_name']
        self.description = dict['description']
        self.command = dict['command']
        self.invoked = dict['invoked']

class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.tasks = []
        
        # set up the main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.tasksOlv = ObjectListView(self, style=wx.LC_REPORT | wx.SUNKEN_BORDER, useAlternateBackColors=False,typingSearchesSortColumn=False)
        self.tasksOlv.SetColumns([ColumnDefn('Task', 'left', -1, 'task_name', isSpaceFilling=True, isEditable=False, isSearchable=False)])
        self.load_tasks()
        self.tasksOlv.SetObjects(self.tasks)
        self.tasksOlv.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.__item_activated)


        # idx = 0
        # index = self.list.InsertItem(idx, 'Appl 1')
        main_sizer.Add(self.tasksOlv, 1, wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT, 10)

        row_sizer = wx.BoxSizer()
        self.addButton = wx.Button(self, wx.ID_ANY, size=(32,32), label="+")
        self.addButton.Bind(wx.EVT_BUTTON, self.__add_new_task)
        row_sizer.Add(self.addButton, 0, wx.ALIGN_LEFT | wx.LEFT, 10)
        self.editButton = wx.Button(self, wx.ID_ANY, size=(48,32), label="Edit")
        self.editButton.Bind(wx.EVT_BUTTON, self.__edit_task)
        row_sizer.Add(self.editButton, 0, wx.ALIGN_LEFT)
        self.deleteButton = wx.Button(self, wx.ID_ANY, size=(32,32), label="-")
        self.deleteButton.Bind(wx.EVT_BUTTON, self.__delete_task)
        row_sizer.Add(self.deleteButton, 0, wx.ALIGN_LEFT)
        main_sizer.Add(row_sizer, 0, wx.ALIGN_LEFT)

        row_sizer = wx.BoxSizer()
        self.btn_close = wx.Button(self, wx.ID_EXIT, label="Close")
        self.btn_close.Bind(wx.EVT_BUTTON, self.__on_close)
        row_sizer.Add(self.btn_close, 0, 0)
        self.launchButton = wx.Button(self, wx.ID_ANY, label="Launch")
        self.launchButton.Bind(wx.EVT_BUTTON, self.__launch_script)
        row_sizer.Add(self.launchButton, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT, 10)
        main_sizer.Add(row_sizer, 0, wx.ALIGN_RIGHT)

        self.SetSizer(main_sizer)

    def load_tasks(self):
        filename = sys.path[0] + '/pylaunch.cfg'
        if (os.path.exists(filename)):
            # config file exists, load tasks
            with open(filename, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                if data['Tasks'] != None:
                    # load the list of task objects
                    for task in data['Tasks']:
                        self.tasks.append(TaskObject(task))
                    # Sort by frequency of invocation
                    self.tasks.sort(key=lambda task: task.invoked, reverse=True)

        else:
            # open file for writing
            with open(filename, 'w') as f:
                f.write('# pylaunch.cfg\n\nTasks:\n')


    # Event Handlers
    def __add_new_task(self):
        pass

    def __delete_task(self):
        pass

    def __edit_task(self):
        pass

    def __launch_script(self):
        pass

    def __on_close(self, event):
        event.Skip()

    def __item_activated(self, event):
        print(f'Selected item: {self.tasksOlv.GetSelectedObject().__dict__}')

