UTAU、人力Vocaloid相关脚本与工具的存放处。不定期更新。

## process_ibm_json.py
根据[IBM Watson Speech to Text](https://www.ibm.com/watson/services/speech-to-text/)返回的json与原始音频文件，将整段音频分割为单音节发音，供UTAU等软件使用。目前仅支持中文音频。

使用例：
`python process_ibm_json.py [JSON文件] [原始WAV音频] [置信度阈值(0~1)] [音节时长阈值(秒)]`

Watson Speech to Text的使用教程：
https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-gettingStarted#getting-started-tutorial
