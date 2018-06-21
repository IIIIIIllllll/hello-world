import subprocess
from multiprocessing import Process


def wget_down(save_path, url):
    cmd = "wget -r -N -c --accept=nc -t 5 -T 10 -P %s %s" % (save_path, url)
    subprocess.Popen(cmd, shell=True)


if __name__ == '__main__':
    save_path = r"/home/yangyubo/data/downloads/Share2/downloads/Ncep"
    url_list = [
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.marine/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.pac.ocean/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis.derived/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis2/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis2.dailyavgs/",
    "ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis2.derived"
    ]
    for url in url_list:
        pro = Process(target=wget_down, args=(save_path, url))
        pro.start()
        pro.join()
