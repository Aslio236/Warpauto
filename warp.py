import ipaddress, platform, subprocess, os, datetime, base64

def arch_suffix():
    machine = platform.machine().lower()
    if machine.startswith('i386') or machine.startswith('i686'):
        return '386'
    elif machine.startswith(('x86_64', 'amd64')):
        return 'amd64'
    elif machine.startswith(('armv8', 'arm64', 'aarch64')):
        return 'arm64'
    elif machine.startswith('s390x'):
        return 's390x'
    else:
        raise ValueError("Unsupported CPU architecture")

arch = arch_suffix()

print("Fetch warp program...")
url = f"https://gitlab.com/Misaka-blog/warp-script/-/raw/main/files/warp-yxip/warp-linux-{arch}"

subprocess.run(["wget", url, "-O", "warp"])
os.chmod("warp", 0o755)
command = "./warp >/dev/null 2>&1"
print("Scanning ips...")
process = subprocess.Popen(command, shell=True)
# Wait for the process to finish
process.wait()

# Check if there's any error
if process.returncode != 0:
    print("Error: Warp execution failed.")
else:
    print("Warp executed successfully.")

Bestip = []

with open(result_path, 'r') as csv_file:
    next(csv_file)
    c = 0
    for line in csv_file:
        Bestip.append(line.split(',')[0])
        c += 1
        if c == 2:
            break

def warp_ip():
    creation_time = os.path.getctime(result_path)
    formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")
    for i, ip in enumerate(Bestip):
        config_prefix = f'warp://{Bestip[0]}?ifp=10-20&ifps=20-60&ifpd=5-10#@mansor427🇮🇷&&detour=warp://{Bestip[1]}?ifp=10-20&ifps=20-60&ifpd=5-10#ÐΛɌ₭ᑎΞ𐒡𐒡🇩🇪WoW'
    return config_prefix, formatted_time


title = "//profile-title: base64:" + base64.b64encode('ʷᵃʳᵖ〘⬳𓄂𓆃⟿〙ʷᵃʳᵖ'.encode('utf-8')).decode('utf-8') + "\n"
update_interval = "//profile-update-interval: 1\n"
sub_info = "//subscription-userinfo: upload=0; download=0; total=10737418240000000; expire=2546249531\n"
profile_web = "//profile-web-page-url: https://github.com/mansor427\n"
last_modified = "//last update on: " + warp_ip()[1] + "\n"
configs = warp_ip()[0]
with open('warp.json', 'w') as op:
    op.write(title + update_interval + sub_info + profile_web  + last_modified + configs)

with open('Bestip.txt', 'w') as f:
    for ip in Bestip:
        f.write(f"{ip}\n")

os.remove(cfw_ips_txt_path)
os.remove(result_path)
os.remove("warp")
