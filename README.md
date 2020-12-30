# pymqtt-docker
一個在python上運行mqtt的docker鏡像

## 依賴
在使用之前。 你需要安裝`docker`在你的系統中. 你可以點擊[Docker](https://www.docker.com "Open") 獲取詳細資料

## 安裝
下載所有的文件，然後在文件根目錄執行：
```sh
sh ./build.sh
```

## 使用

執行以下命令，並同時把你的主體目錄掛載到客體上。
```sh
docker run --name mqtt -v {$YOUR_MOUNT_DIR}:/mqtt_main/data/ -itd mayerlam/mqtt
```
然後在你掛載的目錄下，應該會創建了一個文件`Connector.py`。在一開始裡面帶有進行mqtt連接的模板，你可以修改它，然後執行

```sh
docker exec -it mqtt sh run.sh
```
