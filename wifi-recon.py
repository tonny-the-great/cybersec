echo "[*] Scanning for nearby WiFi networks..."
nmcli dev wifi list

read -p "[?] Enter target SSID: " ssid
read -p "[?] Enter WiFi password: " password

echo "[*] Connecting to $ssid..."
nmcli dev wifi connect "$ssid" password "$password"

echo "[*] Getting IP address of the device..."
ip route | grep default | awk '{print $3}'

read -p "[?] Enter target IP (usually 192.168.x.1): " target_ip

echo "[*] Running port scan on $target_ip..."
nmap -sV -Pn "$target_ip"
