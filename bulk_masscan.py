import csv
import json
import os
import subprocess

# Ruta completa al archivo CSV
csv_file = "iplist/es_development.csv"

# Verificar si el archivo existe
if os.path.exists(csv_file):
  # Lista para almacenar los datos del CSV
  ipList = []

  # Leer el archivo CSV y almacenar los datos en la lista
  with open(csv_file, newline='') as csvfile:
    lector_csv = csv.DictReader(csvfile)
    for file in lector_csv:
      ipList.append({
            "ip_enter":file['ip_enter'],
            "ip_out": file['ip_out']
      })
  #Ejecutamos masscan
  i = 0
  for ip in ipList:
    ip_inicio = ip["ip_enter"]
    ip_fin = ip["ip_out"]
    command = f"masscan -p445 {ip_inicio}-{ip_fin} --max-rate 3000 > ./output/outputTest{i}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    i+=1
  print(i)
      
else:
  print("El archivo CSV no existe en la ruta proporcionada.")