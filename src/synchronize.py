import logging

from helper import *


def copy_from_source(src, rep, src_files, replica_files):
    """
    Copies the files, which are not already present, from source directory to replica directory.
    :param src: Path to the source directory.
    :param rep: Path to the replica directory.
    :param src_files: A dict where the keys are the file names of the files present in the source directory
     and values are the hash of the file.
    :param replica_files: A dict where the keys are the file names of the files present in the replica directory
     and values are the hash of the file.
    :return:
    """
    for fpath in src_files:
        if not os.path.isdir(src/fpath):
            src_file = src / fpath
            rep_file = rep / fpath
            if fpath not in replica_files:  # if the file doesn't exist in replica, copy it
                copy_file(src_file, rep_file)
            else:  # if the file does exist, verify the contents of the file is the same
                if src_files[fpath] != replica_files[fpath]:
                    copy_file(src_file, rep_file)

        elif is_dir_empty(src/fpath):
            src_file = src / fpath
            rep_file = rep / fpath
            copy_directory(src_file, rep_file)


def remove_from_replica(src, rep, src_files, replica_files):
    """
    Removes the files from replica folder which are not present in the source directory.
    :param src: Path to the source directory.
    :param rep: Path to the replica directory.
    :param src_files: A dict where the keys are the file names of the files present in the source directory
     and values are the hash of the file.
    :param replica_files: A dict where the keys are the file names of the files present in the replica directory
     and values are the hash of the file.
    :return:
    """
    for fpath in replica_files:
        if fpath not in src_files:
            rep_file = rep / fpath
            try:
                if is_dir_empty(rep_file):
                    os.rmdir(rep_file)
                else:
                    os.remove(rep_file)
                logging.info(f"{rep_file} deleted from {rep}")
                print(f"{rep_file} deleted from {rep}")
            except FileNotFoundError as e:
                print(e)


def synchronize(src, rep):
    """
    Performs one way synchronization the contents of two directories: Source directory and Replica directory.
    :param src: path to source directory.
    :param rep: path to replica directory.
    :return:
    """

    # if the source directory doesn't exist for some reason
    if not src.is_dir():
        print("Source directory doesn't exist!")
        return

    # To handle the case of initial synchronization when the replica directory doesn't exist
    if not rep.is_dir():
        copy_directory(src, rep)  # Entire source directory is copied as it is
        return

    # Retrieving the file paths and their hashes
    src_files = calculate_hash(src)
    replica_files = calculate_hash(rep)

    # Copying the files from source to replica directory
    copy_from_source(src, rep, src_files, replica_files)

    # Removing the files, that do not exist in source directory anymore, from replica directory
    remove_from_replica(src, rep, src_files, replica_files)



