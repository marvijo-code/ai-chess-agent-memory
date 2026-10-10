# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0015-20261010-001334)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 98 | 1019080 | 436992 | 42.9% | 42.6% |
| GPT-6.1 Sol | 72 | 1772491 | 1611520 | 90.9% | 91.2% |
| Sonnet 5.5 | 67 | 1296936 | 1225091 | 94.5% | 95.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3705 | 40154919 | 18556416 | 46.2% | 46.1% |
| GPT-6.1 Sol | 3202 | 93390282 | 86738688 | 92.9% | 93.3% |
| Sonnet 5.5 | 3361 | 74919894 | 71578873 | 95.5% | 96.1% |
