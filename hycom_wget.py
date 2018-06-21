import subprocess
from multiprocessing import Process
# from rainbowfish.decorator import wget_continue


# @wget_continue
def wget_down(save_path, url):
    cmd = "wget -c -r -N --accept=nc -t 0 -T 10 -P %s %s" % (save_path, url)
    subprocess.Popen(cmd, shell=True)
    # obj = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    # print("****************")
    # print(obj.pid)
    # save_path_detail = "/home/yangyubo/data/downloads/Hycom/ftp.hycom.org/datasets/GLBa0.08/expt_90.2/data"
    # code_path = "/home/yangyubo/data/code/hycom_wget.py"
    # return obj, save_path_detail, code_path


if __name__ == '__main__':
    save_path = "/home/yangyubo/data/downloads/Share2/downloads/Hycom"
    url_list = [
    "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_90.2/data/",
    "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_90.3/data/",
    "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_90.6/data/",
    "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_90.8/data/",
    "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_91.0/data/",
    "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_91.1/data/",
    "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_91.2/data/",
    "ftp://ftp.hycom.org/datasets/GLBa0.08/latest/"
    ]
    for url in url_list:
        pro = Process(target=wget_down, args=(save_path, url))
        pro.start()
        pro.join()

