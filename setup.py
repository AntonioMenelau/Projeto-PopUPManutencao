from cx_Freeze import setup, Executable

setup(name='app-v1',
      description='pop up para alerta de manutenção',
      version='0.1',
      executables=[Executable('Principal4-v2.pyw', base='Win32GUI', icon='MasterTech-ico.ico')])
