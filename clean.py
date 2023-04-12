import os

def clean_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".tmp") or file.endswith(".log") or file.endswith(".obj") or file.endswith(".txt"):
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(e)
            elif os.path.getsize(os.path.join(root, file)) == 0:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    clean_directory("D:\\")
