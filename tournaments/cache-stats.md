# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 122 | 2381067 | 2217088 | 93.1% | 94.0% |
| GLM 5.3 Flash | 135 | 2323452 | 2145792 | 92.4% | 92.9% |
| GPT-6.1 Sol | 140 | 4819222 | 4498816 | 93.4% | 94.2% |
| Sonnet 5.5 | 161 | 4138752 | 3961335 | 95.7% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8999 | 103566386 | 56361088 | 54.4% | 54.4% |
| GLM 5.3 Flash | 423 | 6107945 | 5384640 | 88.2% | 88.8% |
| GPT-6.1 Sol | 7564 | 222329978 | 206881920 | 93.1% | 93.6% |
| Sonnet 5.5 | 7742 | 174675223 | 166818297 | 95.5% | 96.2% |
