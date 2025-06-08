import requests as req
import concurrent.futures

def task(_url: ""):
    try:
        url = _url.strip()
        response = req.get(url, timeout=5, allow_redirects=False)
        status = response.status_code
        if status == 200:
            print(f"✅ {url} is UP")
        if 300 <= status <= 399:
            print(f"❌ {url} redirects (Status: {status})")
        if 400 <= status <= 599:
            print(f"❌ {url} is DOWN (Status: {status})")
    except Exception as e:
        print(f"⚠️ {url} failed with error: [{e}]")

def read_urls_from_file(file_path: str) -> [str]:
    with open("urls.txt", "r") as file:
        return [line.strip() for line in file]

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        executor.map(task, read_urls_from_file("urls.txt"))


if __name__ == "__main__":
    main()