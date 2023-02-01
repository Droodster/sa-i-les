import maincrawler

def export_text(crawler):
    data = maincrawler(crawler)
    with open("export.txt", "w") as file:
        for item in data:
            file.write(str(item) + "\n")

if __name__ == "__main__":
    export_text(maincrawler)
