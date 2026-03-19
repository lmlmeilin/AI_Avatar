# To run streamlit app, run the following commands in the AI_Avatar directory:
```bash
conda create -n ai_avatar python=3.8 -y
conda activate ai_avatar
pip install -r requirements.txt
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
pip install "lmdb<1.4"
pip install -r SadTalker/requirements.txt
conda install ffmpeg -y
pip install streamlit
streamlit run app.py
```