# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 32 | 253689 | 106240 | 41.9% | 41.5% |
| GPT-6.1 Sol | 36 | 899919 | 814976 | 90.6% | 92.1% |
| Sonnet 5.5 | 35 | 599356 | 563499 | 94.0% | 95.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1736 | 19333223 | 8940416 | 46.2% | 46.2% |
| GPT-6.1 Sol | 1410 | 41166618 | 38414336 | 93.3% | 93.8% |
| Sonnet 5.5 | 1577 | 36399558 | 34857110 | 95.8% | 96.3% |
