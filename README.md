UTAU、人力Vocaloid相关脚本与工具的存放处。不定期更新。

process_ibm_json.py
----
根据IBM Watson Speech to Text (https://www.ibm.com/watson/services/speech-to-text/) 返回的json与原始音频文件，将整段音频分割为单音节发音，供UTAU等软件使用。目前仅支持中文音频。

Watson Speech to Text的使用例：

    curl -X POST -u "用户名":"密码" --header "Content-Type: audio/wav" --data-binary "@音频文件.wav" "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=zh-CN_BroadbandModel&word_confidence=true&timestamps=true"  --output curl_result.json
