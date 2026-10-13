# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0040-20261013-090848)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 91 | 1598256 | 1409920 | 88.2% | 89.5% |
| GLM 5.3 Flash | 83 | 1297314 | 1076480 | 83.0% | 83.8% |
| GPT-6.1 Sol | 122 | 3713260 | 3425536 | 92.3% | 93.1% |
| Sonnet 5.5 | 97 | 2920282 | 2808423 | 96.2% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9894 | 119786815 | 71344896 | 59.6% | 59.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1059 | 17339845 | 15311296 | 88.3% | 89.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8847 | 268132862 | 249789568 | 93.2% | 93.7% |
| Sonnet 5.5 | 9021 | 214255767 | 205059791 | 95.7% | 96.4% |
