import wx

class EditorDialog(wx.Dialog):
    """
    The EditorDialog class provides the capability of adding new
    tasks or editing the properties of existing tasks.
    """
    def __init__(self, task, addFlag=False):
        """
        Constructor

        :param task: object to be edited; empty values if being added
        :type task: TaskObject
        :param addFlag: Deteremines whether this is an add or edit operaation
        :type addFlag: Boolean
        """
        title = 'Add Task' if addFlag else 'Edit Task'
        super().__init__(None, title=title)

        # save the original values
        self.task = task

        # copy task values to 'local' storage
        self.task_name = task.task_name
        self.description = task.description
        self.command = task.command
        self.invoked = task.invoked

        self.SetTitle(title)
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # add the controls
        lbl = wx.StaticText(self, label='Task Name:')
        lbl.SetFont(font)
        self.txt_task_name = wx.TextCtrl(self, wx.ID_ANY, value=self.task_name, size=(300,-1))
        main_sizer.Add(self.__row_builder([lbl, self.txt_task_name]), 0, wx.EXPAND | wx.ALL, 10)

        lbl = wx.StaticText(self, label='Description:')
        lbl.SetFont(font)
        self.txt_description = wx.TextCtrl(self, wx.ID_ANY, value=self.description)
        main_sizer.Add(self.__row_builder([lbl, self.txt_description]), 0, wx.EXPAND | wx.ALL, 10)

        lbl = wx.StaticText(self, label='Command:')
        lbl.SetFont(font)
        self.txt_command = wx.TextCtrl(self, wx.ID_ANY, value=self.command)
        main_sizer.Add(self.__row_builder([lbl, self.txt_command]), 0, wx.EXPAND | wx.ALL, 10)

        lbl = wx.StaticText(self, label='Times Invoked')
        lbl.SetFont(font)
        self.spinctl_invoked = wx.SpinCtrl(self, wx.ID_ANY, value=str(self.invoked))
        main_sizer.Add(self.__row_builder([lbl, self.spinctl_invoked]), 0, wx.ALL, 10)

        # add the buttons
        btn_sizer = wx.BoxSizer()
        btn_ok = wx.Button(self, label="Save")
        btn_ok.Bind(wx.EVT_BUTTON, self.__save)
        btn_sizer.Add(btn_ok, 0, wx.CENTER, 5)

        btn_cancel = wx.Button(self, label="Cancel")
        btn_cancel.Bind(wx.EVT_BUTTON, self.__cancel)
        btn_sizer.Add(btn_cancel, 0, wx.CENTER, 5)
        main_sizer.Add(btn_sizer, 0, wx.CENTER | wx.ALL, 10)

        self.SetSizerAndFit(main_sizer)

    def __save(self, event):
        """
        Save the changes

        :param event: wxPython event object
        :type event: wxEvent
        :return: None
        :rtype: N/A
        """
        self.EndModal(True)
        self.task.task_name = self.txt_task_name.GetValue()
        self.task.description = self.txt_description.GetValue()
        self.task.command = self.txt_command.GetValue()
        self.task.invoked = int(self.spinctl_invoked.GetValue())
        self.Close()

    def __cancel(self, event):
        """
        Cancel any edits, close dialog

        :param event: wxPython event
        :type event: wxEvent
        :return: None
        :rtype: N/A
        """
        self.Close()

    def __row_builder(self, widgets):
        """
        Row builder helper method

        :param widgets: list of wxPython widgets
        :type widgets:
        :return: sizer
        :rtype: wxSizer
        """
        sizer = wx.BoxSizer(wx.VERTICAL)
        lbl, txt = widgets
        sizer.Add(lbl, 0, wx.BOTTOM, 5)
        sizer.Add(txt, 1, wx.EXPAND, 5)
        return sizer