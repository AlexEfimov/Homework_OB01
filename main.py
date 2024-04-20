class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = {
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
        print(f"Задача добавлена: {task['description']} - {task['due_date']}")

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['completed'] = True
                print(f"Задача отмечена как выполненная: {task['description']}")
                break
        else:
            print("Задача с таким описанием не найдена")

    def show_current_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task['completed']:
                print(f"{task['description']} - {task['due_date']} (Не выполнено)")


# Пример использования
manager = Task()
manager.add_task("Купить молоко", "2024-04-19")
manager.add_task("Отправить отчет", "2024-04-20")
manager.add_task("Сходить за пивом", "2024-04-23")
manager.add_task("Сделать ДЗ Зерокод", "2024-04-22")
manager.add_task("Сдать анализы", "2024-04-24")
manager.add_task("Не забыть победить Китайцев!", "2024-04-21")
manager.add_task("Насушить сухарей", "2024-04-23")
manager.show_current_tasks()
manager.mark_task_completed("Купить молоко")
manager.mark_task_completed("Отправить отчет")
manager.mark_task_completed("Сдать анализы")
manager.mark_task_completed("Сделать ДЗ Зерокод")
manager.show_current_tasks()
