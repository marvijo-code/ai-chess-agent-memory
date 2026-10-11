# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0032-20261011-203427)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 111 | 1426483 | 666112 | 46.7% | 46.3% |
| GPT-6.1 Sol | 71 | 2025464 | 1918592 | 94.7% | 95.4% |
| Sonnet 5.5 | 71 | 1646636 | 1564968 | 95.0% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8492 | 95487286 | 49214976 | 51.5% | 51.5% |
| GPT-6.1 Sol | 6815 | 199541441 | 185837056 | 93.1% | 93.6% |
| Sonnet 5.5 | 6849 | 151044820 | 144158765 | 95.4% | 96.1% |
