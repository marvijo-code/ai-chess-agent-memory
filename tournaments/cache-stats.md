# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 202 | 2191627 | 896640 | 40.9% | 40.7% |
| GPT-6.1 Sol | 166 | 5502351 | 5347328 | 97.2% | 97.4% |
| Sonnet 5.5 | 166 | 4337570 | 4173652 | 96.2% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 765 | 8493289 | 4077952 | 48.0% | 48.0% |
| GPT-6.1 Sol | 628 | 18665695 | 17550080 | 94.0% | 94.3% |
| Sonnet 5.5 | 729 | 17117830 | 16431615 | 96.0% | 96.4% |
