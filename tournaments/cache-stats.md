# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0035-20261012-085617)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 41 | 521282 | 470272 | 90.2% | 92.2% |
| GLM 5.3 Flash | 25 | 237502 | 193280 | 81.4% | 82.6% |
| GPT-6.1 Sol | 69 | 2096827 | 1936896 | 92.4% | 92.9% |
| Sonnet 5.5 | 24 | 473581 | 441456 | 93.2% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8772 | 99469304 | 52554880 | 52.8% | 52.8% |
| GLM 5.3 Flash | 159 | 1888142 | 1592320 | 84.3% | 85.2% |
| GPT-6.1 Sol | 7266 | 213039601 | 198288256 | 93.1% | 93.6% |
| Sonnet 5.5 | 7363 | 164695666 | 157252890 | 95.5% | 96.2% |
