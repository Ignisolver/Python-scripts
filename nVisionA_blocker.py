def f():
    """
    1. Uruchomić tą funkcje jako administrator
    2. W folderze C:\Program Files (x86)\A cośtam cośtam ręcznie usówać pliki zaczynając od aplikacji
    2.a - te pliki są używane przez wątki o nazwach takich jak powyżej i trudno je usunąć trzeba się wstrzelić w chwilę kiedy dan plik akurat nie jest otwarty
    3. Program powinien wyświetlić SHUTTED DOWN
    """
    import subprocess
    import re
    names = ["AxDBSrvrA.exe",
    "AxenceSvcGuard.exe",
    "nVisionA.exe",
    "nVisionA_DG.exe"]

    path = r'C:\Program Files (x86)\Axence'
    kill_cmd = f'rmdir "{path}"'

    def get_processes():
        result = subprocess.check_output("tasklist", shell=True)
        output = str(result)
        tasks = output.split(r'\r\n')
        p = []
        for task in tasks:
            m = re.match(r"(.+?) +(\d+) (.+?) +(\d+) +(\d+.* K).*",task)
            if m is not None:
                p.append({"image":m.group(1),
                            "pid":m.group(2),
                            "session_name":m.group(3),
                            "session_num":m.group(4),
                            "mem_usage":m.group(5)
                            })
        return p

    def killim():
        while True:
            processes = get_processes()
            pids = []
            for process in processes:
                if process["image"] in names:
                    pids.append(process["pid"])
            if len(pids) == 0:
                print("SHUTTED DOWN!!!")
            for pid in pids:
                polec = f"taskkill /PID {pid} /F"
                try:
                    subprocess.check_output(polec, shell=True)
                except:
                    print(f"can not close {pid}")

    killim()
