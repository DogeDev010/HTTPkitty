import webbrowser
import random

HTTP_STATUS_CODES = [
    100, 101, 102, 200, 201, 202, 204, 206,
    300, 301, 302, 303, 304, 305, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 408,
    409, 410, 411, 412, 413, 414, 415, 416,
    417, 418, 420, 421, 422, 423, 424, 425,
    426, 429, 431, 444, 450, 451, 499, 500,
    501, 502, 503, 504, 506, 507, 508, 509,
    510, 511, 599
]

BASE_URL = "https://http.cat/"

def open_kitteh(code):
    url = f"{BASE_URL}{code}"
    print(f"Opening kitty code {code}...")
    webbrowser.open(url)

def main():
    print("Got a HTTP status code? \n See what kitty matches it and learn about the status!")
    print("1. Enter a specific HTTP status")
    print("2. Pull a random one")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        try:
            code = int(input("Enter HTTP status code: ").strip())
            if code in HTTP_STATUS_CODES:
                open_kitteh(code)
            else:
                print("That status code is FAKE and NOT REAL and WRONG and..")
        except ValueError:
            print("Stop trying to break my shi")
    elif choice == "2":
        code = random.choice(HTTP_STATUS_CODES)
        open_kitteh(code)
    else:
        print("Stop trying to break my shi its not gonna work")

if __name__ == "__main__":
    main()