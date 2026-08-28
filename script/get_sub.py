import curl_cffi as requests
import os

out_folder = 'domains'
rewrite = 1

def getDomains(tld):
    print("-> ", tld)
    headers = {
        'user-agent': ''
    }
    try:
        resp = requests.get(f'https://app.agniops.in/v1/search?domain={tld}', headers=headers, timeout=360).text
    except:
        print(f"Failed to open https://app.agniops.in/v1/search?domain={tld}")
        return

    if rewrite:
        with open(os.path.join(out_folder, f'{tld}.txt'), mode='w+', encoding='utf-8') as f:
            f.write(resp)
    else:
        if not os.path.exists(os.path.join(out_folder, f'{tld}.txt')):
            with open(os.path.join(out_folder, f'{tld}.txt'), mode='w+', encoding='utf-8') as f:
                f.write(resp)
        else:
            print(f"File already exists for tld {tld}")



if __name__ == "__main__":
    os.makedirs(out_folder, exist_ok=True)
    tlds = open('input.txt', mode='r', encoding='utf-8').read().split('\n')
    for tld in tlds:
        getDomains(tld)

