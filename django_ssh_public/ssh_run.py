import spur

def _parse_output(input_data):
    header = True
    header_list = []
    values_list = []

    for row in input_data.split(b'\n'):
        row_list = []

        for row_value in row.split(b' '):
            row_list.append(row_value.decode("utf-8"))

        row_list = list(filter(None, row_list))

        if header:
            header = False
            header_list.append(row_list)
        else:
            if len(row_list) == len(header_list[0]):
                values_list.append(row_list)
            
                # print(len(row_list))
    # print(header_list)
    # print(values_list)
    return header_list, values_list


def ssh_get(ip_address, username, password):
    shell = spur.SshShell(hostname=ip_address, username=username, password=password, missing_host_key=spur.ssh.MissingHostKey.accept)

    with shell:
        result = shell.run(["ps", "aux", "--sort", "-rss"])

        return _parse_output(result.output)
        # print(result.output) # prints hello

