class Job():
    """this class represents a job"""

    def __init__(self, job_config):
        # The friendly name of the job. It is used in log and telegram messages.
        self.name = job_config['name']
        # The category of the job. It used to categories the jobs e.g. backup, update ...
        self.category = job_config['category']
        # This job will be queued if another job of this group is running.
        # The execution will be started if all allready queued jobs are finished.
        self.blocking_group = job_config['blocking_group']
        # Member of this groups get all information messages from the job.
        self.information_groups = job_config['information_groups']
        # Member of this groups can manuel execute this job.
        self.execution_groups = job_config['execution_groups']
        # The command that should be executed 
        self.execution_command_command = job_config['execution_command']['command']        
        self.execution_command_parameter = job_config['execution_command']['parameter']
        # The logfile location of the command. Used to send the log to the user
        self.execution_command_logfile = job_config['execution_command']['logfile']
        self.cfg = job_config

        # last time the job started
        self.start_time = None
        # last time the job finished
        self.stop_time = None
        # last duration
        self.last_duration = 0        
        # last exit status
        self.finished_successfully = True

    def is_active(self):
        if self.start_time > self.stop_time:
            return True
        return False
        

