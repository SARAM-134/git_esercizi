config:dict[str:str|int|bool]={
    "host":"192.168.1.1",
    "port":8080,
    "ssl":True,
    "timeout":30
}

print(config.get("host"))
config["port"]=443
config["protocol"]="https"
print(config)