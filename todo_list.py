import json

def load_tasks():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)
def show_tasks(tasks):
    if not tasks:
        print("沒有待辦事項")
    else:
        for index ,task in enumerate(tasks):
            status="[\u2714]" if task["done"] else"[ ]"
        print(f"{index+1}. {status} {task['title']}")
def add_task(tasks):
    title= input("請輸入待辦事項： ")
    tasks.append({"title":title,"done":False})
    save_tasks(tasks)
    print(f"已新增:「{title}」")
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num= int(input("請輸入已完成的事項編號："))-1
        if 0<=task_num<len(tasks):
            tasks[task_num]["done"]=True
            save_tasks(tasks)
            print(f"以標記為完成：「{tasks[task_num]['title']}」")
        else:
            print('無效的編號！')
    except ValueError:
        print("請輸入正確的數字！")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num=int(input("請輸入要刪除的事項編號："))-1
        if 0 <= task_num <len(tasks):
            removed_task= tasks.pop(task_num)
            save_tasks(tasks)
            print(f"已刪除「{removed_task["title"]}」")
        else:
            print("無效的編號！")
    except ValueError:
        print("請輸入正確的數字！")

def main():
    tasks=load_tasks()
    while True:
        print("\n📌 代辦事項清單")
        print("1.新增事項")
        print("2.顯示事項")
        print("3.標記完成")
        print("4.刪除事項")
        print("5.離開")
        
        choice= input("請選擇操作(1-5): ")
        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            show_tasks(tasks)
        elif choice=="3":
            complete_task(tasks)
        elif choice=="4":
            delete_task(tasks)
        elif choice=="5":
            print("再見！👋")
            break
        else:
            print("請輸入有效選項！")
if __name__ == "__main__":
    main()

               



