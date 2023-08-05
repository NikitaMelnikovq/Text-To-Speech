import os, json, requests, time 
def text_to_speech(text="hello world"):

    url ="https://api.edenai.run/v2/audio/text_to_speech"

    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjg2ZjkxZjUtYWQ1Zi00ZWQ0LTgxNDktODVmODY5YzQ3ZmI0IiwidHlwZSI6ImFwaV90b2tlbiJ9.V-5G_WbBy9M3Yb_o3exQ_XDtpXntHup5FjVYoA-qXzk'} 

    with open(file='text.txt', mode='r', encoding="utf-8") as file:
        src = file.read()

    payload = {
        "providers": 'google',
        "language": 'en-US',
        "option": 'FEMALE',
        "text": src.strip(),
        "lovoai": "en-US_Rose Baker"

    }
    
    response = requests.post(url=url, headers=headers, json=payload)

    result = json.loads(response.text)

    t = time.time()
    with open(f'{t}.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    audio = result.get('google').get('audio_resource_url')

    r = requests.get(audio)

    with open(f"{t}.wav", 'wb') as file:
        file.write(r.content)

def main():
    text_to_speech()

if __name__ == '__main__':
    main()
