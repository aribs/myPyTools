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
  totalFiles = 0
  for ip in ipList:
    ip_inicio = ip["ip_enter"]
    ip_fin = ip["ip_out"]
    command = f"masscan -p445 {ip_inicio}-{ip_fin} --max-rate 3000 > ./output/outputRange{totalFiles}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    totalFiles+=1
  print(totalFiles)
  #Juntamos Ficheros salida en oput
  file = "./output/output"
  with open(file, 'w') as base_file:
      for i in range(0, totalFiles):
        fileName = f"./output/outputRange{i}"
        try:
          with open(fileName, 'r') as temporal_file:
            #print(temporal_file.read())
            base_file.write(temporal_file.read())   
        except FileNotFoundError:
            print(f"El fichero {base_file} no existe.")  
else:
  print("El archivo CSV no existe en la ruta proporcionada.")