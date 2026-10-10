# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0017-20261010-051708)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 287 | 3487779 | 2066048 | 59.2% | 59.4% |
| GPT-6.1 Sol | 145 | 3588404 | 3255296 | 90.7% | 91.0% |
| Sonnet 5.5 | 181 | 3897689 | 3721731 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4434 | 48647102 | 23244416 | 47.8% | 47.7% |
| GPT-6.1 Sol | 3654 | 105125172 | 97566336 | 92.8% | 93.3% |
| Sonnet 5.5 | 3856 | 84965795 | 81138094 | 95.5% | 96.1% |
