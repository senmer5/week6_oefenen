# TASK MANAGEMENT

from typing import List   # List türünü kullanabilmek için gerekli bir import işlemi yapar. 
from datetime import datetime
from task import Task  # Task sınıfını ve alt sınıflarını burada kullanacağız.

class TaskManagement:
    def __init__(self):
        self.task_list: List[Task] = []  
        
    def add_task(self, task: Task) -> None:
        """Yeni bir görev ekler."""
        self.task_list.append(task)
        print(f"Task '{task.task_name}' added successfully.")  


    def display_tasks(self) -> None:
        """Mevcut tüm görevleri görüntüler."""
        if not self.task_list:
            print("No tasks available.")
        else:
            for task in self.task_list:
                print(task)  # Her bir görevin __str__ metodunu çağırır.

    def get_task_by_id(self, task_id: int) -> Task:
        """Verilen task_id'ye sahip görevi döndürür."""
        for task in self.task_list:
            if task.task_id == task_id:
                return task
        return None

"""
SORU - CEVAPLAR

Görev Yönetimi: TaskManagement
	•	Tüm görevler burada tutulur.
	•	TaskManagement, görev eklemek ve görevleri listelemek gibi temel işlevlerden sorumludur.

1. SORU:

from typing import List   # List türünü kullanabilmek için gerekli bir import işlemi yapar. 

2. SORU :
	if not self.task_list:
            print("No tasks available.")

    bu kodda not yerine su sekilde yazsam olur muydu

    if self.task_list: List[Task]=[] :
                print("No tasks available.")
            
    not self.task_list: Bu, self.task_list listesinin boş olup olmadığını kontrol eder. 
    Eğer liste boşsa ([]), not operatörü True olur ve içindeki kod çalışır.

3. SORU : KOD ACIKLAMASI

    def __init__(self):
        self.task_list: List[Task] = []

        ""	
        task_list:  adında bir liste oluşturuluyor. 
                    Bu liste, Task sınıfından türetilmiş nesneleri (yani görevleri) tutacaktır.
        List[Task] ifadesi, 
                     liste içindeki elemanların Task türünden olduğunu belirtir. 
                     Yani bu listeye sadece Task türünde veya onun alt sınıflarından nesneler eklenebilir.""

"""
   