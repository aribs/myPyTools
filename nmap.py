#Get Domain in ARGV, make a hosts, save a IP Address and make Nmap for all of this
import subprocess
import re
import sys


if len(sys.argv)<1:
  print("Error- No param")
else:
  process = subprocess.Popen(['host', sys.argv[1]],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  stdout, stderr

  bruteText =  stdout.decode("utf-8")
  file = None
  if len(sys.argv)<=3:
    nameOutputFile = sys.argv[2]
    file = open(nameOutputFile, "x")
  arrIp = re.findall( r'[0-9]+(?:\.[0-9]+){3}', bruteText )
  for ip in arrIp:
    process = subprocess.Popen(['nmap', ip],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout, stderr  
    if(file):
      file.write(ip)
      file.write('\n')
      file.write(stdout.decode("utf-8"))
      file.write("//////////////")
    print("///////////////////")
    print (ip)
    print(stdout.decode("utf-8"))
if(file):
  file.close()
