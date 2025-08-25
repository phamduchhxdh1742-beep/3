import requests
import time
cookies = {
    'ajs_anonymous_id': 'aced0852-2039-4331-8bb1-83ccaec50204',
    'modal-session': 'se-rz7speTQeduihcEQLADMgZ:xx-zm6wpKL5MwGm0jVy6OYdZ4',
    'modal-last-used-environment#vudeptrai79007': 'main',
    'modal-last-used-workspace': 'vudeptrai79007',
    'ajs_user_id': 'us-CHOoCHBz0ygGkUm80OiGv5',
    'INGRESSCOOKIE': '1755862455.709.353.979042|9de6a539c14bab7f9073ed2b75abad44',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%22us-CHOoCHBz0ygGkUm80OiGv5%22%2C%22%24sesid%22%3A%5B1755866108101%2C%220198d18e-d623-7a3f-bc30-5da2712ba527%22%2C1755862455843%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fapps%22%7D%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=1543c249318246a694140eff3b21f2f3,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=c001a3bb54a795519d3da013ff1b706d,sentry-sample_rand=0.7959776268865488',
    'content-type': 'application/json',
    'origin': 'https://modal.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'c001a3bb54a795519d3da013ff1b706d-8ed5d7594d1be602',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'ajs_anonymous_id=aced0852-2039-4331-8bb1-83ccaec50204; modal-session=se-rz7speTQeduihcEQLADMgZ:xx-zm6wpKL5MwGm0jVy6OYdZ4; modal-last-used-environment#vudeptrai79007=main; modal-last-used-workspace=vudeptrai79007; ajs_user_id=us-CHOoCHBz0ygGkUm80OiGv5; INGRESSCOOKIE=1755862455.709.353.979042|9de6a539c14bab7f9073ed2b75abad44; ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog=%7B%22distinct_id%22%3A%22us-CHOoCHBz0ygGkUm80OiGv5%22%2C%22%24sesid%22%3A%5B1755866108101%2C%220198d18e-d623-7a3f-bc30-5da2712ba527%22%2C1755862455843%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fapps%22%7D%7D',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import modal\n\n# Tạo image có CUDA, Python, git, curl, Node.js LTS 18\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .apt_install("git", "curl", "gnupg")\n    .run_commands(\n        "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n        "apt-get install -y nodejs"\n    )\n    .pip_install("cupy-cuda12x")\n)\n\napp = modal.App("node-runner")\n\n@app.function(image=image, gpu="A10G")\ndef run_node():\n    import subprocess\n\n    # Clone repo (chỉ clone nếu chưa có)\n    subprocess.run(["git", "clone", "--depth=1", "https://github.com/vudeptrai79007-sketch/tool.git"], check=False)\n\n    # Chạy node app.js trong thư mục tool\n    process = subprocess.Popen(["node", "app.js"], cwd="tool")\n    process.wait()',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 16,
        'cols': 43,
    },
}

response = requests.post('https://modal.com/api/playground/vudeptrai79007/run', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import modal\\n\\n# Tạo image có CUDA, Python, git, curl, Node.js LTS 18\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .apt_install(\\"git\\", \\"curl\\", \\"gnupg\\")\\n    .run_commands(\\n        \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n        \\"apt-get install -y nodejs\\"\\n    )\\n    .pip_install(\\"cupy-cuda12x\\")\\n)\\n\\napp = modal.App(\\"node-runner\\")\\n\\n@app.function(image=image, gpu=\\"A10G\\")\\ndef run_node():\\n    import subprocess\\n\\n    # Clone repo (chỉ clone nếu chưa có)\\n    subprocess.run([\\"git\\", \\"clone\\", \\"--depth=1\\", \\"https://github.com/vudeptrai79007-sketch/tool.git\\"], check=False)\\n\\n    # Chạy node app.js trong thư mục tool\\n    process = subprocess.Popen([\\"node\\", \\"app.js\\"], cwd=\\"tool\\")\\n    process.wait()","modalEnvironment":"main","winsize":{"rows":16,"cols":43}}'.encode()
#response = requests.post('https://modal.com/api/playground/vudeptrai79007/run', cookies=cookies, headers=headers, data=data)
url = 'https://modal.com/api/playground/vudeptrai79007/run'
delay = 3  

def main():
    while True:
        try:
            resp = requests.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=10  
            )
            print(f"Đã tạo worker thành công | Status: {resp.status_code}")
        except requests.exceptions.Timeout:
            print("Request bị timeout, thử lại sau...")
        except Exception as e:
            print(f"Tạo worker với lỗi: {e}")

        for i in range(delay, 0, -1):
            print(f"Đợi {i} giây...", end="\r", flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()

