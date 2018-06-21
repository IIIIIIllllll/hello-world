import subprocess


def wget_down(save_path, url):
    cmd = "wget -r -c -N -t 5 -T 10 -P %s %s" % (save_path, url)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    save_path = r"/home/yangyubo/data/downloads/Share1/downloads/French_argo"
    url_list = [
    "ftp://ftp.ifremer.fr/ifremer/argo/geo/atlantic_ocean/",
    "ftp://ftp.ifremer.fr/ifremer/argo/geo/indian_ocean/",
    "ftp://ftp.ifremer.fr/ifremer/argo/geo/pacific_ocean/"
    ]
    for url in url_list:
        wget_down(save_path, url)
