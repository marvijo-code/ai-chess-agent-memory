# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 115 | 1139977 | 572928 | 50.3% | 50.1% |
| GPT-6.1 Sol | 134 | 4170828 | 3834880 | 91.9% | 92.4% |
| Sonnet 5.5 | 114 | 2567667 | 2452661 | 95.5% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2781 | 30158621 | 13578496 | 45.0% | 44.9% |
| GPT-6.1 Sol | 2471 | 73941733 | 68803072 | 93.1% | 93.5% |
| Sonnet 5.5 | 2518 | 56098821 | 53610518 | 95.6% | 96.1% |
