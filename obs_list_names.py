from obsws_python import ReqClient
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
HOST=os.getenv('OBS_HOST','localhost'); PORT=int(os.getenv('OBS_PORT',4455)); PASS=os.getenv('OBS_PASSWORD','R7D_News_2025')

c=ReqClient(host=HOST, port=PORT, password=PASS)

print('--- Inputs ---')
res=c.get_input_list()
inputs = res.get('inputs') if isinstance(res, dict) else getattr(res,'inputs',[])
for i in inputs:
    name = i.get('inputName') if isinstance(i, dict) else getattr(i,'inputName',None)
    kind = i.get('inputKind') if isinstance(i, dict) else getattr(i,'inputKind',None)
    print(f"- {name}  ({kind})")

print('\n--- Scenes ---')
sc=c.get_scene_list()
scenes = sc.get('scenes') if isinstance(sc, dict) else getattr(sc,'scenes',[])
for s in scenes:
    name = s.get('sceneName') if isinstance(s, dict) else getattr(s,'sceneName',None)
    print(f"- {name}")
