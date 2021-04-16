from pathlib import Path
# path = Path("C:\\Users\\hhhye\\PycharmProjects\\pythonProject")

# path.parent
# path.name
# path.suffix
# path.stem
#
# path.exists()
# path.is_dir()
# path.is_file()
# path.home()

file_path = Path("C:\\Users\\hhhye\\PycharmProjects\\pythonProject\\modules\\car_sample.py")
print(file_path.parent)
print(file_path.name)
print(file_path.suffix)
print(file_path.stem)

# methods
dir_path = Path('C:\\Users\\hhhye\\PycharmProjects\\pythonProject\\modules')
print(dir_path.exists())
print(dir_path.is_dir())
print(dir_path.is_file())
print(dir_path.home())

r_dir_path = Path('.')
r_dir_path.resolve()


