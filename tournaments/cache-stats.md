# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 165 | 1818831 | 890496 | 49.0% | 48.9% |
| GPT-6.1 Sol | 106 | 2516601 | 2327040 | 92.5% | 93.2% |
| Sonnet 5.5 | 130 | 2760675 | 2635507 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4667 | 51346267 | 24572672 | 47.9% | 47.8% |
| GPT-6.1 Sol | 3775 | 107881818 | 100101376 | 92.8% | 93.3% |
| Sonnet 5.5 | 4027 | 88531033 | 84536255 | 95.5% | 96.1% |
