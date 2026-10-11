# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 95 | 988988 | 603136 | 61.0% | 61.1% |
| GPT-6.1 Sol | 50 | 978429 | 868480 | 88.8% | 90.4% |
| Sonnet 5.5 | 59 | 944848 | 882206 | 93.4% | 94.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7666 | 85790195 | 43945984 | 51.2% | 51.2% |
| GPT-6.1 Sol | 6126 | 178468397 | 166279680 | 93.2% | 93.6% |
| Sonnet 5.5 | 6285 | 137859394 | 131591276 | 95.5% | 96.1% |
