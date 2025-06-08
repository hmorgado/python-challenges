import random
import datetime

def generate_log_line():
    ip_list = [
        '160.113.147.19',
        '51.74.34.236',
        '11.175.97.150',
        '126.81.182.39',
        '67.254.149.86',
        '127.66.136.3',
        '68.103.169.131',
        '161.194.196.175',
        '227.184.10.179',
        '75.166.133.91',
        '238.245.220.169',
        '163.156.31.153',
        '153.34.118.214'
    ]

    def select_ip_randomly(ips: []) -> str:
        return ips[random.randint(0, len(ips) - 1)]

    ip_address = select_ip_randomly(ip_list)
    timestamp = datetime.datetime.now() - datetime.timedelta(
        seconds=random.randint(0, 60 * 60 * 24 * 30)
    )
    formatted_timestamp = timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")

    method = random.choice(["GET", "POST", "DELETE", "PUT"])
    url = random.choice(["/index.html", "/api/data", "/login", "/dashboard", "/home"])
    protocol = "HTTP/1.1"

    status_code = random.choices(
        [200, 301, 400, 403, 404, 500, 502, 503],
        weights=[70, 5, 5, 5, 5, 2, 2, 1],
        k=1
    )[0]
    size = random.randint(100, 5000)

    return f'{ip_address} - - [{formatted_timestamp}] "{method} {url} {protocol}" {status_code} {size}'


def generate_log_file(filename, num_lines):
    with open(filename, "w") as f:
        for _ in range(num_lines):
            f.write(generate_log_line() + "\n")


amount_of_lines = 10000

if __name__ == "__main__":
    generate_log_file("access.log", amount_of_lines)
    print(f"Log file 'access.log' created with {amount_of_lines} lines.")

