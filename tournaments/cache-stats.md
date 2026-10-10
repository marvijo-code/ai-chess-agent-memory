# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 98 | 950796 | 528384 | 55.6% | 55.9% |
| GPT-6.1 Sol | 76 | 2022818 | 1860480 | 92.0% | 92.5% |
| Sonnet 5.5 | 59 | 953949 | 891474 | 93.5% | 94.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5993 | 66454267 | 32778752 | 49.3% | 49.3% |
| GPT-6.1 Sol | 4850 | 139689289 | 129922688 | 93.0% | 93.5% |
| Sonnet 5.5 | 5091 | 112383252 | 107327177 | 95.5% | 96.1% |
