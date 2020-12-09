class TaskObject():
    """
    The TaskObject contains the parameters associated with a task
    """
    def __init__(self, task_name='', description='', command='', invoked=0):
        """
        Constructor

        :param task_name: Name of the task
        :type task_name: String
        :param description: Description of the task
        :type description: String
        :param command: Command to execute
        :type command: String
        :param invoked: Number of times invoked
        :type invoked: Integer
        """
        self.task_name = task_name
        self.description = description
        self.command = command
        self.invoked = invoked


