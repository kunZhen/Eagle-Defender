import paramiko
import os


class SSHFileTransfer:
    def __init__(self, hostname, port, username, private_key_file):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.private_key_file = private_key_file
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            private_key = paramiko.RSAKey(filename=self.private_key_file)
            self.ssh.connect(self.hostname, self.port, self.username, pkey=private_key)
        except Exception as e:
            print(f'Error al establecer la conexión SSH: {str(e)}')

    def __enter__(self):
        return self

    def __exit__(self):
        self.ssh.close()

    def copy_file_to_remote(self, archivo_local, directorio_destino, name):
        try:
            sftp = self.ssh.open_sftp()
            sftp.put(archivo_local, os.path.join(directorio_destino, name))
            print(f'El archivo {archivo_local} se ha copiado a la máquina virtual en {directorio_destino}.')
        except Exception as e:
            print(f'Error al copiar el archivo: {str(e)}')

    def copy_file_from_remote(self, archivo_remoto, directorio_destino):
        try:
            sftp = self.ssh.open_sftp()
            sftp.get(archivo_remoto, os.path.join(directorio_destino, os.path.basename(archivo_remoto)))
            print(f'El archivo {archivo_remoto} se ha copiado desde la máquina virtual a {directorio_destino}.')
        except Exception as e:
            print(f'Error al copiar el archivo desde la máquina virtual: {str(e)}')

    def delete_remote_file(self, archivo_remoto):
        try:
            sftp = self.ssh.open_sftp()
            sftp.remove(archivo_remoto)
            print(f'El archivo {archivo_remoto} se ha eliminado de la máquina virtual.')
        except Exception as e:
            print(f'Error al eliminar el archivo en la máquina virtual: {str(e)}')

    def remote_file_exists(self, archivo_remoto):
        try:
            sftp = self.ssh.open_sftp()
            try:
                sftp.stat(archivo_remoto)
                print(f'El archivo {archivo_remoto} existe en la máquina virtual.')
                return True
            except FileNotFoundError:
                print(f'El archivo {archivo_remoto} no existe en la máquina virtual.')
                return False
        except Exception as e:
            print(f'Error al validar la existencia del archivo en la máquina virtual: {str(e)}')
            return False
