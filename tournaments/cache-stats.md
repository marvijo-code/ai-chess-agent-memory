# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0034-20261012-050243)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 113 | 1585674 | 1430400 | 90.2% | 91.4% |
| GLM 5.3 Flash | 134 | 1650640 | 1399040 | 84.8% | 85.6% |
| GPT-6.1 Sol | 169 | 5511734 | 5176064 | 93.9% | 94.5% |
| Sonnet 5.5 | 181 | 4889522 | 4695231 | 96.0% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8655 | 97575475 | 50849664 | 52.1% | 52.1% |
| GLM 5.3 Flash | 134 | 1650640 | 1399040 | 84.8% | 85.6% |
| GPT-6.1 Sol | 7144 | 209700087 | 195242240 | 93.1% | 93.6% |
| Sonnet 5.5 | 7186 | 159859279 | 152606268 | 95.5% | 96.1% |
