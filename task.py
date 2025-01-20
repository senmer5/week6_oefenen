# 1. Task (Soyut Sınıf)

from abc import ABC, abstractmethod
from datetime import datetime


class Task(ABC):
    def __init__(self, task_id: int, task_name: str, deadline: datetime, status: str = "Pending", priority: str = "Low"):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.status = status
        self.priority = priority
        self.color = "Undefined"  # Varsayılan renk

    @abstractmethod
    def color_your_task(self) -> None:   # 	None dönüş türü, metot bir değer döndürmediğini belirtir.
        """Alt sınıflarda görev rengini ayarlamak için kullanılır."""
        pass

    def days_to_accomplish_task(self) -> int:
        """Görevin tamamlanmasına kalan gün sayısını döndürür."""
        today = datetime.now()
        remaining_days = (self.deadline - today).days
        return remaining_days

    def __str__(self):
        return f"""
        TASK ID   : {self.task_id}
        NAME      : {self.task_name}
        DEADLINE  : {self.deadline}
        STATUS    : {self.status}
        PRIORITY  : {self.priority}
        COLOR     : {self.color}
        """


# 2. PersonalTask (Task'tan Türetilen Sınıf)
class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline, status="Pending", priority="Low"):
        super().__init__(task_id, task_name, deadline, status, priority)
        self.color = "Blue"  # Özel rengi ayarla

    def color_your_task(self):
        return f"The task is marked with the color {self.color}"


# 3. WorkTask (Task'tan Türetilen Sınıf)
class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline, status="Pending", priority="High"):
        super().__init__(task_id, task_name, deadline, status, priority)
        self.color = "Red"  # Özel rengi ayarla

    def color_your_task(self):
        return f"The task is marked with the color {self.color}"



"""
SORULAR VE CEVAPLAR : 

1. Temel Task sınıfı, tüm görev türlerinin paylaşacağı ortak özellikleri içerir.

        - task_id: Görevin benzersiz kimliği
        - task_name: Görevin adı
        - deadline: Görevin teslim tarihi
        - status: Görevin durumu ('Pending'='Beklemede' veya 'Completed')
        - priority: Görevin önceliği ('Low', 'Medium', 'High')
        - color: Görevin görsel ayrımı için rengi /kirmizi = onemliler, green = tanimalanmis, yellow = devam edenler olsun.

2. Task sınıfı, tüm görevlerin temel özelliklerini içeren soyut bir sınıftır. Bu sınıfı türetecek olan diğer sınıflar, 
        örneğin PersonalTask ve WorkTask, Task sınıfındaki temel özellikleri miras alır. 
        Amaç, tüm görevlerin ortak özelliklerine sahip bir temel sınıf sağlamak.

3. (ABC)
	•	ABC, “Abstract Base Class” (Soyut Taban Sınıf) anlamına gelir.
        abc modülünü, Python’da soyut sınıflar ve soyut metotlar oluşturmak için kullanıyoruz. 
        ABC sınıfını miras alarak, sınıfın soyut olduğunu belirtmiş oluruz.

	•	abstractmethod dekoratörü, bir metodu soyut hale getirebilmemizi sağlar. 
        Bu metot alt sınıflarda mutlaka implement edilmelidir.

	•	datetime modülünü, tarih ve saat işlemleri için kullanıyoruz.
    
    Soyut Sınıf Neden Kullanılır?
	•	Bir şablon oluşturmak için kullanılır.
	•	Bu şablonu miras alan diğer sınıflar, soyut metodları kendi özelliklerine göre doldurmak (uygulamak) zorundadır.
	•	Soyut sınıfın kendisinden nesne oluşturulamaz.

    Soyut sınıfın amacı:
	•	Task sınıfı, genel bir çerçeve sağlar. Ancak kendisi direkt bir “nesne” olarak kullanılmaz.
	•	Soyut bir sınıf olduğunda, türetilen sınıfların belirli bir işlevselliği 
        (örneğin, color_your_task metodu) kesinlikle tanımlaması gerektiğini garanti eder.

    Örnek Durum:
	•	Task genel bir görev sınıfıdır ve farklı görev türlerinin (örneğin, kişisel veya iş görevleri) kendine özgü özellikleri vardır.
	•	color_your_task gibi bir metot, her alt sınıfın kendi türüne göre bir görev rengi belirlemesi gerektiğini ifade eder. 
        Soyut bir sınıf ile bu metodu zorunlu hale getiriyoruz.

    Eğer Task soyut olmasaydı, şu sorunlarla karşılaşabilirdik:
	1.	Direkt olarak Task sınıfından nesne oluşturulabilir ve bu nesnenin rengi gibi özellikleri eksik kalabilirdi.
	2.	Alt sınıfların belirli metotları (örneğin, color_your_task) yanlışlıkla ihmal edilip boş bırakılabilirdi.

    Soyutluk sayesinde:
	•	Task tek başına kullanılmaz, sadece bir temel sağlar.
	•	Alt sınıfların gerekli tüm metodları tanımladığı garanti edilir.

4. Type Hinting’in Kullanımı: -> None , -> int , ....
	•	Fonksiyonun dönüş türü hakkında bilgi vermek amacıyla kullanılır.
	•	Eğer fonksiyon bir değer döndürseydi, örneğin bir sayı döndürüyorsa -> int yazardık.

        """