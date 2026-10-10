# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 221 | 2226879 | 923136 | 41.5% | 41.2% |
| GPT-6.1 Sol | 193 | 6303246 | 5910528 | 93.8% | 94.1% |
| Sonnet 5.5 | 184 | 4357481 | 4179291 | 95.9% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5021 | 55124145 | 26217216 | 47.6% | 47.5% |
| GPT-6.1 Sol | 4086 | 118483554 | 110070656 | 92.9% | 93.4% |
| Sonnet 5.5 | 4318 | 95425570 | 91150612 | 95.5% | 96.1% |
