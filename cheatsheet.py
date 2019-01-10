import os
import time
import subprocess


if os.name == 'nt':
    os.system('cls')
    print('[+]Windows System Detected.')
    print('[+]Checking for Unusual Processes and Services')
    time.sleep(3)
    os.system('net start > net_start.txt')
    os.system('sc query > sc_query.txt')
    os.system('tasklist /svc > tasklist_svc.txt')
    print('[+]Checking for Unusual Files and Registry Keys')
    try:
        os.system('reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run > hklm_Run.txt')
        os.system('reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Runonce > hklm_Runonce.txt')
        os.system('reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunonceEx > hklm_RunonceEx.txt')
        os.system('reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run > hkcu_Run.txt')
        os.system('reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Runonce > hkcu_Runonce.txt')
        os.system('reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunonceEx > hkcu_RunonceEx.txt')
    except  ERROR as e:
        print ('[-]') + e
    print('[[+]Checking for Unusual Network Usage')
    try:
        os.system('net view \\127.0.01 >  net_view.txt')
        os.system('net session > net_session.txt')
        os.system('net use > net_use.txt')
        os.system('nbtstat -S > nbstat.txt')
        os.system('netstat -naob > netstat_naob.txt')
        os.system('netsh advfirewall firewall show rule name=all > netsh.txt')
    except:
        e = sys.exc_info()[0]
        write_to_page( "<p>Error: %s</p>" % e )
    print('[+]Checking for Unusual Scheduled Tasks > schtasks.txt')
    os.system('wmic startup list full > startup.txt')
    print('[+]Checking for Unusal Accounts')
    os.system('net user > net_user.txt')
    os.system('net localgroup administrators > net_localgroup.txt')
    
elif os.name == 'posix':
    os.system('clear')
    print('[+]Linux System Detected.')
    print('[+]Checking for Unusual Processes and Services.')
    time.sleep(3)
    # This loop is for pulling out root activities after running ps -aux
    file_handle_write = open('ps_aux', 'w')
    subprocess.call(['ps', '-aux'], stdout = file_handle_write)
    file_handle_write.close()
    # Open file to be read and parsed
    # so we can find the root user 
    # processes
    file_handle_read = open('ps_aux', 'r')
    contents = file_handle_read.readlines()
    
    for row in range(len(contents)):
        if 'root' in contents[row]:
            print(contents[row])


elif os.name == 'os2':
    os.system('clear')

    
