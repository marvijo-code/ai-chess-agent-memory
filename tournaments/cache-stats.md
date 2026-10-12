# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 189 | 2958221 | 2665344 | 90.1% | 91.1% |
| GLM 5.3 Flash | 134 | 1650640 | 1399040 | 84.8% | 85.6% |
| GPT-6.1 Sol | 222 | 6754421 | 6285184 | 93.1% | 93.8% |
| Sonnet 5.5 | 334 | 9252328 | 8900397 | 96.2% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8731 | 98948022 | 52084608 | 52.6% | 52.6% |
| GLM 5.3 Flash | 134 | 1650640 | 1399040 | 84.8% | 85.6% |
| GPT-6.1 Sol | 7197 | 210942774 | 196351360 | 93.1% | 93.6% |
| Sonnet 5.5 | 7339 | 164222085 | 156811434 | 95.5% | 96.2% |
