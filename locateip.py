import pygeoip
gi = pygeoip.GeoIP('GeoIP.dat') 

if len(sys.argv)<1:
  print("Error- No param")
else:
  gi.country_name_by_addr(sys.argv[1])
