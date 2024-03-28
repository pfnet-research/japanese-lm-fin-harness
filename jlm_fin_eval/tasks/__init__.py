import os
from typing import Optional

from lm_eval.tasks import TaskManager as OriginalTaskManager


class TaskManager(OriginalTaskManager):
    """TaskManager indexes all tasks from the default `lm_eval/tasks/`
    and an optional directory if provided.

    """

    def initialize_tasks(self, include_path: Optional[str] = None) -> dict:
        """Creates a dictionary of tasks index.

        :param include_path: str = None
            An additional path to be searched for tasks

        :return
            Dictionary of task names as key and task metadata
        """
        all_paths = [os.path.dirname(os.path.abspath(__file__)) + "/"]
        if include_path is not None:
            if isinstance(include_path, str):
                include_path = [include_path]
            all_paths.extend(include_path)

        task_index = {}
        for task_dir in all_paths:
            tasks = self._get_task_and_group(task_dir)
            task_index = {**tasks, **task_index}

        return task_index
