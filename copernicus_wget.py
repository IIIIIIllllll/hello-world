import subprocess


def wget_down(save_path, url):
    cmd = "wget -r -N -c -t 5 -T 10 -P %s %s" % (save_path, url)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    save_path = "/home/yangyubo/data/downloads/Share1/downloads/Copernicus"
    url_list = [
        "ftp://dwang6:DingqiCMEMS2017@nrt.cmems-du.eu/Core/GLOBAL_ANALYSIS_FORECAST_PHYS_001_015/",
        "ftp://dwang6:DingqiCMEMS2017@nrt.cmems-du.eu/Core/OCEANCOLOUR_GLO_OPTICS_L3_NRT_OBSERVATIONS_009_030/",
        "ftp://dwang6:DingqiCMEMS2017@nrt.cmems-du.eu/Core/OCEANCOLOUR_GLO_CHL_L3_NRT_OBSERVATIONS_009_032/",
        "ftp://dwang6:DingqiCMEMS2017@ftp.sltac.cls.fr/Core/SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046/"
    ]
    for url in url_list:
        wget_down(save_path, url)


