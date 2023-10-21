import errno
    # Let's take a look at some selected constants useful for detecting stream errors:

    # errno.EACCES → Permission denied

    # The error occurs when you try, for example, to open a file with the read only attribute for writing.

    # errno.EBADF → Bad file number

    # The error occurs when you try, for example, to operate with an unopened stream.

    # errno.EEXIST → File exists

    # The error occurs when you try, for example, to rename a file with its previous name.

    # errno.EFBIG → File too large

    # The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.

    # errno.EISDIR → Is a directory

    # The error occurs when you try to treat a directory name as the name of an ordinary file.

    # errno.EMFILE → Too many open files

    # The error occurs when you try to simultaneously open more streams than acceptable for your operating system.

    # errno.ENOENT → No such file or directory

    # The error occurs when you try to access a non-existent file/directory.

    # errno.ENOSPC → No space left on device

    # The error occurs when there is no free space on the media.
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)