import subprocess


def china_argo_wget(save_path, url):
    cmd = "wget -r -N -c -t 5 -T 10 -P %s %s" % (save_path, url)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    save_path = "/home/yangyubo/data/downloads/Share1/downloads/China_argo"
    url = "ftp://ftp.argo.org.cn/pub/ARGO/china/ncfiles/"
    china_argo_wget(save_path, url)
