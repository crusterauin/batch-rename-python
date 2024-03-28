import os

source_dir = './bahan'
dest_dir = './hasil'

files = os.listdir(source_dir)

for file in files:
    source_path = os.path.join(source_dir, file)
    dest_filename = f"{file.split('.')[0]} TW 1.pdf"
    dest_path = os.path.join(dest_dir, dest_filename)
    
    try:
        os.rename(source_path, dest_path)
        print(f"{source_path} berhasil diubah nama menjadi {dest_path}.")
    except IsADirectoryError:
        print(f"{source_path} adalah sebuah direktori dan tidak dapat diubah namanya.")
    except NotADirectoryError:
        print(f"{source_path} adalah sebuah file dan tidak dapat diubah namanya.")
    except PermissionError:
        print(f"Tidak dapat mengubah nama {source_path} karena tidak memiliki izin.")
    except OSError as error:
        print(f"Terjadi kesalahan: {error}")