from configobj import ConfigObj

filename='web_pos10_2RAM_2CPU_HDD.txt'
config = ConfigObj(filename)

#print(config)
print(config['max_connections'])

#for key, value in config.items():
#    print(key, value)
