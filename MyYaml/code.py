import yaml

with open('./dev4.yaml', 'r') as f:
    x = yaml.safe_load(f)

print(x)
# print(x['ip'])
# print(x['allow_hosts'])
