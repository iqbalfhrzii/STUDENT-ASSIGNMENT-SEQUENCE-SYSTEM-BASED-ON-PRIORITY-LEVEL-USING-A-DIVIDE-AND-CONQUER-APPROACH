def merge_sort(arr, key="deadline"):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if key == "deadline":
                if (
                    left_half[i]["deadline"] > right_half[j]["deadline"]
                ):  # Perubahan dilakukan di sini
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            elif key == "prioritas":
                if left_half[i]["prioritas"] < right_half[j]["prioritas"]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def print_tasks(tasks):
    if not tasks:
        print("Tidak ada daftar tugas")
    else:
        for i, task in enumerate(tasks, 1):
            print(
                f"{i}. {task['nama']} - Deadline: {task['deadline']} - Prioritas: {task['prioritas']}"
            )


tasks = []

while True:
    print("\nMenu:")
    print("1. Daftar tugas")
    print("2. Tambah tugas")
    print("3. Urutkan tugas")
    print("4. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        print("\nDaftar Tugas:")
        print_tasks(tasks)
    elif choice == "2":
        nama = input("Masukkan nama tugas: ")
        deadline = input("Masukkan deadline tugas (DD/MM/YYYY): ")
        prioritas = int(input("Masukkan prioritas tugas (1-10): "))
        tasks.append({"nama": nama, "deadline": deadline, "prioritas": prioritas})
        print("Tugas berhasil ditambahkan!")
    elif choice == "3":
        if not tasks:
            print("Tidak ada daftar tugas")
        else:
            key = input("Urutkan berdasarkan prioritas (p) atau deadline (d): ")
            merge_sort(tasks, "prioritas" if key == "p" else "deadline")
            tasks.reverse()
            print("Daftar tugas berhasil diurutkan")
    elif choice == "4":
        break
    else:
        print("Pilihan tidak valid")
