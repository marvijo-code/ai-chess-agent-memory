# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 122 | 2381067 | 2217088 | 93.1% | 94.0% |
| GLM 5.3 Flash | 92 | 1619009 | 1506304 | 93.0% | 93.6% |
| GPT-6.1 Sol | 93 | 3343859 | 3142656 | 94.0% | 94.8% |
| Sonnet 5.5 | 119 | 3125728 | 2993532 | 95.8% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8999 | 103566386 | 56361088 | 54.4% | 54.4% |
| GLM 5.3 Flash | 380 | 5403502 | 4745152 | 87.8% | 88.5% |
| GPT-6.1 Sol | 7517 | 220854615 | 205525760 | 93.1% | 93.6% |
| Sonnet 5.5 | 7700 | 173662199 | 165850494 | 95.5% | 96.2% |
