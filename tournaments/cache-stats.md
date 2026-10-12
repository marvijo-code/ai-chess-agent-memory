# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0035-20261012-085617)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 115 | 1896942 | 1749888 | 92.2% | 93.1% |
| GLM 5.3 Flash | 154 | 2133853 | 1839808 | 86.2% | 86.9% |
| GPT-6.1 Sol | 146 | 4327179 | 4031104 | 93.2% | 93.7% |
| Sonnet 5.5 | 173 | 4613434 | 4423781 | 95.9% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8846 | 100844964 | 53834496 | 53.4% | 53.3% |
| GLM 5.3 Flash | 288 | 3784493 | 3238848 | 85.6% | 86.3% |
| GPT-6.1 Sol | 7343 | 215269953 | 200382464 | 93.1% | 93.6% |
| Sonnet 5.5 | 7512 | 168835519 | 161235215 | 95.5% | 96.2% |
