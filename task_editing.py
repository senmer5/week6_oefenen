from task_management import TaskManagement
from task import Task
from datetime import datetime

"""
TaskEditing sınıfı, bir görev üzerinde düzenleme işlemleri yapmayı sağlayan bir sınıftır. 
Bu sınıf, görevlerin durumunu (status), önceliğini (priority), son tarihini (deadline) güncellemeyi 
ve görevi tamamlanmış olarak işaretlemeyi amaçlayan metotlar içerir. 
TaskEditing sınıfı, görevlerle ilgili bu düzenlemeleri yapmak için TaskManagement sınıfından 
görev bilgilerine erişir
"""


class TaskEditing:
    def __init__(self, task_management: TaskManagement):
        self.task_management = task_management

        """
        Bu metod, TaskEditing sınıfının bir örneği (instance) oluşturulduğunda çalışır.
	    task_management parametresi, TaskManagement sınıfına ait bir nesne alır. 
        Bu nesne, görevlerin bulunduğu listeyi yönetir.
	    self.task_management özelliği, TaskManagement sınıfının nesnesine bağlanır. 
        Bu sayede TaskEditing sınıfı, görevlerle ilgili işlemleri bu sınıf aracılığıyla yapabilir.
        """

    def set_task_status(self, task_id: int, status: str) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status
            print(f"Task {task_id} status updated to '{status}'.")
        """
        Bu metod, verilen task_id’ye göre görevin status (durum) bilgisini günceller.
	    get_task_by_id metodu, görev listesindeki görevleri bulur. 
        Eğer görev bulunursa, görev durumu status ile güncellenir ve ekrana yazdırılır.
        """

    def set_prioritization(self, task_id: int, priority: str) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority
            print(f"Task {task_id} priority updated to '{priority}'.")
        """
        Bu metod, verilen task_id’ye göre görevin priority (öncelik) bilgisini günceller.
	    get_task_by_id ile görev bulunur ve ardından priority (öncelik) bilgisi güncellenir. 
        Sonrasında yeni öncelik ekrana yazdırılır.
        """

    def set_new_date(self, task_id: int, deadline: datetime) -> None:
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = deadline
            print(f"Task {task_id} deadline updated to {deadline}.")
        """
        Bu metod, verilen task_id’ye göre görevin deadline (son tarih) bilgisini günceller.
	    get_task_by_id ile görev bulunur ve son tarih deadline ile güncellenir. 
        Sonrasında yeni tarih ekrana yazdırılır.
        """

    def mark_status_completed(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task.status = "Completed"
            print(f"Task {task_id} marked as completed.")
            return True
        return False

    def get_task_by_id(self, task_id: int) -> Task:
        return self.task_management.get_task_by_id(task_id)