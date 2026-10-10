# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 110 | 945934 | 522368 | 55.2% | 54.8% |
| GPT-6.1 Sol | 121 | 3866747 | 3590016 | 92.8% | 93.6% |
| Sonnet 5.5 | 145 | 3504843 | 3372498 | 96.2% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5189 | 56632920 | 27000320 | 47.7% | 47.6% |
| GPT-6.1 Sol | 4243 | 123296076 | 114525184 | 92.9% | 93.4% |
| Sonnet 5.5 | 4494 | 99451958 | 95008801 | 95.5% | 96.1% |
