import subprocess

class Raspberry:
  @staticmethod
  def Call(command):
    time = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = time.communicate();
    return [output,err];
  
  @staticmethod
  def GetDate():
    return Raspberry.Call('date')[0];
  
  @staticmethod
  def Reboot():
    return Raspberry.Call('reboot');
  @staticmethod
  def PowerOff():
    return Raspberry.Call('poweroff');
  
  @staticmethod
  def GetCPUInfo():
    return Raspberry.Call('lscpu')[0];
  @staticmethod
  def GetDiscInfo():
    return Raspberry.Call('lsblk')[0];
  @staticmethod
  def GetDiscSpaceInfo():
    return Raspberry.Call('fdisk -l')[0];
  @staticmethod
  def GetUSBInfo():
    return Raspberry.Call('lsusb')[0];

  @staticmethod
  def GetProcessInfo():
    return Raspberry.Call('sudo ps -a')[0];
  @staticmethod
  def GetSystemInfo():
    return Raspberry.Call('top')[0];
  
  @staticmethod
  def KillProcessByID(pid):
    return Raspberry.Call('kill '+str(pid));
  
  @staticmethod
  def KillProcessByName(processName,killAll=False):
    if killAll:
      resp= Raspberry.Call('killall '+str(processName));
    else:
      resp= Raspberry.Call('pkill '+str(processName));
    return resp;
    
