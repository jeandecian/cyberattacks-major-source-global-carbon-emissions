ACS712_VOLTAGES = {
    "hosafe": 12,
    "rpi4b4": 5,
}
ATTACK = "Attack"
ATTACK_MODE_000101 = {
    "idle": "00:00:00.000",
    "attack": "00:01:00.000",
    "recovery": "00:01:10.000",
}
ATTACK_MODE_000103 = {
    "idle": "00:00:00.000",
    "attack": "00:01:00.000",
    "recovery": "00:03:05.000",
}
ATTACK_MODE_000202 = {
    "idle": "00:00:00.000",
    "attack": "00:02:00.000",
    "recovery": "00:02:10.000",
}
ATTACK_MODE_000204 = {
    "idle": "00:00:00.000",
    "attack": "00:02:00.000",
    "recovery": "00:04:00.000",
}
ATTACK_MODE_000510 = {
    "idle": "00:00:00.000",
    "attack": "00:05:00.000",
    "recovery": "00:10:00.000",
}
ATTACK_MODE_45485055 = {
    "idle": "02:45:00.000",
    "idle_browser_open": "02:48:00.000",
    "attack": "02:50:00.000",
    "recovery": "02:55:00.000",
}
ATTACK_MODES = ("Idle", "Attack", "Recovery")
ATTACK_NAMES = {
    "bstry": "Bstry",
    "coinimp": "CoinIMP (CPU) (100%)",
    "coinimp-0%": "CoinIMP (CPU) (0%)",
    "coinimp-10%": "CoinIMP (CPU) (10%)",
    "coinimp-100%": "CoinIMP (CPU) (100%)",
    "coinimp-20%": "CoinIMP (CPU) (20%)",
    "coinimp-30%": "CoinIMP (CPU) (30%)",
    "coinimp-40%": "CoinIMP (CPU) (40%)",
    "coinimp-50%": "CoinIMP (CPU) (50%)",
    "gminer": "GMiner (GPU)",
    "goldeneye": "GoldenEye (HTTP)",
    "goloris": "Goloris (HTTP)",
    "hping3": "Hping3 (SYN)",
    "hulk": "HULK (HTTP)",
    "jigsaw": "Jigsaw",
    "lolminer": "lolMiner (GPU)",
    "mhddos-icmp": "MHDDoS (ICMP)",
    "mhddos-tcp": "MHDDoS (TCP)",
    "mhddos-udp": "MHDDoS (UDP)",
    "miniz": "miniZ (GPU)",
    "nbminer": "NBMiner (GPU)",
    "nicehash": "NiceHash (GPU)",
    "onezerominer": "OneZeroMiner (GPU)",
    "petya": "Petya",
    "pyflooder": "PyFlooder (HTTP)",
    "randomware": "Randomware",
    "ransomware-poc": "Ransomware-PoC",
    "rex": "Rex",
    "slowloris": "Slowloris (HTTP)",
    "srbminer": "SRBMiner Multi (GPU)",
    "t-rex": "T-Rex (GPU)",
    "thanos": "Thanos",
    "wannacry": "WannaCry",
    "wildrig": "WildRig Multi (GPU)",
    "xmrig": "XMRig (CPU)",
}
ATTACK_TYPE = "Attack Type"
ATTACK_TYPES = {
    "cryptojacking": "Cryptojacking",
    "denial-of-service": "Denial of Service",
    "ransomware": "Ransomware",
}

CLEANED_DATA = {"%": "", ",": ".", "W": "", "°C": "", "�C": ""}
CPU_GRAPHICS_POWER = "CPU Graphics Power (W)"
CPU_POWER = "CPU Power (W)"
CPU_POWER_CORES = "CPU Power Cores (W)"
CPU_TEMPERATURE = "CPU Temperature (°C)"
CPU_TEMPERATURE_CORE_1 = "CPU Temperature Core #1 (°C)"
CPU_TEMPERATURE_CORE_2 = "CPU Temperature Core #2 (°C)"
CPU_TEMPERATURE_CORE_3 = "CPU Temperature Core #3 (°C)"
CPU_TEMPERATURE_CORE_4 = "CPU Temperature Core #4 (°C)"
CPU_TEMPERATURE_MILLI = "CPU Temperature (m°C)"
CPU_USAGE = "CPU Usage (%)"
CPU_USAGE_IDLE = "CPU Usage Idle (%)"
CPU_USAGE_SYSTEM = "CPU Usage System (%)"
CPU_USAGE_USER = "CPU Usage User (%)"
CPU_USAGE_WAIT = "CPU Usage Wait %"
CURRENT = "Current (A)"
CURRENT_MILLI = "Current (mA)"

ENCODING_DEFAULT = "utf-8-sig"
EXTENSION_CSV = "csv"
EXTENSION_HTML = "html"
EXTENSION_LOG = "log"

FIGURES_OUTPUT_DIRECTORY_PATH = "output/figures"

GPU_MEMORY_USAGE = "GPU Memory Usage (%)"
GPU_POWER = "GPU Power (W)"
GPU_TEMPERATURE = "GPU Temperature (°C)"
GPU_USAGE = "GPU Usage (%)"

HOST = "Host"
HOST_NAMES = {
    "d-link": "D-Link DIR-822",
    "hosafe": "HOSAFE HX-2PT1",
    "huawei": "Huawei H151-381",
    "m1": "Apple M1 Pro",
    "macbook": "Apple MacBook Pro i7 2013",
    "msi": "Windows 11 i7 GeForce RTX 4060 Laptop",
    "rpi3b": "Raspberry Pi 3B 1GB",
    "rpi4b2": "Raspberry Pi 4B 2GB",
    "rpi4b4": "Raspberry Pi 4B 4GB",
    "rpi4b8": "Raspberry Pi 4B 8GB",
    "rpi5": "Raspberry Pi 5",
    "tp-link": "TP-Link Tapo C200",
    "victus": "HP Victus 16-d0417nf",
    "vm": "Windows 10 VM",
    "zenbook": "ASUS Zenbook UX51VZ",
}

MEASUREMENT = "Measurement"
MEASUREMENT_TOOLS = {
    "acs712": "ACS712",
    "kuman": "Kuman KW47",
    "nmon": "nmon",
    "openhardwaremonitor": "Open Hardware Monitor",
    "prometheus": "Prometheus",
    "system": "System",
}
MEMORY_USAGE = "Memory Usage (%)"
MEMORY_USAGE_FREE_MO = "Memory Free (Mo)"
MEMORY_USAGE_TOTAL_MO = "Memory Usage (Mo)"
MODE = "Mode"

PLOT_SCATTERS_CONFIGURATIONS = {
    "cryptojacking": {"color": "#1f77b4", "marker": "o"},
    "denial-of-service": {"color": "#ff7f0e", "marker": "s"},
    "ransomware": {"color": "#2ca02c", "marker": "D"},
}
POWER = "Power (W)"
PREPROCESSED = "preprocessed"
PREPROCESSED_DATA_DIRECTORY_PATH = "data/preprocessed"
PROCESSED = "processed"
PROCESSED_DATA_DIRECTORY_PATH = "data/processed"

RAW = "raw"
RAW_DATA_DIRECTORY_PATH = "data/raw"
REGEX_PATTERN_GOOGLE_VISUALIZATION_ARRAY = r"var\s+(data_[A-Za-z0-9_]+)\s*=\s*google\.visualization\.arrayToDataTable\(\s*\[(.*?)\]\s*\)"
REGEX_PATTERN_GOOGLE_VISUALIZATION_ARRAY_HEADER = r"\[\s*(?:\{.*?\}\s*,\s*)?(.*?)\]"
REGEX_PATTERN_GOOGLE_VISUALIZATION_ARRAY_ROW = r"\['Date\((.*?)\)'\s*,\s*(.*?)\]"
REPORTED_ATTACKS = {
    "CoinIMP (CPU) (10%)": "C01 (CPU)",
    "CoinIMP (CPU) (20%)": "C02 (CPU)",
    "CoinIMP (CPU) (30%)": "C03 (CPU)",
    "CoinIMP (CPU) (40%)": "C04 (CPU)",
    "CoinIMP (CPU) (50%)": "C05 (CPU)",
    "CoinIMP (CPU) (100%)": "C06 (CPU)",
    "CoinIMP (CPU) (100%)": "C06 (CPU)",
    "GMiner (GPU)": "C07 (GPU)",
    "lolMiner (GPU)": "C08 (GPU)",
    "miniZ (GPU)": "C09 (GPU)",
    "NBMiner (GPU)": "C10 (GPU)",
    "NiceHash (GPU)": "C11 (GPU)",
    "OneZeroMiner (GPU)": "C12 (GPU)",
    "SRBMiner Multi (GPU)": "C13 (GPU)",
    "T-Rex (GPU)": "C14 (GPU)",
    "WildRig Multi (GPU)": "C15 (GPU)",
    "XMRig (CPU)": "C16 (CPU)",
    "GoldenEye (HTTP)": "D01 (HTTP)",
    "Goloris (HTTP)": "D02 (HTTP)",
    "Hping3 (SYN)": "D03 (SYN)",
    "HULK (HTTP)": "D04 (HTTP)",
    "MHDDoS (ICMP)": "D05 (ICMP)",
    "MHDDoS (TCP)": "D06 (TCP)",
    "MHDDoS (UDP)": "D07 (UDP)",
    "PyFlooder (HTTP)": "D08 (HTTP)",
    "Slowloris (HTTP)": "D09 (HTTP)",
    "Bstry": "R01",
    "Jigsaw": "R02",
    "Petya": "R03",
    "Randomware": "R04",
    "Ransomware-PoC": "R05",
    "Rex": "R06",
    "Thanos": "R07",
    "WannaCry": "R08",
}
REPORTED_DATA_DIRECTORY_PATH = "data/reported"
REPORTED_HOSTS = {
    "Apple M1 Pro": "H01",
    "Apple MacBook Pro i7 2013": "H02",
    "ASUS Zenbook UX51VZ": "H03",
    "HP Victus 16-d0417nf": "H04",
    "Windows 10 VM": "H05",
    "Windows 11 i7 GeForce RTX 4060 Laptop": "H06",
    "D-Link DIR-822": "L01",
    "HOSAFE HX-2PT1": "L02",
    "Huawei H151-381": "L03",
    "Raspberry Pi 3B 1GB": "L04",
    "Raspberry Pi 4B 2GB": "L05",
    "Raspberry Pi 4B 4GB": "L06",
    "Raspberry Pi 4B 8GB": "L07",
    "Raspberry Pi 5": "L08",
    "TP-Link Tapo C200": "L09",
}
REPORTED_METRICS = [
    CPU_POWER,
    CPU_TEMPERATURE,
    CPU_USAGE,
    GPU_MEMORY_USAGE,
    GPU_TEMPERATURE,
    GPU_USAGE,
    MEMORY_USAGE,
    POWER,
]
RUN = "Run"

STUDY = "Study"

TABLES_OUTPUT_DIRECTORY_PATH = "output/tables"
TIME_MILLI = ".000"
TIME_ZERO_LEFT = "00:"
TIME_ZERO_RIGHT = ":00"
TIMESTAMP = "Timestamp"
TIMESTAMP_RELATIVE = "Relative Time (s)"

VOLTAGE = "Voltage (V)"
VOLTAGE_ADJUSTED = "Voltage Adjusted (V)"

CLEANED_HEADERS = {
    "Consommation (W)": POWER,
    "Courant (A)": CURRENT,
    "CPU (%)": CPU_USAGE,
    "CPU Core #1": CPU_TEMPERATURE_CORE_1,
    "CPU Core #1 Temp (°C)": CPU_TEMPERATURE_CORE_1,
    "CPU Core #1 Temp (�C)": CPU_TEMPERATURE_CORE_1,
    "CPU Core #2": CPU_TEMPERATURE_CORE_2,
    "CPU Core #2 Temp (°C)": CPU_TEMPERATURE_CORE_2,
    "CPU Core #2 Temp (�C)": CPU_TEMPERATURE_CORE_2,
    "CPU Core #3": CPU_TEMPERATURE_CORE_3,
    "CPU Core #3 Temp (°C)": CPU_TEMPERATURE_CORE_3,
    "CPU Core #3 Temp (�C)": CPU_TEMPERATURE_CORE_3,
    "CPU Core #4": CPU_TEMPERATURE_CORE_4,
    "CPU Core #4 Temp (°C)": CPU_TEMPERATURE_CORE_4,
    "CPU Core #4 Temp (�C)": CPU_TEMPERATURE_CORE_4,
    "CPU Cores Power": CPU_POWER_CORES,
    "CPU Cores Power (W)": CPU_POWER_CORES,
    "CPU Graphics Power": CPU_GRAPHICS_POWER,
    "CPU Package": CPU_TEMPERATURE,
    "CPU Package Power": CPU_POWER,
    "CPU Package Power (W)": CPU_POWER,
    "CPU Package Temp (°C)": CPU_TEMPERATURE,
    "CPU Package Temp (�C)": CPU_TEMPERATURE,
    "CPU Temperature (Â°C)": CPU_TEMPERATURE,
    "CPU Total Load (%)": CPU_USAGE,
    "data_CPU_UTIL_Idle%": CPU_USAGE_IDLE,
    "data_CPU_UTIL_Sys%": CPU_USAGE_SYSTEM,
    "data_CPU_UTIL_User%": CPU_USAGE_USER,
    "data_CPU_UTIL_Wait%": CPU_USAGE_WAIT,
    "data_DISKBSIZE_mmcblk0": "Disk mmcblk0 Block Size (Ko)",
    "data_DISKBSIZE_mmcblk0p1": "Disk mmcblk0p1 Block Size (Ko)",
    "data_DISKBSIZE_mmcblk0p2": "Disk mmcblk0p2 Block Size (Ko)",
    "data_DISKBSIZE_mmcblk1": "Disk mmcblk1 Block Size (Ko)",
    "data_DISKBSIZE_mmcblk1p1": "Disk mmcblk1p1 Block Size (Ko)",
    "data_DISKBSIZE_mmcblk1p2": "Disk mmcblk1p2 Block Size (Ko)",
    "data_DISKBUSY_mmcblk0": "Disk mmcblk0 Usage (%)",
    "data_DISKBUSY_mmcblk0p1": "Disk mmcblk0p1 Usage (%)",
    "data_DISKBUSY_mmcblk0p2": "Disk mmcblk0p2 Usage (%)",
    "data_DISKBUSY_mmcblk1": "Disk mmcblk1 Usage (%)",
    "data_DISKBUSY_mmcblk1p1": "Disk mmcblk1p1 Usage (%)",
    "data_DISKBUSY_mmcblk1p2": "Disk mmcblk1p2 Usage (%)",
    "data_DISKREAD_mmcblk0": "Disk mmcblk0 Read (Ko/s)",
    "data_DISKREAD_mmcblk0p1": "Disk mmcblk0p1 Read (Ko/s)",
    "data_DISKREAD_mmcblk0p2": "Disk mmcblk0p2 Read (Ko/s)",
    "data_DISKREAD_mmcblk1": "Disk mmcblk1 Read (Ko/s)",
    "data_DISKREAD_mmcblk1p1": "Disk mmcblk1p1 Read (Ko/s)",
    "data_DISKREAD_mmcblk1p2": "Disk mmcblk1p2 Read (Ko/s)",
    "data_DISKWRITE_mmcblk0": "Disk mmcblk0 Write (Ko/s)",
    "data_DISKWRITE_mmcblk0p1": "Disk mmcblk0p1 Write (Ko/s)",
    "data_DISKWRITE_mmcblk0p2": "Disk mmcblk0p2 Write (Ko/s)",
    "data_DISKWRITE_mmcblk1": "Disk mmcblk1 Write (Ko/s)",
    "data_DISKWRITE_mmcblk1p1": "Disk mmcblk1p1 Write (Ko/s)",
    "data_DISKWRITE_mmcblk1p2": "Disk mmcblk1p2 Write (Ko/s)",
    "data_DISKXFER_mmcblk0": "Disk mmcblk0 Transfers",
    "data_DISKXFER_mmcblk0p1": "Disk mmcblk0p1 Transfers",
    "data_DISKXFER_mmcblk0p2": "Disk mmcblk0p2 Transfers",
    "data_DISKXFER_mmcblk1": "Disk mmcblk1 Transfers",
    "data_DISKXFER_mmcblk1p1": "Disk mmcblk1p1 Transfers",
    "data_DISKXFER_mmcblk1p2": "Disk mmcblk1p2 Transfers",
    "data_FORKEXEC_exec": "Process Execs",
    "data_FORKEXEC_fork": "Process Forks",
    "data_JFS_/": "JFS Usage (%)",
    "data_JFS_/boot/firmware": "JFS boot/firmware Usage (%)",
    "data_JFS_/dev": "JFS dev Usage (%)",
    "data_JFS_/run": "JFS run Usage (%)",
    "data_MEM_LINUX_active": "Memory Active (Mo)",
    "data_MEM_LINUX_buffers": "Memory Buffers (Mo)",
    "data_MEM_LINUX_cached": "Memory Cached (Mo)",
    "data_MEM_LINUX_inactive": "Memory Inactive (Mo)",
    "data_MEM_LINUX_memfree": MEMORY_USAGE_FREE_MO,
    "data_MEM_LINUX_memtotal": MEMORY_USAGE_TOTAL_MO,
    "data_NET_eth0-read-KB/s": "Network eth0 Received (Ko/s)",
    "data_NET_eth0-write-KB/s": "Network eth0 Sent (Ko/s)",
    "data_NET_lo-read-KB/s": "Network lo Received (Ko/s)",
    "data_NET_lo-write-KB/s": "Network lo Sent (Ko/s)",
    "data_NET_wlan0-read-KB/s": "Network wlan0 Received (Ko/s)",
    "data_NET_wlan0-write-KB/s": "Network wlan0 Sent (Ko/s)",
    "data_NETPACKET_eth0-read/s": "Network Packet eth0 Received",
    "data_NETPACKET_eth0-write/s": "Network Packet eth0 Sent",
    "data_NETPACKET_lo-read/s": "Network Packet lo Received",
    "data_NETPACKET_lo-write/s": "Network Packet lo Sent",
    "data_NETPACKET_wlan0-read/s": "Network Packet wlan0 Received",
    "data_NETPACKET_wlan0-write/s": "Network Packet wlan0 Sent",
    "data_PSWITCH_pswitch": "Process Switches",
    "data_RUNQBLOCK_Blocked": "Processes Blocked",
    "data_RUNQBLOCK_Runnable": "Processes Runnable",
    "data_SWAP_LINUX_swapfree": "Swap Free (Mo)",
    "data_SWAP_LINUX_swaptotal": "Swap Usage (Mo)",
    "Disque chiffré (%)": "Encrypted Disk Usage (%)",
    "Ecriture disque (Mo/s)": "Disk Write (Mo/s)",
    "Fichiers chiffrés": "Encrypted Files",
    "GPU Core": GPU_TEMPERATURE,
    "GPU Core Load (%)": GPU_USAGE,
    "GPU Core Temp (°C)": GPU_TEMPERATURE,
    "GPU Core Temp (�C)": GPU_TEMPERATURE,
    "GPU Memory Load (%)": GPU_MEMORY_USAGE,
    "GPU Power Consumption (W)": GPU_POWER,
    "Horodatage": TIMESTAMP,
    "Lecture disque (Mo/s)": "Disk Read (Mo/s)",
    "Power Consumption (W)": POWER,
    "Puissance (W)": POWER,
    "RAM (%)": MEMORY_USAGE,
    "RAM (Mo)": "Memory Usage (Mo)",
    "RAM Load (%)": MEMORY_USAGE,
    "RAM Usage (%)": MEMORY_USAGE,
    "Réseau (Ko/s)": "Network (Ko/s)",
    "Taille fichiers chiffres (Mo)": "Encrypted Files Size (Mo)",
    "Temps": TIMESTAMP,
    "Temps relatif (s)": TIMESTAMP_RELATIVE,
    "Température (°C)": CPU_TEMPERATURE,
    "Tension (V)": VOLTAGE,
    "Timestamp (s)": TIMESTAMP_RELATIVE,
    "Vitesse chiffrement (o/s)": "Encryption Speed (o/s)",
}

DATA_FILES = {
    "cryptojacking_coinimp-0%_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"idle": "09:22:00.000"}
    },
    "cryptojacking_coinimp-10%_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"attack": "03:52:00.000"}
    },
    "cryptojacking_coinimp-100%_macbook_kuman.csv": {
        "attack_configuration": {
            "idle": "01:00:00.000",
            "idle_browser_open": "01:03:00.000",
            "attack": "01:05:00.000",
            "recovery": "01:10:00.000",
        }
    },
    "cryptojacking_coinimp-100%_macbook_system.csv": {
        "attack_configuration": {
            "idle_buffer": "00:59:34.342",
            "idle": "01:00:00.000",
            "idle_browser_open": "01:03:00.000",
            "attack": "01:05:00.000",
            "recovery": "01:10:00.000",
        }
    },
    "cryptojacking_coinimp-100%_rpi3b_acs712.csv": {
        "missing_headers": [
            TIMESTAMP,
            VOLTAGE,
            VOLTAGE_ADJUSTED,
            CURRENT,
            POWER,
        ],
        "attack_configuration": ATTACK_MODE_45485055,
    },
    "cryptojacking_coinimp-100%_rpi3b_system.csv": {
        "attack_configuration": ATTACK_MODE_45485055
    },
    "cryptojacking_coinimp-100%_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"attack": "09:42:00.000"}
    },
    "cryptojacking_coinimp-20%_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"attack": "03:30:00.000"}
    },
    "cryptojacking_coinimp-30%_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"attack": "03:01:00.000"}
    },
    "cryptojacking_coinimp-40%_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"attack": "05:26:00.000"}
    },
    "cryptojacking_coinimp-50%_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"attack": "04:52:00.000"}
    },
    "cryptojacking_coinimp_m1_system.csv": {"attack_configuration": 1},
    "cryptojacking_gminer_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "11:51:00.000",
            "attack": "11:56:00.000",
            "recovery": "12:04:00.000",
        }
    },
    "cryptojacking_lolminer_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "09:35:00.000",
            "attack": "09:40:00.000",
            "recovery": "09:46:00.000",
        }
    },
    "cryptojacking_miniz_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "16:02:00.000",
            "attack": "16:09:00.000",
            "recovery": "16:17:00.000",
        }
    },
    "cryptojacking_nbminer_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "08:00:00.000",
            "attack": "08:04:00.000",
            "recovery": "08:10:00.000",
        }
    },
    "cryptojacking_nicehash_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "19:48:00.000",
            "attack": "19:54:00.000",
            "recovery": "19:59:00.000",
        }
    },
    "cryptojacking_onezerominer_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "00:21:00.000",
            "attack": "00:29:00.000",
            "recovery": "00:35:00.000",
        }
    },
    "cryptojacking_srbminer_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "20:20:00.000",
            "attack": "20:25:00.000",
            "recovery": "20:30:00.000",
        }
    },
    "cryptojacking_t-rex_msi_system.csv": {"attack_configuration": 1},
    "cryptojacking_t-rex_zenbook_openhardwaremonitor.csv": {
        "attack_configuration": {"idle": "11:06:00.000", "attack": "11:10:42.000"}
    },
    "cryptojacking_wildrig_victus_openhardwaremonitor.csv": {
        "attack_configuration": {
            "idle": "11:55:00.000",
            "attack": "12:00:00.000",
            "recovery": "12:06:00.000",
        }
    },
    "cryptojacking_xmrig_rpi3b_system.csv": {"attack_configuration": 1},
    "cryptojacking_xmrig_rpi4b2_system.csv": {"attack_configuration": 1},
    "cryptojacking_xmrig_rpi4b4_system_01.csv": {"attack_configuration": 1},
    "cryptojacking_xmrig_rpi4b4_system_02.csv": {"attack_configuration": 1},
    "cryptojacking_xmrig_rpi4b4_system_03.csv": {"attack_configuration": 1},
    "cryptojacking_xmrig_rpi5_system.csv": {"attack_configuration": 1},
    "denial-of-service_goldeneye_rpi4b4_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_goldeneye_rpi4b4_nmon.html": {"attack_configuration": 200},
    "denial-of-service_goldeneye_rpi4b4_system.log": {
        "missing_headers": [CPU_TEMPERATURE_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_goloris_hosafe_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_goloris_rpi4b4_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_goloris_rpi4b4_nmon.html": {"attack_configuration": 200},
    "denial-of-service_hping3_d-link_kuman.csv": {"attack_configuration": 1},
    "denial-of-service_hping3_hosafe_acs712.csv": {"attack_configuration": 1},
    "denial-of-service_hping3_huawei_acs712.csv": {"attack_configuration": 1},
    "denial-of-service_hping3_tp-link_acs712.csv": {"attack_configuration": 1},
    "denial-of-service_hulk_rpi4b4_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_hulk_rpi4b4_nmon.html": {"attack_configuration": 200},
    "denial-of-service_hulk_rpi4b4_system.log": {
        "missing_headers": [CPU_TEMPERATURE_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_mhddos-icmp_hosafe_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_mhddos-icmp_rpi4b4_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_mhddos-icmp_rpi4b4_nmon.html": {"attack_configuration": 200},
    "denial-of-service_mhddos-tcp_hosafe_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_mhddos-tcp_rpi4b4_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_mhddos-tcp_rpi4b4_nmon.html": {"attack_configuration": 200},
    "denial-of-service_mhddos-udp_hosafe_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_mhddos-udp_rpi4b4_acs712.log": {
        "missing_headers": [CURRENT_MILLI],
        "attack_configuration": 200,
    },
    "denial-of-service_mhddos-udp_rpi4b4_nmon.html": {"attack_configuration": 200},
    "denial-of-service_pyflooder_rpi4b8_system.csv": {
        "attack_configuration": {
            "idle": "03:32:00.000",
            "attack": "03:35:00.000",
            "recovery": "03:57:10.000",
        }
    },
    "denial-of-service_slowloris_rpi4b2_acs712_01.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "denial-of-service_slowloris_rpi4b2_acs712_02.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "denial-of-service_slowloris_rpi4b2_acs712_03.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "denial-of-service_slowloris_rpi4b2_system_01.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "denial-of-service_slowloris_rpi4b2_system_02.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "denial-of-service_slowloris_rpi4b2_system_03.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "ransomware_bstry_rpi4b2_acs712.csv": {"attack_configuration": ATTACK_MODE_000101},
    "ransomware_bstry_rpi4b2_system.csv": {"attack_configuration": ATTACK_MODE_000101},
    "ransomware_jigsaw_rpi4b4_prometheus.csv": {
        "attack_configuration": ATTACK_MODE_000510
    },
    "ransomware_jigsaw_vm_prometheus.csv": {"attack_configuration": ATTACK_MODE_000510},
    "ransomware_petya_rpi4b4_prometheus.csv": {
        "attack_configuration": ATTACK_MODE_000510
    },
    "ransomware_petya_vm_prometheus.csv": {"attack_configuration": ATTACK_MODE_000510},
    "ransomware_randomware_rpi4b2_acs712.csv": {
        "attack_configuration": ATTACK_MODE_000202
    },
    "ransomware_randomware_rpi4b2_system.csv": {
        "attack_configuration": ATTACK_MODE_000202
    },
    "ransomware_ransomware-poc_rpi4b2_acs712_01.csv": {
        "attack_configuration": ATTACK_MODE_000103
    },
    "ransomware_ransomware-poc_rpi4b2_acs712_02.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "ransomware_ransomware-poc_rpi4b2_system_01.csv": {
        "attack_configuration": ATTACK_MODE_000103
    },
    "ransomware_ransomware-poc_rpi4b2_system_02.csv": {
        "attack_configuration": ATTACK_MODE_000204
    },
    "ransomware_rex_rpi4b4_prometheus.csv": {
        "attack_configuration": ATTACK_MODE_000510
    },
    "ransomware_rex_vm_prometheus.csv": {"attack_configuration": ATTACK_MODE_000510},
    "ransomware_thanos_rpi4b4_prometheus.csv": {
        "attack_configuration": ATTACK_MODE_000510
    },
    "ransomware_thanos_vm_prometheus.csv": {"attack_configuration": ATTACK_MODE_000510},
    "ransomware_wannacry_rpi4b4_prometheus.csv": {
        "attack_configuration": ATTACK_MODE_000510
    },
    "ransomware_wannacry_vm_prometheus.csv": {
        "attack_configuration": ATTACK_MODE_000510
    },
}

ORDERED_HEADERS = [
    ATTACK,
    HOST,
    RUN,
    MODE,
    CPU_POWER,
    CPU_TEMPERATURE,
    CPU_USAGE,
    GPU_MEMORY_USAGE,
    GPU_TEMPERATURE,
    GPU_USAGE,
    MEMORY_USAGE,
    POWER,
    ATTACK_TYPE,
    MEASUREMENT,
    TIMESTAMP,
    TIMESTAMP_RELATIVE,
    CPU_GRAPHICS_POWER,
    CPU_TEMPERATURE_CORE_1,
    CPU_TEMPERATURE_CORE_2,
    CPU_TEMPERATURE_CORE_3,
    CPU_TEMPERATURE_CORE_4,
    CPU_TEMPERATURE_MILLI,
    CPU_POWER_CORES,
    CPU_USAGE_IDLE,
    CPU_USAGE_SYSTEM,
    CPU_USAGE_USER,
    CPU_USAGE_WAIT,
    CURRENT,
    CURRENT_MILLI,
    "Disk mmcblk0 Block Size (Ko)",
    "Disk mmcblk0 Read (Ko/s)",
    "Disk mmcblk0 Transfers",
    "Disk mmcblk0 Usage (%)",
    "Disk mmcblk0 Write (Ko/s)",
    "Disk mmcblk0p1 Block Size (Ko)",
    "Disk mmcblk0p1 Read (Ko/s)",
    "Disk mmcblk0p1 Transfers",
    "Disk mmcblk0p1 Usage (%)",
    "Disk mmcblk0p1 Write (Ko/s)",
    "Disk mmcblk0p2 Block Size (Ko)",
    "Disk mmcblk0p2 Read (Ko/s)",
    "Disk mmcblk0p2 Transfers",
    "Disk mmcblk0p2 Usage (%)",
    "Disk mmcblk0p2 Write (Ko/s)",
    "Disk mmcblk1 Block Size (Ko)",
    "Disk mmcblk1 Read (Ko/s)",
    "Disk mmcblk1 Transfers",
    "Disk mmcblk1 Usage (%)",
    "Disk mmcblk1 Write (Ko/s)",
    "Disk mmcblk1p1 Block Size (Ko)",
    "Disk mmcblk1p1 Read (Ko/s)",
    "Disk mmcblk1p1 Transfers",
    "Disk mmcblk1p1 Usage (%)",
    "Disk mmcblk1p1 Write (Ko/s)",
    "Disk mmcblk1p2 Block Size (Ko)",
    "Disk mmcblk1p2 Read (Ko/s)",
    "Disk mmcblk1p2 Transfers",
    "Disk mmcblk1p2 Usage (%)",
    "Disk mmcblk1p2 Write (Ko/s)",
    "Disk Read (Mo/s)",
    "Disk Write (Mo/s)",
    "Encrypted Disk Usage (%)",
    "Encrypted Files",
    "Encrypted Files Size (Mo)",
    "Encryption Speed (o/s)",
    GPU_POWER,
    "JFS boot/firmware Usage (%)",
    "JFS dev Usage (%)",
    "JFS run Usage (%)",
    "JFS Usage (%)",
    "Memory Active (Mo)",
    "Memory Buffers (Mo)",
    "Memory Cached (Mo)",
    "Memory Free (Mo)",
    "Memory Inactive (Mo)",
    "Memory Total (Mo)",
    "Memory Usage (Mo)",
    "Network (Ko/s)",
    "Network eth0 Received (Ko/s)",
    "Network eth0 Sent (Ko/s)",
    "Network lo Received (Ko/s)",
    "Network lo Sent (Ko/s)",
    "Network wlan0 Received (Ko/s)",
    "Network wlan0 Sent (Ko/s)",
    "Network Packet eth0 Received",
    "Network Packet eth0 Sent",
    "Network Packet lo Received",
    "Network Packet lo Sent",
    "Network Packet wlan0 Received",
    "Network Packet wlan0 Sent",
    "Process Execs",
    "Process Forks",
    "Process Switches",
    "Processes Blocked",
    "Processes Runnable",
    "Swap Free (Mo)",
    "Swap Usage (Mo)",
    VOLTAGE,
    VOLTAGE_ADJUSTED,
]
