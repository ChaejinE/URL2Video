from yaml.loader import FullLoader
from downloader import Youtube

def main(cfg):
    from tqdm import tqdm
    method = cfg["method"]
    
    if method == "youtube":
        print("Downloading...")
        for url in tqdm(cfg["url"]):
            yt = Youtube(url, cfg["save_dir"])
            yt.download(resolution=cfg["resolution"])
        print("Download Success")
        
if __name__ == "__main__":
    import yaml
    
    with open("./downloader_cfg.yaml", 'r') as f:
        config = yaml.load(f, Loader=FullLoader)

    main(config)
    