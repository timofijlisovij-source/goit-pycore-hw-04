def get_cats_info(path: str) -> list[dict]:

    cats = []

    try:
        with open(path, "r", encoding="utf-8") as cats_raw:
            for line in cats_raw:
                id, name, age = line.strip().split(",")

                cats_data = {
                    "id": id,
                    "name": name,
                    "age": age,
                }

                cats.append(cats_data)

            return cats

    except FileNotFoundError:
        print("File not found")
        return []

    except ValueError:
        print("Invalid data format in the file")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info(r"C:\games\New Text Document.txt")
    print(cats_info)
