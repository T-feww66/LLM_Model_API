docker build -t api_web_leech_truyen_audio .

docker run -d --restart always -v /root/dir_api_web_leech_truyen_audio:/_app_/utils/download --name api_web_leech_truyen_audio -p 60074:60074 api_web_leech_truyen_audio

docker save -o api_web_leech_truyen_audio.tar api_web_leech_truyen_audio

docker load -i api_web_leech_truyen_audio.tar


docker exec -it api_web_leech_truyen_audio bash

pip freeze: kiem tra cac lib va phien ban da cai
pip freeze > requirements.txt


teen thuong hieu, tong danh gia thuong hieu

ten thuong hieu -> json database

//div[@role='button'and @id]
