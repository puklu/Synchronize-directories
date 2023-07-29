import os
import logging
import shutil
import hashlib


def copy_directory(source, destination):
    """
    Copies an entire directory with its content to a desired destination.
    :param source: Path of the directory that needs to be copied.
    :param destination: Path where the directory needs to be copied.
    :return:
    """
    try:
        if not os.path.exists(destination):
            shutil.copytree(source, destination)
            logging.info(f"{source} directory copied to {destination}")
            print(f"{source} directory copied to {destination}")
    except shutil.Error as e:
        logging.info(f"Error: {e}")
        print(f"Error: {e}")
    except OSError as e:
        logging.info(f"Error: {e}")
        print(f"Error: {e}")


def copy_file(source, destination):
    """
    Copies a file from one place to another.
    :param source: Path of the file that needs to be copied
    :param destination: Path to where the file needs to be copied.
    :return:
    """
    try:
        destination_dir = os.path.dirname(destination)
        os.makedirs(destination_dir, exist_ok=True)
        shutil.copy2(source, destination)
        logging.info(f"{source} file copied to {destination}")
        print(f"{source} file copied to {destination}")
    except Exception as e:
        logging.info(f"Error: {e}")
        print(f"Error: {e}")


def is_dir_empty(directory_path):
    """
    Checks if a directory is empty.
    :param directory_path: Path to the directory.
    :return: True if empty, else False.
    """
    return not os.listdir(directory_path)


def calculate_hash(parent_path):
    """
    Calculates the hash of every file present in the parent_path directory.
    :param parent_path: Path of the directory whose files needs to be hashed.
    :return: A dict with the keys being the path of each file (relative to parent_path) and values being the hash
    of the file.
    """
    walker = os.walk(parent_path)
    hash_files = dict()

    for directory, sub_directory, files in walker:
        if is_dir_empty(directory):
            try:
                filepath = directory.split(f"{parent_path}/")[1]
                hash_files[f"{filepath}/"] = ""
            except IndexError:
                pass
        else:
            for file in files:
                tpath = os.path.join(directory, file)
                filehash = hashlib.md5(open(tpath, 'rb').read()).hexdigest()
                filepath = tpath.split(f"{parent_path}/")[1]
                hash_files[filepath] = filehash

    return hash_files


def remove_file_dir(fpath):
    """
    Deletes a file from a path. If the path is to an empty directory, then the directory is deleted.
    :param fpath: Path to the file or empty directory that is to be deleted.
    """
    try:
        if os.path.isdir(fpath) and is_dir_empty(fpath):
            os.rmdir(fpath)
        else:
            os.remove(fpath)

        logging.info(f"{fpath} deleted.")
        print(f"{fpath} deleted.")

    except FileNotFoundError as e:
        print(e)