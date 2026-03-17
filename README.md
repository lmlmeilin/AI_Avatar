# AI_Avatar

https://docs.google.com/document/d/1etimxiq7JTu8011Plbg-E2a9RNP40q0kgSNv6AIMpnM/edit?usp=sharing

## Download requirements.txt
```bash 
pip install -r requirements.txt
``` 
## Create input.wav
python create_wav.py 

## Create response.wav
python test_run.py

## Generate avatar video 
### Copy avatar.png and response.wav over to SadTalker directory

cd SadTalker 

conda create -n sadtalker python=3.8

conda activate sadtalker

pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

conda install ffmpeg

pip install -r requirements.txt

python inference.py --driven_audio response.wav --source_image avatar.png --result_dir results

### Video can be found in SadTalker > results folder
