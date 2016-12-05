#
#  tail and grep :)
#
#
#

from tail import tailf


def grep(pattern, lines):
    """Search for a pattern in given lines."""
    for line in lines:
        if pattern in line:
            yield line

if __name__ == "__main__":
    file_desc = open("/var/log/apache2/access.log")
    read_lines = tailf(filed=file_desc)
    # look for word test in the read lines
    grepped_lines = grep("test", read_lines)
    for _line in grepped_lines:
        print _line,

