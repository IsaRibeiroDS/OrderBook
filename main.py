# main.py

from classes import OrderBook

def main():
    orders = OrderBook()

    while True:
        try:
            command = input("command: ").strip()

            if command == "0":
                break

            elif command == "1":
                description = input("description: ").strip()
                prog_and_hours = input("programmer and workload estimate: ").strip()
                parts = prog_and_hours.split()
                if len(parts) != 2 or not parts[1].isdigit():
                    print("erroneous input")
                    continue
                programmer = parts[0]
                workload = int(parts[1])
                orders.add_order(description, programmer, workload)

            elif command == "2":
                for task in orders.finished_tasks():
                    print(task)

            elif command == "3":
                for task in orders.unfinished_tasks():
                    print(task)

            elif command == "4":
                task_id_input = input("id: ").strip()
                if not task_id_input.isdigit():
                    print("erroneous input")
                    continue
                try:
                    orders.mark_finished(int(task_id_input))
                except ValueError:
                    print("erroneous input")

            elif command == "5":
                for name in orders.programmers():
                    print(name)

            elif command == "6":
                name = input("programmer: ").strip()
                try:
                    status = orders.status_of_programmer(name)
                    print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
                except ValueError:
                    print("erroneous input")
            else:
                print("erroneous input")

        except Exception:
            print("erroneous input")


if __name__ == "__main__":
    main()
