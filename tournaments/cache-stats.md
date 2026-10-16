# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0042-20261016-110957)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 117 | 1619981 | 1368576 | 84.5% | 85.5% |
| GLM 5.3 Flash | 96 | 1394550 | 1170752 | 84.0% | 85.4% |
| GPT-6.1 Sol | 155 | 4861903 | 4455296 | 91.6% | 92.7% |
| Sonnet 5.5 | 198 | 5610842 | 5376224 | 95.8% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10360 | 128337264 | 79077888 | 61.6% | 61.7% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1399 | 23853382 | 20987392 | 88.0% | 88.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9321 | 281645058 | 262008320 | 93.0% | 93.6% |
| Sonnet 5.5 | 9731 | 234697344 | 224635504 | 95.7% | 96.4% |
