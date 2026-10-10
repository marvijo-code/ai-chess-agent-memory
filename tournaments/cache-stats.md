# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 165 | 1818831 | 890496 | 49.0% | 48.9% |
| GPT-6.1 Sol | 113 | 2855479 | 2657792 | 93.1% | 93.7% |
| Sonnet 5.5 | 137 | 2991674 | 2861856 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4667 | 51346267 | 24572672 | 47.9% | 47.8% |
| GPT-6.1 Sol | 3782 | 108220696 | 100432128 | 92.8% | 93.3% |
| Sonnet 5.5 | 4034 | 88762032 | 84762604 | 95.5% | 96.1% |
