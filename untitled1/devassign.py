ips_count = {}
with open("logfile","r") as logfile:
    for line in logfile:
        ip = line.split()
        ips_count.setdefault(str(ip[0]),0)
        ips_count[str(ip[0])]+=1
ips_count = sorted(ips_count.items(), key=lambda x:x[1], reverse=True)
sorted_ips = dict(ips_count)
for i in sorted_ips:
    print(i, sorted_ips[i])