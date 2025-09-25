
config = dict()

config = dict()

for i in range(3):
    key = input(f"{i+1}-setting nomi: ")
    value = input(f"{i+1}-setting qiymati: ")
    config[key] = value

print("---Config sozlamalari---")
print(config)
