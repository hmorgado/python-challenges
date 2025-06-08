import re
from datetime import datetime

pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>\w+)\s+(?P<path>[^\s]+)\s+(?P<protocol>[^"]+)"\s+(?P<status>\d+)\s+(?P<size>\d+)'
)

ip_counter_map = {}
status_counter = {}
dates = []

with open("access.log", "r") as file:
    for line_number, line in enumerate(file, 1):
        line.strip()
        match = pattern.match(line)
        if match:
            # gather info
            ip = match.group('ip')
            status = int(match.group('status'))
            date_obj = datetime.strptime(match.group('timestamp'), "%d/%b/%Y:%H:%M:%S %z")

            # Aggregate times
            dates.append(date_obj)

            # Aggregate IPs
            ip_counter_map[ip] = ip_counter_map.get(ip, 0) + 1

            # Sum 4XX and 5XX
            if 400 <= status <= 499:
                status_counter['4XX'] = status_counter.get('4XX', 0) + 1
            elif 500 <= status <= 599:
                status_counter['5XX'] = status_counter.get('5XX', 0) + 1


        else:
            print("no entry matched or found")

def order_map_by_value(map: {}) -> {}:
    return {ip: occ for ip, occ in sorted(map.items(), key=lambda item: item[1], reverse=True)}

def print_ip_rank():
    ordered_ip_occ = order_map_by_value(ip_counter_map)
    for idx, (ip, occ) in enumerate(ordered_ip_occ.items()):
        if idx >= 5:
            break
        print(f"IP Rank {idx + 1}: {ip}, occurred {occ} times.")

def print_4xx_5xx_count():
    for k, v in status_counter.items():
        print(f"Status {k}, sum of occ: {v}.")

def print_dates():
    print(f"Earlier entry: {sorted(dates)[0]}")
    print(f"Latest entry: {sorted(dates)[-1]}")

print_ip_rank()
print_4xx_5xx_count()
print_dates()
