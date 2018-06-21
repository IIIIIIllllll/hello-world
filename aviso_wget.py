import subprocess
from multiprocessing import Process
import time
import sys
# from rainbowfish.decorator import wget_continue


# @wget_continue
def wget_aviso(index, url):
    if 0 <= index <= 1:
        save_path = "/home/yangyubo/data/downloads/Share1/downloads/Aviso/mwind_mswh"
    else:
        save_path = "/home/yangyubo/data/downloads/Share1/downloads/Aviso/time_kind"
    cmd = "wget -r -N -c -t 5 -T 10 -P %s %s" % (save_path, url)
    subprocess.Popen(cmd, shell=True)
    # obj = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    # print("****************")
    # print(obj.pid)
    # save_path_detail = "/home/yangyubo/data/downloads/Aviso/time_kind/avisoftp.cnes.fr/AVISO/pub/saral/ogdr_t"
    # code_path = "home/yangyubo/data/code/aviso_wget.py"
    # return obj, save_path_detail, code_path


if __name__ == '__main__':
    url_list = [
        # mwind 每日6:40更新
        "ftp://m15995791473%40163.com:dKMYdk@ftp-access.aviso.altimetry.fr/wind-wave/nrt/mwind/merged",
        # mswh
        "ftp://m15995791473%40163.com:dKMYdk@ftp-access.aviso.altimetry.fr/wind-wave/nrt/mswh/merged",
        # GDR（延时时间）
        "ftp://avisoftp.cnes.fr/AVISO/pub/jason-3/gdr_d",
        "ftp://avisoftp.cnes.fr/AVISO/pub/saral/gdr_t",
        "ftp://avisoftp.cnes.fr/AVISO/pub/jason-2/gdr_d",
        "ftp://avisoftp.cnes.fr/AVISO/pub/jason-1/gdr_e",
        # IGDR （近实时）
        # "ftp://avisoftp.cnes.fr/AVISO/pub/jason-3/igdr",
        # "ftp://avisoftp.cnes.fr/AVISO/pub/saral/igdr_t",
        # "ftp://avisoftp.cnes.fr/AVISO/pub/jason-2/igdr",
        # # 实时
        # "ftp://avisoftp.cnes.fr/AVISO/pub/saral/ogdr_t"
    ]
    cmd_list = []
    for index, url in enumerate(url_list):
        pro = Process(target=wget_aviso, args=(index, url))
        pro.start()
        pro.join()
        # wget_aviso(index, url)

